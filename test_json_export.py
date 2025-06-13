#!/usr/bin/env python3
"""
Test script for the new JSON export feature in PBIXRay.
This script demonstrates the usage of the export_metadata_json method.
"""

from pbixray import PBIXRay
import json
import os

def test_json_export():
    """Test the JSON export functionality with different options."""
    
    # Test data files (you'll need actual PBIX files in the data directory)
    test_files = [
        "data/Sales & Returns Sample v201912.pbix",
        "data/Adventure Works DW 2020.pbix",
        "data/Excalidraw.pbix"
    ]
    
    for pbix_file in test_files:
        if not os.path.exists(pbix_file):
            print(f"Skipping {pbix_file} - file not found")
            continue
            
        print(f"\n{'='*60}")
        print(f"Testing JSON export for: {pbix_file}")
        print(f"{'='*60}")
        
        try:
            # Initialize PBIXRay
            model = PBIXRay(pbix_file)
            
            # Test 1: Export as JSON string
            print("Test 1: Exporting metadata as JSON string...")
            json_string = model.export_metadata_json()
            print(f"✓ JSON string generated (length: {len(json_string)} characters)")
            
            # Validate JSON structure
            parsed_json = json.loads(json_string)
            required_keys = ['export_info', 'model_info', 'metadata', 'power_query', 'dax']
            
            for key in required_keys:
                if key in parsed_json:
                    print(f"✓ JSON contains required section: {key}")
                else:
                    print(f"✗ JSON missing required section: {key}")
            
            # Test 2: Export to file (metadata only)
            base_name = os.path.basename(pbix_file).replace('.pbix', '')
            output_file = f"{base_name}_metadata.json"
            print(f"\nTest 2: Exporting metadata to file: {output_file}")
            
            result_path = model.export_metadata_json(output_file)
            if os.path.exists(result_path):
                file_size = os.path.getsize(result_path)
                print(f"✓ File created successfully: {result_path} ({file_size} bytes)")
            else:
                print(f"✗ File creation failed: {result_path}")
            
            # Test 3: Show some sample data from the JSON
            print(f"\nTest 3: Sample data from JSON export:")
            print(f"  - Model size: {parsed_json['model_info']['size_bytes']} bytes")
            print(f"  - Table count: {parsed_json['model_info']['table_count']}")
            print(f"  - Table names: {', '.join(parsed_json['model_info']['table_names'][:3])}...")
            print(f"  - Export timestamp: {parsed_json['export_info']['exported_at']}")
            
            # Test 4: Export with table data (only for smaller models)
            table_count = parsed_json['model_info']['table_count']
            if table_count <= 5:  # Only test with small models
                print(f"\nTest 4: Exporting with table data...")
                output_file_full = f"{base_name}_full.json"
                result_path_full = model.export_metadata_json(output_file_full, include_table_data=True)
                
                if os.path.exists(result_path_full):
                    file_size_full = os.path.getsize(result_path_full)
                    print(f"✓ Full export created: {result_path_full} ({file_size_full} bytes)")
                else:
                    print(f"✗ Full export failed: {result_path_full}")
            else:
                print(f"\nTest 4: Skipping table data export (too many tables: {table_count})")
                
        except Exception as e:
            print(f"✗ Error processing {pbix_file}: {str(e)}")
            continue

def main():
    """Main test function."""
    print("PBIXRay JSON Export Feature Test")
    print("="*60)
    
    # Check if pbixray is importable
    try:
        from pbixray import PBIXRay
        print("✓ PBIXRay imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import PBIXRay: {e}")
        return
    
    # Check if data directory exists
    if not os.path.exists("data"):
        print("✗ Data directory not found. Please ensure PBIX files are in the 'data' directory.")
        return
    
    test_json_export()
    
    print(f"\n{'='*60}")
    print("JSON Export Test Completed")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()