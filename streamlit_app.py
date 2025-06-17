import streamlit as st
from pbixray.core import PBIXRay
import json
import datetime

def load_css(file_name):
    """Load CSS file and inject it into the Streamlit app"""
    try:
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning(f"CSS file {file_name} not found. Using default styling.")

def sizeof_fmt(num, suffix="B"):
    for unit in ("", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"):
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"

def app():
    # Load custom dark mode CSS
    load_css('dark_theme.css')
    
    # Enhanced page configuration
    st.set_page_config(
        page_title="PBIXRay - Power BI File Analyzer",
        page_icon="🔍",
        layout="wide",
        initial_sidebar_state="auto"
    )
    
    # Add custom styling for better dark mode appearance
    st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: 700;
        color: #ff6b6b;
        text-align: center;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .section-header {
        font-size: 1.5rem;
        font-weight: 600;
        color: #fafafa;
        margin: 1.5rem 0 1rem 0;
        border-bottom: 2px solid #ff6b6b;
        padding-bottom: 0.5rem;
    }
    .file-upload-section {
        background: linear-gradient(135deg, #1e2027 0%, #262730 100%);
        padding: 2rem;
        border-radius: 12px;
        border: 1px solid #262730;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Main title with enhanced styling
    st.markdown('<h1 class="main-header">🔍 PBIXRay - Power BI File Analyzer</h1>', unsafe_allow_html=True)
    
    # File upload section with enhanced styling
    st.markdown('<div class="file-upload-section">', unsafe_allow_html=True)
    st.markdown("### 📁 Upload Your PBIX File")
    st.markdown("Select a Power BI (.pbix) file to analyze its structure, metadata, and contents.")
    
    uploaded_file = st.file_uploader(
        "Choose a PBIX file", 
        type="pbix",
        help="Upload a .pbix file to analyze its contents and structure"
    )
    st.markdown('</div>', unsafe_allow_html=True)

    if uploaded_file:
        # Show file info
        col_info1, col_info2 = st.columns(2)
        with col_info1:
            st.info(f"📄 **File**: {uploaded_file.name}")
        with col_info2:
            st.info(f"📊 **Size**: {sizeof_fmt(uploaded_file.size)}")
        
        # Process the PBIX file
        with st.spinner("🔄 Processing PBIX file..."):
            model = PBIXRay(uploaded_file)

        # Enhanced metadata display
        st.markdown('<div class="section-header">📋 File Metadata</div>', unsafe_allow_html=True)
        
        # Create an expandable section for metadata
        with st.expander("View Detailed Metadata", expanded=False):
            st.json(model.metadata)
        
        # Enhanced metrics display
        st.markdown('<div class="section-header">📊 Quick Statistics</div>', unsafe_allow_html=True)
        met1, met2, met3 = st.columns(3)
        
        with met1:
            st.metric(
                label='📏 Model Size', 
                value=sizeof_fmt(model.size),
                help="Total size of the Power BI model"
            )
        with met2:
            st.metric(
                label='🗃️ Tables Count', 
                value=model.tables.size,
                help="Number of data tables in the model"
            )
        with met3:
            st.metric(
                label='🔗 Relationships', 
                value=model.relationships.shape[0] if not model.relationships.empty else 0,
                help="Number of relationships between tables"
            )

        # Enhanced JSON Export Section
        st.markdown('<div class="section-header">📥 Export Options</div>', unsafe_allow_html=True)
        export_col1, export_col2 = st.columns(2)
        
        with export_col1:
            st.markdown("#### 📄 Metadata Only Export")
            st.markdown("Exports schema, relationships, DAX, Power Query code, and statistics *(lightweight)*")
            
            # Generate metadata JSON
            metadata_json = model.export_metadata_json()
            file_name_base = uploaded_file.name.replace('.pbix', '')
            metadata_filename = f"{file_name_base}_metadata_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            
            st.download_button(
                label="📄 Download Metadata JSON",
                data=metadata_json,
                file_name=metadata_filename,
                mime="application/json",
                help="Download all metadata as JSON (excludes table data)",
                use_container_width=True
            )
            
        with export_col2:
            st.markdown("#### 📁 Full Export with Table Data")
            st.markdown("Includes all metadata plus actual table data *(can be large)*")
            
            # Show warning for large models
            table_count = len(model.table_names())
            if table_count > 10:
                st.warning(f"⚠️ Large model detected ({table_count} tables). Full export may take time and create a large file.")
            
            if st.button("🚀 Generate Full Export", help="Click to generate JSON with table data", use_container_width=True):
                with st.spinner("⏳ Generating full export with table data..."):
                    try:
                        full_json = model.export_metadata_json(include_table_data=True)
                        full_filename = f"{file_name_base}_full_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                        
                        st.download_button(
                            label="📁 Download Full JSON",
                            data=full_json,
                            file_name=full_filename,
                            mime="application/json",
                            help="Download complete export including table data",
                            use_container_width=True
                        )
                        st.success("✅ Full export generated successfully!")
                        
                    except Exception as e:
                        st.error(f"❌ Error generating full export: {str(e)}")

        st.divider()

        # Enhanced data display sections
        st.markdown('<div class="section-header">🏗️ Model Structure</div>', unsafe_allow_html=True)
        
        # Schema section
        with st.expander("📋 Schema Overview", expanded=True):
            if hasattr(model, 'schema') and not model.schema.empty:
                st.dataframe(model.schema, use_container_width=True)
            else:
                st.info("No schema information available")

        # Statistics section
        with st.expander("📈 Model Statistics", expanded=False):
            if hasattr(model, 'statistics') and not model.statistics.empty:
                st.dataframe(model.statistics, use_container_width=True)
            else:
                st.info("No statistics available")

        # Relationships section
        if hasattr(model, 'relationships') and model.relationships.size > 0:
            with st.expander("🔗 Table Relationships", expanded=False):
                st.dataframe(model.relationships, use_container_width=True)

        # Power Query section
        if hasattr(model, 'power_query') and model.power_query.size > 0:
            with st.expander("🔄 Power Query Code", expanded=False):
                st.dataframe(model.power_query, use_container_width=True)

        # M Parameters section
        if hasattr(model, 'm_parameters') and model.m_parameters.size > 0:
            with st.expander("⚙️ M Parameters", expanded=False):
                st.dataframe(model.m_parameters, use_container_width=True)

        # DAX sections
        if hasattr(model, 'dax_tables') and model.dax_tables.size > 0:
            with st.expander("🧮 DAX Tables", expanded=False):
                st.dataframe(model.dax_tables, use_container_width=True)
        
        if hasattr(model, 'dax_measures') and model.dax_measures.size > 0:
            with st.expander("📏 DAX Measures", expanded=False):
                st.dataframe(model.dax_measures, use_container_width=True)

        if hasattr(model, 'dax_columns') and model.dax_columns.size > 0:
            with st.expander("🧮 Calculated Columns", expanded=False):
                st.dataframe(model.dax_columns, use_container_width=True)
            
        # Enhanced Table Data Preview section
        st.markdown('<div class="section-header">🔍 Table Data Preview</div>', unsafe_allow_html=True)
        
        col_select, col_button = st.columns([3, 1])
        
        with col_select:
            table_name_input = st.selectbox(
                "Select a table to preview its contents:",
                model.tables,
                help="Choose a table from the dropdown to preview its data"
            )
        
        with col_button:
            st.markdown("<br>", unsafe_allow_html=True)  # Add spacing
            preview_button = st.button("🔍 Preview Table", use_container_width=True)

        if preview_button and table_name_input:
            with st.spinner(f"📊 Loading data from table: **{table_name_input}**"):
                try:
                    table_data = model.get_table(table_name_input)
                    
                    # Show table info
                    col_info1, col_info2, col_info3 = st.columns(3)
                    with col_info1:
                        st.metric("📊 Rows", len(table_data))
                    with col_info2:
                        st.metric("📋 Columns", len(table_data.columns))
                    with col_info3:
                        st.metric("💾 Memory", sizeof_fmt(table_data.memory_usage(deep=True).sum()))
                    
                    # Display the table
                    st.dataframe(table_data, use_container_width=True, height=400)
                    
                    st.success(f"✅ Successfully loaded {len(table_data):,} rows from table '{table_name_input}'")
                    
                except Exception as e:
                    st.error(f"❌ Error loading table data: {str(e)}")


if __name__ == '__main__':
    app()
