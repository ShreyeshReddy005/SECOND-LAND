import json
import re

def calculate_irr(cash_flows):
    # Simple bisect IRR solver
    low, high = -0.5, 1.0
    for _ in range(50):
        mid = (low + high) / 2
        npv = sum(cf / ((1 + mid) ** t) for t, cf in enumerate(cash_flows))
        if npv > 0:
            low = mid
        else:
            high = mid
    return mid * 100

submarkets = ["Madhapur", "Gachibowli", "Kondapur", "Manikonda", "Serilingampally"]
types = ["Office", "Residential", "Co-living"]
rooftops = ["Low", "Medium", "High"]
plot_sizes = [1000, 1500, 2000, 2500]

scenarios = []

for n in range(60):
    submarket = submarkets[n % 5]
    prop_type = types[(n // 5) % 3]
    rooftop = rooftops[n % 3]
    floors = [4, 6, 8][n % 3]
    plot_area = plot_sizes[n % 4]
    
    fsi = 2.0
    tdr_multiplier = 2.0
    bua = plot_area * 9 * (fsi + tdr_multiplier) # sqft
    tdr_req = plot_area * tdr_multiplier # sqyd
    
    tdr_prices = {"Madhapur": 28000, "Gachibowli": 25000, "Kondapur": 20000, "Manikonda": 15000, "Serilingampally": 12000}
    tdr_price = tdr_prices.get(submarket, 15000)
    tdr_cost_cr = (tdr_req * tdr_price) / 10000000
    
    const_costs = {"Office": 2800, "Residential": 2200, "Co-living": 2500}
    const_cost_sqft = const_costs.get(prop_type, 2500)
    const_cost_cr = (bua * const_cost_sqft) / 10000000
    
    capex_cr = tdr_cost_cr + const_cost_cr
    
    rents = {"Madhapur": 95, "Gachibowli": 85, "Kondapur": 65, "Manikonda": 50, "Serilingampally": 45}
    base_rent = rents.get(submarket, 60)
    type_mult = {"Office": 1.2, "Co-living": 1.1, "Residential": 0.8}
    rent = base_rent * type_mult.get(prop_type, 1.0)
    
    noi_cr = (bua * rent * 12 * 0.85) / 10000000
    
    cap_rate = 0.08
    exit_value_cr = noi_cr / cap_rate
    
    cash_flows = [-capex_cr, noi_cr, noi_cr, noi_cr, noi_cr, noi_cr + exit_value_cr]
    irr = calculate_irr(cash_flows)
    
    confidence = 90 - (n % 15)
    if submarket in ["Madhapur", "Gachibowli"]: confidence += 5
    
    scenarios.append({
        "id": f"S{str(n+1).zfill(3)}",
        "submarket": submarket,
        "type": prop_type,
        "floors": floors,
        "rooftop": rooftop,
        "bUA": int(bua),
        "tdrReq": int(tdr_req),
        "capex": round(capex_cr, 2),
        "noi": round(noi_cr, 2),
        "irr": round(irr, 1),
        "value": round(exit_value_cr, 2),
        "confidence": confidence,
        "zone": submarket
    })

total_bua = sum(s["bUA"] for s in scenarios)
total_value = sum(s["value"] for s in scenarios)

# Update HTML
with open('Flagship-Final-Stable-No.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the IV function output
js_array = json.dumps(scenarios, separators=(',', ':'))
html = re.sub(r'function IV\(\)\{.*?\}var hh=IV\(\);', f'var hh={js_array};', html)

# Fix the headlines to match true sum
bua_lakhs = total_bua / 100000
html = re.sub(r'28\.14L MODELED BUA', f'{bua_lakhs:.2f}L MODELED BUA', html)
html = re.sub(r'1,379Cr MODELED DEVELOPMENT VALUE', f'{int(total_value):,}Cr MODELED DEVELOPMENT VALUE', html)

with open('Flagship-Final-Stable-No.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Generated 60 true scenarios. Total BUA: {bua_lakhs:.2f}L, Total Value: {int(total_value):,}Cr")
