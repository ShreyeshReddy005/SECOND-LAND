import os
import json
import asyncio
import pandas as pd
from dotenv import load_dotenv
from typesafe_sdk import AsyncTypeSafeClient, Choice

load_dotenv(r"C:\Users\SHREYESH REDDY\.gemini\antigravity\scratch\.env")

async def process_record(client, idx, record):
    address = record.get('Metadata Single Responses', '')
    if not isinstance(address, str) or len(address) < 5: return None
        
    try:
        response = await client.system_one(
            state={
                "raw_address_data": address,
                "project_status": record.get('Status', '')
            },
            questions={
                "submarket": Choice(
                    instructions="Determine the exact IT corridor submarket based on the address string.",
                    criteria={
                        "Madhapur": "Mentions Madhapur, Hi-Tech City, Raidurg, or Jubilee Hills.",
                        "Gachibowli": "Mentions Gachibowli, Nanakramguda, Financial District, or Kokapet.",
                        "Kondapur": "Mentions Kondapur, Kothaguda, or Hafeezpet.",
                        "Serilingampally": "Mentions Serilingampally.",
                        "Malkajgiri": "Mentions Malkajgiri or Secunderabad.",
                        "Kukatpally": "Mentions Kukatpally or Miyapur.",
                        "Manikonda": "Mentions Manikonda or Puppalaguda.",
                        "Malakpet": "Mentions Malakpet or Dilsukhnagar.",
                        "Rangareddy": "Mentions Rangareddy generally.",
                        "Others": "Any other location."
                    }
                )
            }
        )
        
        submarket = response.choices["submarket"].choice
        
        centers = {
            "Madhapur": [78.391, 17.441],
            "Gachibowli": [78.344, 17.437],
            "Kondapur": [78.367, 17.467],
            "Serilingampally": [78.330, 17.480],
            "Malkajgiri": [78.526, 17.447],
            "Kukatpally": [78.399, 17.494],
            "Manikonda": [78.370, 17.406],
            "Malakpet": [78.489, 17.372],
            "Rangareddy": [78.456, 17.384],
            "Others": [78.486, 17.385]
        }
        
        base_lon, base_lat = centers.get(submarket, centers["Others"])
        
        offset_lon = (idx % 10 - 5) * 0.005
        offset_lat = ((idx // 10) % 10 - 5) * 0.005
        
        lon = base_lon + offset_lon
        lat = base_lat + offset_lat
        
        market_val = 15000
        if "market_value_at_issued_time" in address:
            try:
                import re
                match = re.search(r"'market_value_at_issued_time'.*?'floatValue': (\d+\.\d+)", address)
                if match: market_val = float(match.group(1))
            except: pass
            
        authority = "GHMC"
        if "'authority'.*?'stringValue': 'HMDA'" in address: authority = "HMDA"
        elif "'authority'.*?'stringValue': 'MMC'" in address: authority = "MMC"

        avail = float(record.get('Available Balance', 0))
        initial = float(record.get('Initial Balance', avail))
        utilized = float(record.get('Utilized Balance', 0))
        issued_date = str(record.get('Issued At', '2024-01-01'))
        year = int(issued_date[:4]) if len(issued_date) >= 4 and issued_date[:4].isdigit() else 2024
        
        return {
            "id": f"TDR-{str(idx+1).zfill(4)}",
            "zone": submarket,
            "lon": lon,
            "lat": lat,
            "available": avail,
            "utilized": utilized,
            "initial": initial,
            "marketValue": market_val,
            "year": year,
            "issue_year": year,
            "authority": authority,
            "confidence": 1.0,
            "x": (lon - 78.3) * 8000 + 400,
            "y": (17.6 - lat) * 8000 + 100
        }
    except Exception as e:
        print(f"Error on {idx}: {e}")
        return None

async def main():
    df = pd.read_excel('TDR_Accounts_Cleaned.xlsx')
    df = df[df['Status'] == 'FUNCTIONAL']
    sample_records = df.head(240).to_dict('records')
    
    valid_results = []
    chunk_size = 20
    async with AsyncTypeSafeClient() as client:
        for i in range(0, len(sample_records), chunk_size):
            print(f"Processing chunk {i} to {i+chunk_size}...")
            chunk = sample_records[i:i+chunk_size]
            tasks = [process_record(client, i+idx, record) for idx, record in enumerate(chunk)]
            results = await asyncio.gather(*tasks)
            valid_results.extend([r for r in results if r is not None])
            await asyncio.sleep(1) # Small delay to avoid rate limits
            
    js_array = json.dumps(valid_results, separators=(',', ':'))
    
    with open('Flagship-Final-Stable-No.html', 'r', encoding='utf-8') as f:
        html = f.read()
        
    import re
    new_html = re.sub(r'var w6=OV\(\);', f'var w6={js_array};', html)
    
    with open('Flagship-Final-Stable-No.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
        
    print(f"Successfully processed and injected {len(valid_results)} records into HTML!")

if __name__ == "__main__":
    asyncio.run(main())
