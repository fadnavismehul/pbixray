from pbixray import PBIXRay
from icecream import ic

# PBIX_FILE_PATH = r"data/Excalidraw.pbix"
PBIX_FILE_PATH = r"data/Sales & Returns Sample v201912.pbix"
model = PBIXRay(PBIX_FILE_PATH)
ic(model.tables)
ic(model.metadata)
ic(model.power_query)
ic(model.statistics)
ic(model.dax_tables)
ic(model.dax_measures)
ic(model.size)
ic(model.schema)
ic(model.relationships)
ic(model.get_table("Age"))

# Demonstrate new JSON export functionality
print("\n" + "="*50)
print("JSON EXPORT EXAMPLES")
print("="*50)

# Export metadata to JSON string (without table data)
json_metadata = model.export_metadata_json()
print(f"JSON metadata length: {len(json_metadata)} characters")

# Export metadata to file (without table data)
json_file_path = model.export_metadata_json("sales_returns_metadata.json")
print(f"Metadata exported to: {json_file_path}")

# Export metadata to file including table data (warning: can be large)
json_file_with_data = model.export_metadata_json("sales_returns_full.json", include_table_data=True)
print(f"Full metadata with table data exported to: {json_file_with_data}")

PBIX_FILE_PATH = r"data/Adventure Works DW 2020.pbix"
model = PBIXRay(PBIX_FILE_PATH)
ic(model.tables)
ic(model.metadata)
ic(model.power_query)
ic(model.statistics)
ic(model.dax_tables)
ic(model.dax_measures)
ic(model.size)
ic(model.schema)
ic(model.relationships)
ic(model.get_table("Sales Order"))

# JSON export for Adventure Works
json_file_path = model.export_metadata_json("adventure_works_metadata.json")
print(f"Adventure Works metadata exported to: {json_file_path}")

model = PBIXRay(r"data/Excalidraw.pbix")
ic(model.tables)
ic(model.metadata)
ic(model.power_query)
ic(model.statistics)
ic(model.dax_tables)
ic(model.dax_measures)
ic(model.size)
ic(model.schema)
ic(model.relationships)
ic(model.dax_columns)
ic(model.get_table("Fruit_RLE"))

# JSON export for Excalidraw
json_file_path = model.export_metadata_json("excalidraw_metadata.json")
print(f"Excalidraw metadata exported to: {json_file_path}")

model = PBIXRay(r"data/2020SU11 Blog Demo - November.pbix")
ic(model.tables)
ic(model.metadata)
ic(model.power_query)
ic(model.statistics)
ic(model.dax_tables)
ic(model.dax_measures)
ic(model.dax_columns)
ic(model.size)
ic(model.schema)
ic(model.relationships)
ic(model.get_table("Reseller"))

model = PBIXRay(r"data/2020SU11 Blog Demo - November.pbix")
ic(model.tables)
ic(model.metadata)
ic(model.m_parameters)
ic(model.statistics)

model = PBIXRay(r"data/old-Supplier-Quality-Analysis-Sample-PBIX.pbix")
ic(model.tables)
ic(model.metadata)
ic(model.m_parameters)
ic(model.statistics)
ic(model.dax_tables)
ic(model.dax_measures)
ic(model.dax_columns)
ic(model.size)
ic(model.schema)
ic(model.relationships)
ic(model.get_table("Vendor"))

# Final JSON export demo
json_file_path = model.export_metadata_json("supplier_quality_metadata.json")
print(f"Supplier Quality metadata exported to: {json_file_path}")

print("\n" + "="*50)
print("JSON EXPORT FEATURE DEMO COMPLETED")
print("="*50)