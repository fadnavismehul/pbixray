# Grab Duxton Design Tokens
# Color scheme following Grab's brand guidelines and design principles

class GrabDesignTokens:
    """
    Design tokens for Grab Duxton Design System
    Following Grab's brand guidelines with their signature green (#00B14F) as primary
    """
    
    # Primary Brand Colors
    PRIMARY = "#00B14F"  # Grab Green (PMS 355C)
    PRIMARY_LIGHT = "#33C473"
    PRIMARY_LIGHTER = "#66D797"
    PRIMARY_LIGHTEST = "#E6F7ED"
    PRIMARY_DARK = "#008A3B"
    PRIMARY_DARKER = "#006428"
    
    # Secondary Colors
    SECONDARY = "#0066CC"  # Digital Blue
    SECONDARY_LIGHT = "#3385D6"
    SECONDARY_LIGHTER = "#66A3E0"
    SECONDARY_LIGHTEST = "#E6F2FF"
    
    # Neutral Colors
    NEUTRAL_WHITE = "#FFFFFF"
    NEUTRAL_LIGHT = "#F8F9FA"
    NEUTRAL_LIGHTER = "#E9ECEF"
    NEUTRAL_DEFAULT = "#6C757D"
    NEUTRAL_DARK = "#495057"
    NEUTRAL_DARKER = "#343A40"
    NEUTRAL_DARKEST = "#212529"
    
    # Semantic Colors
    SUCCESS = "#28A745"
    SUCCESS_LIGHT = "#D4EDDA"
    WARNING = "#FFC107"
    WARNING_LIGHT = "#FFF3CD"
    ERROR = "#DC3545"
    ERROR_LIGHT = "#F8D7DA"
    INFO = "#17A2B8"
    INFO_LIGHT = "#D1ECF1"
    
    # Text Colors
    TEXT_PRIMARY = "#212529"
    TEXT_SECONDARY = "#6C757D"
    TEXT_MUTED = "#ADB5BD"
    TEXT_ON_PRIMARY = "#FFFFFF"
    TEXT_ON_DARK = "#FFFFFF"
    
    # Border Colors
    BORDER_DEFAULT = "#DEE2E6"
    BORDER_LIGHT = "#F1F3F4"
    BORDER_FOCUS = PRIMARY
    
    # Background Colors
    BACKGROUND_DEFAULT = "#FFFFFF"
    BACKGROUND_LIGHT = "#F8F9FA"
    BACKGROUND_DARK = "#343A40"
    BACKGROUND_PRIMARY = PRIMARY
    
    # Spacing Scale (in rem units)
    SPACE_XS = "0.25rem"    # 4px
    SPACE_SM = "0.5rem"     # 8px
    SPACE_MD = "1rem"       # 16px
    SPACE_LG = "1.5rem"     # 24px
    SPACE_XL = "2rem"       # 32px
    SPACE_XXL = "3rem"      # 48px
    
    # Typography
    FONT_FAMILY_PRIMARY = '"Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif'
    FONT_SIZE_XS = "0.75rem"   # 12px
    FONT_SIZE_SM = "0.875rem"  # 14px
    FONT_SIZE_MD = "1rem"      # 16px
    FONT_SIZE_LG = "1.125rem"  # 18px
    FONT_SIZE_XL = "1.25rem"   # 20px
    FONT_SIZE_XXL = "1.5rem"   # 24px
    FONT_SIZE_XXXL = "2rem"    # 32px
    
    # Border Radius
    RADIUS_SM = "0.25rem"   # 4px
    RADIUS_MD = "0.5rem"    # 8px
    RADIUS_LG = "0.75rem"   # 12px
    RADIUS_XL = "1rem"      # 16px
    
    # Shadows
    SHADOW_SM = "0 1px 2px 0 rgba(0, 0, 0, 0.05)"
    SHADOW_MD = "0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)"
    SHADOW_LG = "0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)"
    SHADOW_XL = "0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)"


def get_streamlit_theme_css():
    """Generate CSS for Streamlit theming with Grab Duxton Design tokens"""
    tokens = GrabDesignTokens()
    
    return f"""
    <style>
    /* Import Inter font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Root variables */
    :root {{
        --primary-color: {tokens.PRIMARY};
        --primary-light: {tokens.PRIMARY_LIGHT};
        --primary-lightest: {tokens.PRIMARY_LIGHTEST};
        --secondary-color: {tokens.SECONDARY};
        --text-primary: {tokens.TEXT_PRIMARY};
        --text-secondary: {tokens.TEXT_SECONDARY};
        --background-light: {tokens.BACKGROUND_LIGHT};
        --border-default: {tokens.BORDER_DEFAULT};
        --success-color: {tokens.SUCCESS};
        --warning-color: {tokens.WARNING};
        --error-color: {tokens.ERROR};
        --font-family: {tokens.FONT_FAMILY_PRIMARY};
    }}
    
    /* Global styles */
    .main {{
        font-family: var(--font-family);
        background-color: var(--background-light);
    }}
    
    /* Title styling */
    h1 {{
        color: var(--primary-color) !important;
        font-family: var(--font-family) !important;
        font-weight: 700 !important;
        font-size: {tokens.FONT_SIZE_XXXL} !important;
        margin-bottom: {tokens.SPACE_LG} !important;
        border-bottom: 3px solid var(--primary-color);
        padding-bottom: {tokens.SPACE_SM};
    }}
    
    /* Subheader styling */
    h2, h3 {{
        color: var(--text-primary) !important;
        font-family: var(--font-family) !important;
        font-weight: 600 !important;
    }}
    
    /* File uploader styling */
    .stFileUploader > div {{
        border: 2px dashed var(--primary-light) !important;
        border-radius: {tokens.RADIUS_LG} !important;
        background-color: var(--primary-lightest) !important;
        padding: {tokens.SPACE_LG} !important;
    }}
    
    .stFileUploader label {{
        color: var(--primary-color) !important;
        font-weight: 600 !important;
    }}
    
    /* Button styling */
    .stButton > button {{
        background-color: var(--primary-color) !important;
        color: white !important;
        border: none !important;
        border-radius: {tokens.RADIUS_MD} !important;
        font-family: var(--font-family) !important;
        font-weight: 500 !important;
        transition: all 0.2s ease !important;
        box-shadow: {tokens.SHADOW_SM} !important;
    }}
    
    .stButton > button:hover {{
        background-color: var(--primary-light) !important;
        box-shadow: {tokens.SHADOW_MD} !important;
        transform: translateY(-1px) !important;
    }}
    
    /* Download button styling */
    .stDownloadButton > button {{
        background-color: var(--secondary-color) !important;
        color: white !important;
        border: none !important;
        border-radius: {tokens.RADIUS_MD} !important;
        font-family: var(--font-family) !important;
        font-weight: 500 !important;
        transition: all 0.2s ease !important;
    }}
    
    .stDownloadButton > button:hover {{
        background-color: var(--secondary-light) !important;
        transform: translateY(-1px) !important;
    }}
    
    /* Metric styling */
    .metric-container {{
        background-color: white !important;
        padding: {tokens.SPACE_LG} !important;
        border-radius: {tokens.RADIUS_LG} !important;
        border: 1px solid var(--border-default) !important;
        box-shadow: {tokens.SHADOW_SM} !important;
    }}
    
    [data-testid="metric-container"] {{
        background-color: white !important;
        border: 1px solid var(--border-default) !important;
        border-radius: {tokens.RADIUS_LG} !important;
        box-shadow: {tokens.SHADOW_SM} !important;
        padding: {tokens.SPACE_MD} !important;
    }}
    
    [data-testid="metric-container"] > div {{
        color: var(--text-primary) !important;
    }}
    
    [data-testid="metric-container"] [data-testid="metric-value"] {{
        color: var(--primary-color) !important;
        font-weight: 700 !important;
        font-size: {tokens.FONT_SIZE_XL} !important;
    }}
    
    /* Selectbox styling */
    .stSelectbox > div > div {{
        border: 1px solid var(--border-default) !important;
        border-radius: {tokens.RADIUS_MD} !important;
        background-color: white !important;
    }}
    
    .stSelectbox label {{
        color: var(--text-primary) !important;
        font-weight: 600 !important;
        font-family: var(--font-family) !important;
    }}
    
    /* Success/Warning/Error message styling */
    .stSuccess {{
        background-color: var(--success-light) !important;
        border-left: 4px solid var(--success-color) !important;
        border-radius: {tokens.RADIUS_MD} !important;
    }}
    
    .stWarning {{
        background-color: var(--warning-light) !important;
        border-left: 4px solid var(--warning-color) !important;
        border-radius: {tokens.RADIUS_MD} !important;
    }}
    
    .stError {{
        background-color: var(--error-light) !important;
        border-left: 4px solid var(--error-color) !important;
        border-radius: {tokens.RADIUS_MD} !important;
    }}
    
    /* Dataframe styling */
    .stDataFrame {{
        border: 1px solid var(--border-default) !important;
        border-radius: {tokens.RADIUS_MD} !important;
        overflow: hidden !important;
    }}
    
    /* Spinner styling */
    .stSpinner > div {{
        border-top-color: var(--primary-color) !important;
    }}
    
    /* Info message styling */
    .stInfo {{
        background-color: var(--info-light) !important;
        border-left: 4px solid var(--info-color) !important;
        border-radius: {tokens.RADIUS_MD} !important;
    }}
    
    /* Column styling */
    .css-1r6slb0 {{
        background-color: white !important;
        padding: {tokens.SPACE_MD} !important;
        border-radius: {tokens.RADIUS_MD} !important;
        border: 1px solid var(--border-default) !important;
        margin: {tokens.SPACE_SM} !important;
    }}
    
    /* Sidebar styling (if used) */
    .css-1d391kg {{
        background-color: var(--primary-lightest) !important;
    }}
    
    /* Text styling */
    p, div, span {{
        color: var(--text-primary) !important;
        font-family: var(--font-family) !important;
    }}
    
    /* Divider styling */
    hr {{
        border-color: var(--border-default) !important;
        margin: {tokens.SPACE_LG} 0 !important;
    }}
    </style>
    """