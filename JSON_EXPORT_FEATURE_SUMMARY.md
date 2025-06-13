# JSON Export Feature for PBIXRay

## Overview

A new JSON export feature has been successfully added to the PBIXRay library. This feature allows users to export all metadata from PBIX files in a structured JSON format for external processing, archival, or integration with other systems.

## New Method: `export_metadata_json()`

### Signature
```python
def export_metadata_json(self, file_path=None, include_table_data=False):
```

### Parameters
- **`file_path`** (str, optional): Path to save the JSON file. If `None`, returns JSON string.
- **`include_table_data`** (bool): Whether to include actual table data (default: `False`)

### Returns
- **str**: JSON string if `file_path` is `None`, otherwise returns the file path after saving.

## Usage Examples

### 1. Export as JSON String
```python
from pbixray import PBIXRay

model = PBIXRay('path/to/your/file.pbix')
json_string = model.export_metadata_json()
print(json_string)
```

### 2. Export to File (Metadata Only)
```python
model.export_metadata_json('metadata_export.json')
```

### 3. Export Including Table Data
```python
model.export_metadata_json('full_export.json', include_table_data=True)
```

## JSON Structure

The exported JSON contains the following sections:

### 1. Export Information
- Export timestamp
- PBIXRay version
- Export type

### 2. Model Information
- Model size in bytes
- Table count
- List of table names

### 3. Metadata
- **General**: Power BI configuration metadata
- **Schema**: Table and column schema information
- **Statistics**: Column cardinality and storage statistics
- **Relationships**: Model relationships and their properties

### 4. Power Query
- **Expressions**: M/Power Query code by table
- **Parameters**: M parameters with descriptions and values

### 5. DAX
- **Tables**: DAX calculated tables
- **Measures**: DAX measures with expressions
- **Columns**: Calculated column expressions

### 6. Table Data (Optional)
- Actual table contents when `include_table_data=True`

## Enhanced Features

### Streamlit Integration
The Streamlit web app (`streamlit_app.py`) now includes:
- Download buttons for metadata JSON export
- Separate option for full export with table data
- Warning for large models
- Progress indicators during export generation

### Error Handling
- Graceful handling of datetime objects
- Proper conversion of pandas DataFrames
- Exception handling for problematic tables
- UTF-8 encoding support

### File Management
- Automatic timestamp generation for unique filenames
- JSON validation before export
- Memory-efficient processing

## Files Modified

1. **`pbixray/core.py`** - Added the main export method
2. **`demo.py`** - Added demonstration examples
3. **`README.md`** - Updated documentation
4. **`streamlit_app.py`** - Enhanced web interface
5. **`test_json_export.py`** - Created comprehensive test script

## Benefits

1. **Interoperability**: JSON format enables integration with other tools and systems
2. **Archival**: Structured format for long-term metadata preservation
3. **Analysis**: Enables external analysis and processing of PBIX metadata
4. **Documentation**: Human-readable format for documentation purposes
5. **Automation**: Programmatic access to all PBIX metadata in a standard format

## Performance Considerations

- **Metadata Only**: Fast export, typically under 1MB for most models
- **With Table Data**: Can be large for models with significant data volumes
- **Memory Usage**: Efficient processing with proper DataFrame handling
- **Datetime Handling**: Automatic conversion to ISO format strings

## Testing

The feature includes comprehensive testing through:
- Unit tests in `test_json_export.py`
- Integration examples in `demo.py`
- Interactive testing via Streamlit app

This feature significantly enhances PBIXRay's utility by providing a standardized way to export and work with PBIX metadata in modern data workflows.