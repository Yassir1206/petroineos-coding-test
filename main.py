
from powerplants import PowerPlants

pp = PowerPlants()

files = [
    "Wind Plants Data - Petroineos.csv",
    "gas_plants.csv",
    "Gas Fr Plants - Coding Challenge.csv"
]

for file in files:
    print(f"Processing: {file}")
    data = pp.load_new_data_from_file(file)
    pp.save_new_data(data)

print("\nLATEST DATA PER PLANT:")
print(pp.get_data_from_database())

print("\nMONTHLY AVERAGE, MIN, MAX:")
print(pp.aggregate_data_to_monthly())

print("\nTOTAL ENERGY BY COUNTRY AND TECHNOLOGY:")
print(pp.aggregate_data_to_country())
