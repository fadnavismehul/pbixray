from pbixray import PBIXRay

# Example usage of the new table_names feature
def demonstrate_table_names():
    """Demonstrate the new table_names method vs the existing tables property."""
    
    # Load a PBIX file (you'll need to update the path to your actual file)
    PBIX_FILE_PATH = "data/Sales & Returns Sample v201912.pbix"
    
    try:
        model = PBIXRay(PBIX_FILE_PATH)
        
        print("=== Table Names Feature Demonstration ===\n")
        
        # Current tables property (returns numpy array)
        tables_array = model.tables
        print(f"model.tables (numpy array):")
        print(f"  Type: {type(tables_array)}")
        print(f"  Content: {tables_array}")
        print(f"  Length: {len(tables_array)}")
        print()
        
        # New table_names method (returns Python list)
        table_names_list = model.table_names()
        print(f"model.table_names() (Python list):")
        print(f"  Type: {type(table_names_list)}")
        print(f"  Content: {table_names_list}")
        print(f"  Length: {len(table_names_list)}")
        print()
        
        # Show practical usage examples
        print("=== Practical Usage Examples ===")
        print("\n1. Easy iteration over table names:")
        for table_name in model.table_names():
            print(f"   - {table_name}")
        
        print("\n2. Quick check if a table exists:")
        target_table = "Age"
        if target_table in model.table_names():
            print(f"   ✓ Table '{target_table}' exists in the model")
        
        print("\n3. Get table count:")
        print(f"   Total tables: {len(model.table_names())}")
        
        print("\n4. Convert to other data structures:")
        table_set = set(model.table_names())
        print(f"   As set: {table_set}")
        
    except FileNotFoundError:
        print(f"Please update the PBIX_FILE_PATH to point to a valid PBIX file.")
        print("The demonstration shows the structure of the new feature.")
        
        # Show the expected output structure
        print("\n=== Expected Output Structure ===")
        print("model.tables (numpy array):")
        print("  Type: <class 'numpy.ndarray'>")
        print("  Content: ['Table1' 'Table2' 'Table3']")
        print()
        print("model.table_names() (Python list):")
        print("  Type: <class 'list'>")
        print("  Content: ['Table1', 'Table2', 'Table3']")

if __name__ == "__main__":
    demonstrate_table_names()