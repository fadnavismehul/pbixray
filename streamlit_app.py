import streamlit as st
from pbixray.core import PBIXRay
import json
import datetime

def sizeof_fmt(num, suffix="B"):
    for unit in ("", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"):
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"

def app():
    st.title("PBIX info")

    uploaded_file = st.file_uploader("Choose a PBIX file", type="pbix")
    if uploaded_file:
        # Unpack the PBIX file to get the schema_df
        model = PBIXRay(uploaded_file)

        st.write(model.metadata)
        
        met1, met2, met3 = st.columns(3)
        
        met1.metric(label='Model size', value = sizeof_fmt(model.size))
        met2.metric(label='# Tables', value = model.tables.size)
        met3.metric(label='# Relationships', value = model.relationships.shape[0] if not model.relationships.empty else 0)

        # JSON Export Section
        st.subheader("📥 Export Options")
        export_col1, export_col2 = st.columns(2)
        
        with export_col1:
            st.write("**Metadata Only Export**")
            st.write("Exports schema, relationships, DAX, Power Query code, and statistics (lightweight)")
            
            # Generate metadata JSON
            metadata_json = model.export_metadata_json()
            file_name_base = uploaded_file.name.replace('.pbix', '')
            metadata_filename = f"{file_name_base}_metadata_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            
            st.download_button(
                label="📄 Download Metadata JSON",
                data=metadata_json,
                file_name=metadata_filename,
                mime="application/json",
                help="Download all metadata as JSON (excludes table data)"
            )
            
        with export_col2:
            st.write("**Full Export with Table Data**")
            st.write("Includes all metadata plus actual table data (can be large)")
            
            # Show warning for large models
            table_count = len(model.table_names())
            if table_count > 10:
                st.warning(f"⚠️ Large model detected ({table_count} tables). Full export may take time and create a large file.")
            
            if st.button("Generate Full Export", help="Click to generate JSON with table data"):
                with st.spinner("Generating full export with table data..."):
                    try:
                        full_json = model.export_metadata_json(include_table_data=True)
                        full_filename = f"{file_name_base}_full_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                        
                        st.download_button(
                            label="📁 Download Full JSON",
                            data=full_json,
                            file_name=full_filename,
                            mime="application/json",
                            help="Download complete export including table data"
                        )
                        st.success("✅ Full export generated successfully!")
                        
                    except Exception as e:
                        st.error(f"❌ Error generating full export: {str(e)}")

        st.divider()

        st.write("Schema:")
        st.write(model.schema)

        st.write("Statistics:")
        st.dataframe(model.statistics)

        if model.relationships.size:
            st.write("Relationships:")
            st.write(model.relationships)

        if model.power_query.size:
            st.write("Power Query code:")
            st.dataframe(model.power_query)

        if model.m_parameters.size:
            st.write("M parameters:")
            st.dataframe(model.m_parameters)

        if model.dax_tables.size:
            st.write("DAX tables:")
            st.dataframe(model.dax_tables)
        
        if model.dax_measures.size:
            st.write("DAX measures:")
            st.dataframe(model.dax_measures)

        if model.dax_columns.size:
            st.write("Calculated columns:")
            st.dataframe(model.dax_columns)
            
        # Let the user select a table name
        st.subheader("🔍 Table Data Preview")
        table_name_input = st.selectbox("Select a table to peek at its contents:", model.tables)

        if st.button("Un-VertiPaq"):
            with st.spinner(f"Loading data from table: {table_name_input}"):
                try:
                    table_data = model.get_table(table_name_input)
                    st.dataframe(table_data, use_container_width=True)
                    st.info(f"Showing {len(table_data)} rows from table '{table_name_input}'")
                except Exception as e:
                    st.error(f"Error loading table data: {str(e)}")


if __name__ == '__main__':
    app()
