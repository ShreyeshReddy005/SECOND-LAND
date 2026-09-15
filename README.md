# SECOND LAND: Real Estate Financial Dashboard (Compiled Demo)

<p align="center">
  <img src="./assets/hero.png" alt="Second Land Dashboard" width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" />
  <img src="https://img.shields.io/badge/MapLibre-000000?style=for-the-badge&logo=maplibre&logoColor=white" />
  <img src="https://img.shields.io/badge/Status-Compiled_Proof_of_Concept-F6A820?style=for-the-badge" />
</p>

## Overview

**SECOND LAND** is a highly specialized financial modeling dashboard built for institutional real estate analysis in the IT Corridors of Hyderabad (Madhapur, Gachibowli, Kondapur). 

It models the complex urban economics of **Transferable Development Rights (TDR)** under recent Government Orders, demonstrating how buying air rights impacts base land value, vertical expansion (BUA), and financial feasibility across **60 distinct deterministic scenarios**.

> **Note on Repository State**: This repository currently serves as a **compiled proof-of-concept demonstration**. The application is bundled into a single, offline-ready file (Flagship-Final-Stable-No.html). The raw React/Vite source code is not currently published here, as this repo is intended to showcase the UI, spatial integration, and financial thesis in a zero-dependency, instantly runnable format.

## Regulatory Thesis & Methodology

This tool replaces traditional clunky Excel models (e.g., Institutional_LGSF_CoLiving_Master_Model.xlsx) by providing a genuine analytical interface. The modeling engine is strictly grounded in recent Telangana regulatory shifts:

* **G.O. Ms. No. 16 (16.01.2026)**: Introduction of updated TDR grant provisions.
* **G.O. Ms. No. 95 (21.03.2026)**: Amended Telangana Building Rules 2012, setting the 21 m high-rise threshold, TDR-mandated 18–21 m band for 750–2000 sq.m plots, and 50% TDR loading requirements before Occupancy Certificate.

The 60 scenarios are deterministic, based on current datasets:
* Location matching: 90%+
* TDR Pricing inputs: 80%+
* Structural limits: 70%+
* Rent curves: 85%+
* Regulatory compliance: 95%
*(Average 82% deterministic confidence).*

### Data Provenance
* *TS-RERA Projects Data*: Scraped and cleaned from public registries (Q1 2026).
* *TDR Accounts Data*: Publicly issued TDR certificates registry.
* *Notice*: This data is provided for academic/portfolio demonstration only and should not be used for live commercial underwriting without independent verification.

## Features

### 🏛️ The 3D Feasibility Cube
A custom-built, isometric 3D rendering engine built purely with SVG math to visualize the 'stack'. It allows stakeholders to instantly comprehend the physical relationship between the base allowable build and the vertical extension unlocked by TDR capital.

### 📊 Spatial Financial Modeling
Takes complex financial outputs (IRR, NOI, CAPEX, Downside Resilience) and integrates them directly into a **MapLibre** geographic environment.

### ⚡ Apple HIG Compliant 'Swiss Editorial' Design
The UI adheres strictly to Apple's Human Interface Guidelines for accessibility (touch targets, contrast ratios, typography scaling) while maintaining a dense, research-grade 'Swiss editorial' aesthetic.

## Usage

Simply clone the repository and double-click Flagship-Final-Stable-No.html to open it in any modern browser. It requires no installation, no local server, and runs 100% offline.

`ash
git clone https://github.com/ShreyeshReddy005/SECOND-LAND.git
# Double-click Flagship-Final-Stable-No.html
`

## Roadmap & Known Limitations

* **Jurisdictional Shifts**: The dashboard currently models the GHMC framework. Future updates will need to account for the February 2026 CURE reorganization (Cyberabad Municipal Corporation).
* **TDR Price Sensitivity**: TDR prices are volatile (currently pegged at ₹300–400/sq.ft impact based on G.O. 95). A live sensitivity slider is planned for the next release.
* **Source Release**: Extraction and publication of the raw Vite/React component tree and unit tests to verify the IRR/NOI mathematical core.

## License
MIT License
