import pandas as pd
import json

# Load your Excel file (make sure the name matches your file)
df = pd.read_excel('products_catalog.xlsx')

# Convert to list of dicts for JSON export
products = df.to_dict(orient='records')

# Overwrite products_catalog.json with latest data from Excel
with open('products_catalog.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, ensure_ascii=False, indent=2)

print("products_catalog.json updated from Excel.")
