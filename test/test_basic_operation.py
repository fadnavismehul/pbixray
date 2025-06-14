import pytest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pbix')))

from pbixray import PBIXRay

PBIX_FILE_PATH = r"C:\git\hub\pbixray\data\Sales & Returns Sample v201912.pbix"
# C:\git\hub\pbixray\data\Excalidraw.pbix

def test_initialization():
    """Test initialization of the library with the test PBIX file."""
    model = PBIXRay(PBIX_FILE_PATH)
    assert model is not None, "Failed to initialize PBIXRay with the test PBIX file."

def test_metadata_retrieval():
    """Test retrieval of metadata (tables, columns)."""
    model = PBIXRay(PBIX_FILE_PATH)
    
    tables = model.tables
    #test number of tables greater than 0
    assert tables.size, "No tables found in the PBIX file."
    
    assert "Age" in tables, "Expected table 'Age' not found in the PBIX file."
    
def test_data_retrieval():
    """Test data retrieval from a specific table."""
    model = PBIXRay(PBIX_FILE_PATH)
    
    table = model.get_table("Age")
    assert table.size, "Failed to retrieve the 'Age' table."

def test_table_names_method():
    """Test the new table_names method returns a Python list."""
    model = PBIXRay(PBIX_FILE_PATH)
    
    # Test the new table_names method
    table_names = model.table_names()
    assert isinstance(table_names, list), "table_names() should return a Python list."
    assert len(table_names) > 0, "table_names() should return a non-empty list."
    assert "Age" in table_names, "Expected table 'Age' not found in table_names list."
    
    # Verify it returns the same content as tables property but as a list
    tables_array = model.tables
    assert set(table_names) == set(tables_array), "table_names() should contain the same tables as tables property."
