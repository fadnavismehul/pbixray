# ---------- IMPORTS ----------

from .pbix_unpacker import PbixUnpacker
from .vertipaq_decoder import VertiPaqDecoder
from .meta.metadata_handler import MetadataHandler
from .utils import WINDOWS_EPOCH_START
import datetime
import json
import pandas as pd

# ---------- MAIN CLASS ----------

class PBIXRay:
    def __init__(self, file_path):
        unpacker = PbixUnpacker(file_path)
        
        self._metadata_handler = MetadataHandler(unpacker.data_model)
        self._vertipaq_decoder = VertiPaqDecoder(self._metadata_handler.metadata, unpacker.data_model)
        
    def get_table(self, table_name):
        """Generates a DataFrame representation of the specified table."""
        return self._vertipaq_decoder.get_table(table_name)

    def export_metadata_json(self, file_path=None, include_table_data=False):
        """
        Exports all metadata as JSON format.
        
        Args:
            file_path (str, optional): Path to save the JSON file. If None, returns JSON string.
            include_table_data (bool): Whether to include actual table data (can be large).
            
        Returns:
            str: JSON string if file_path is None, otherwise saves to file and returns the file path.
        """
        
        def _convert_dataframe_to_dict(df):
            """Convert DataFrame to dict, handling datetime objects."""
            if df is None or df.empty:
                return []
            
            # Convert datetime columns to ISO format strings
            df_copy = df.copy()
            for col in df_copy.columns:
                if pd.api.types.is_datetime64_any_dtype(df_copy[col]):
                    df_copy[col] = df_copy[col].dt.strftime('%Y-%m-%d %H:%M:%S')
            
            return df_copy.to_dict('records')
        
        metadata_export = {
            "export_info": {
                "exported_at": datetime.datetime.now().isoformat(),
                "pbixray_version": "1.0.0",  # You may want to make this dynamic
                "export_type": "full_metadata"
            },
            "model_info": {
                "size_bytes": self.size,
                "table_count": len(self.table_names()),
                "table_names": self.table_names()
            },
            "metadata": {
                "general": _convert_dataframe_to_dict(self.metadata),
                "schema": _convert_dataframe_to_dict(self.schema),
                "statistics": _convert_dataframe_to_dict(self.statistics),
                "relationships": _convert_dataframe_to_dict(self.relationships)
            },
            "power_query": {
                "expressions": _convert_dataframe_to_dict(self.power_query),
                "parameters": _convert_dataframe_to_dict(self.m_parameters)
            },
            "dax": {
                "tables": _convert_dataframe_to_dict(self.dax_tables),
                "measures": _convert_dataframe_to_dict(self.dax_measures),
                "columns": _convert_dataframe_to_dict(self.dax_columns)
            }
        }
        
        # Optionally include table data
        if include_table_data:
            metadata_export["table_data"] = {}
            for table_name in self.table_names():
                try:
                    table_df = self.get_table(table_name)
                    metadata_export["table_data"][table_name] = _convert_dataframe_to_dict(table_df)
                except Exception as e:
                    metadata_export["table_data"][table_name] = {"error": str(e)}
        
        # Convert to JSON string
        json_string = json.dumps(metadata_export, indent=2, ensure_ascii=False)
        
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(json_string)
            return file_path
        else:
            return json_string

    # ---------- PROPERTIES ----------

    @property   
    def tables(self):
        return self._metadata_handler.tables
    
    def table_names(self):
        """Returns a simple Python list of all table names in the model."""
        return self.tables.tolist()
    
    @property
    def statistics(self):
        return self._metadata_handler.stats
    
    @property
    def power_query(self):
        return self._metadata_handler.metadata.m_df
    
    @property
    def m_parameters(self):
        df = self._metadata_handler.metadata.m_parameters_df
        return df if df.empty else df.assign(
            ModifiedTime=lambda df: df['ModifiedTime'].apply(
                lambda x: WINDOWS_EPOCH_START + datetime.timedelta(seconds=x / 1e7)
            )
        )

    @property
    def dax_tables(self):
        return self._metadata_handler.metadata.dax_tables_df
    
    @property
    def dax_measures(self):
        return self._metadata_handler.metadata.dax_measures_df
    
    @property
    def dax_columns(self):
        return self._metadata_handler.metadata.dax_columns_df
    
    @property
    def metadata(self):
        return self._metadata_handler.metadata.metadata_df
    
    @property
    def size(self):
        return self._metadata_handler.size
    
    @property
    def schema(self):
        return  self._metadata_handler.schema
    
    @property
    def relationships(self):
        return self._metadata_handler.metadata.relationships_df
