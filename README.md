# Petroineos Coding Test – Power Plant Data Pipeline

This project is a submission for the Petroineos 2025 Summer Internship coding test. It processes power plant production data from multiple CSV files and outputs key operational insights.

---

## 🧩 What It Does

- ✅ Loads and cleans wind and gas plant production data
- ✅ Saves it to a persistent CSV-based "database"
- ✅ Generates three key outputs:
  - 🔹 Latest data for each plant
  - 🔹 Monthly average, min, max production
  - 🔹 Total energy output by country and technology

---

## 🗂️ Files in This Repo

| File | Description |
|------|-------------|
| `main.py` | Script to run the full process |
| `powerplants.py` | Contains all logic for data processing and analysis |
| `gas_plants.csv` | Raw UK gas plant data |
| `Gas Fr Plants - Coding Challenge.csv` | Raw France gas plant data |
| `Wind Plants Data - Petroineos.csv` | Raw UK wind plant data |
| `Coding Challenge Database.csv` | Output file that stores merged and cleaned data |

---

## ⚙️ How to Run

Make sure you have **Python 3** and **pandas** installed.

1. Clone the repo or download the files
2. In your terminal, run:

```bash
pip install pandas
python3 main.py
