import streamlit as st
from pbixray.core import PBIXRay
import json
import datetime
from design_tokens import GrabDesignTokens, get_streamlit_theme_css

def sizeof_fmt(num, suffix="B"):
    for unit in ("", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"):
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"

def app():
    # Apply Grab Duxton Design theme
    st.markdown(get_streamlit_theme_css(), unsafe_allow_html=True)
    
    # Page configuration
    st.set_page_config(
        page_title="PBIXRay - Power BI File Analyzer",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # Header with branding
    st.markdown(
        """
        <div style="text-align: center; padding: 1rem 0; background: linear-gradient(135deg, #00B14F 0%, #33C473 100%); 
                    color: white; border-radius: 0.75rem; margin-bottom: 2rem; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);">
            <h1 style="margin: 0; color: white !important; border: none !important; padding: 0 !important;">
                📊 PBIXRay
            </h1>
            <p style="margin: 0; opacity: 0.9; font-size: 1.125rem;">
                Power BI File Analysis Tool
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # File upload section
    st.markdown("### 📁 Upload PBIX File")
    uploaded_file = st.file_uploader(
        "Choose a PBIX file to analyze", 
        type="pbix",
        help="Upload your Power BI (.pbix) file to extract and analyze its contents"
    )
    
    if uploaded_file:
        # Initialize PBIXRay model
        with st.spinner("🔍 Analyzing PBIX file..."):
            model = PBIXRay(uploaded_file)

        # Model metadata section
        st.markdown("### 📋 Model Information")
        with st.expander("View Metadata", expanded=False):
            st.json(model.metadata)
        
        # Key metrics section
        st.markdown("### 📊 Key Metrics")
        met1, met2, met3 = st.columns(3)
        
        with met1:
            st.metric(
                label="📦 Model Size", 
                value=sizeof_fmt(model.size),
                help="Total size of the PBIX file"
            )
        
        with met2:
            st.metric(
                label="🗂️ Tables", 
                value=model.tables.size,
                help="Number of data tables in the model"
            )
        
        with met3:
            st.metric(
                label="🔗 Relationships", 
                value=model.relationships.shape[0] if not model.relationships.empty else 0,
                help="Number of relationships between tables"
            )

        # Export options section
        st.markdown("### 📥 Export Options")
        export_col1, export_col2 = st.columns(2)
        
        with export_col1:
            st.markdown("#### 📄 Metadata Only Export")
            st.markdown(
                """
                <div style="padding: 1rem; background-color: #E6F2FF; border-radius: 0.5rem; border-left: 4px solid #0066CC; margin-bottom: 1rem;">
                    <p style="margin: 0; color: #212529;">
                        Exports schema, relationships, DAX, Power Query code, and statistics (lightweight)
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )
            
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
            
            # Show warning for large models
            table_count = len(model.table_names())
            if table_count > 10:
                st.warning(f"⚠️ Large model detected ({table_count} tables). Full export may take time and create a large file.")
            else:
                st.markdown(
                    """
                    <div style="padding: 1rem; background-color: #E6F7ED; border-radius: 0.5rem; border-left: 4px solid #00B14F; margin-bottom: 1rem;">
                        <p style="margin: 0; color: #212529;">
                            Includes all metadata plus actual table data (can be large)
                        </p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            
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

        # Schema and data sections
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 🗂️ Schema Overview")
            with st.expander("View Schema Details", expanded=False):
                st.dataframe(model.schema, use_container_width=True)

        with col2:
            st.markdown("### 📈 Statistics")
            with st.expander("View Statistics", expanded=False):
                st.dataframe(model.statistics, use_container_width=True)

        # Relationships section
        if model.relationships.size:
            st.markdown("### 🔗 Relationships")
            with st.expander("View Relationships", expanded=False):
                st.dataframe(model.relationships, use_container_width=True)

        # Power Query section
        if model.power_query.size:
            st.markdown("### ⚡ Power Query Code")
            with st.expander("View Power Query Code", expanded=False):
                st.dataframe(model.power_query, use_container_width=True)

        # M Parameters section
        if model.m_parameters.size:
            st.markdown("### 🔧 M Parameters")
            with st.expander("View M Parameters", expanded=False):
                st.dataframe(model.m_parameters, use_container_width=True)

        # DAX sections
        if model.dax_tables.size:
            st.markdown("### 📊 DAX Tables")
            with st.expander("View DAX Tables", expanded=False):
                st.dataframe(model.dax_tables, use_container_width=True)
        
        if model.dax_measures.size:
            st.markdown("### 📏 DAX Measures")
            with st.expander("View DAX Measures", expanded=False):
                st.dataframe(model.dax_measures, use_container_width=True)

        if model.dax_columns.size:
            st.markdown("### 🧮 Calculated Columns")
            with st.expander("View Calculated Columns", expanded=False):
                st.dataframe(model.dax_columns, use_container_width=True)
            
        # Table data preview section
        st.markdown("### 🔍 Table Data Preview")
        preview_col1, preview_col2 = st.columns([2, 1])
        
        with preview_col1:
            table_name_input = st.selectbox(
                "Select a table to preview its contents:",
                model.tables,
                help="Choose a table to view its data structure and content"
            )
        
        with preview_col2:
            st.markdown("<br>", unsafe_allow_html=True)  # Add spacing
            if st.button("🔓 Un-VertiPaq", help="Click to load and display table data", use_container_width=True):
                with st.spinner(f"⏳ Loading data from table: {table_name_input}"):
                    try:
                        table_data = model.get_table(table_name_input)
                        st.markdown(f"#### 📋 Data from '{table_name_input}'")
                        st.dataframe(table_data, use_container_width=True)
                        st.info(f"📊 Showing {len(table_data)} rows from table '{table_name_input}'")
                    except Exception as e:
                        st.error(f"❌ Error loading table data: {str(e)}")
    
    else:
        # Welcome message when no file is uploaded
        st.markdown(
            """
            <div style="text-align: center; padding: 3rem; background-color: #E6F7ED; border-radius: 1rem; margin: 2rem 0;">
                <h3 style="color: #00B14F; margin-bottom: 1rem;">Welcome to PBIXRay! 🎉</h3>
                <p style="color: #212529; font-size: 1.125rem; margin-bottom: 1.5rem;">
                    Upload a Power BI (.pbix) file to start analyzing its contents, relationships, and data.
                </p>
                <div style="display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap;">
                    <div style="background: white; padding: 1.5rem; border-radius: 0.75rem; box-shadow: 0 2px 4px rgba(0,0,0,0.1); max-width: 200px;">
                        <h4 style="color: #00B14F; margin-bottom: 0.5rem;">📊 Analyze</h4>
                        <p style="color: #6C757D; font-size: 0.875rem; margin: 0;">Extract metadata, schema, and relationships</p>
                    </div>
                    <div style="background: white; padding: 1.5rem; border-radius: 0.75rem; box-shadow: 0 2px 4px rgba(0,0,0,0.1); max-width: 200px;">
                        <h4 style="color: #0066CC; margin-bottom: 0.5rem;">📥 Export</h4>
                        <p style="color: #6C757D; font-size: 0.875rem; margin: 0;">Download data in JSON format</p>
                    </div>
                    <div style="background: white; padding: 1.5rem; border-radius: 0.75rem; box-shadow: 0 2px 4px rgba(0,0,0,0.1); max-width: 200px;">
                        <h4 style="color: #17A2B8; margin-bottom: 0.5rem;">🔍 Preview</h4>
                        <p style="color: #6C757D; font-size: 0.875rem; margin: 0;">View table contents and DAX code</p>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


if __name__ == '__main__':
    app()
