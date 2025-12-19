"""
Custom CSS styles for FaceTrace AI application
Minimal blue-gray theme
"""

CUSTOM_CSS = """
<style>
    /* Main App Styling */
    .main {
        padding: 1rem 2rem;
    }
    
    /* Header Styling */
    .main-header {
        background: linear-gradient(135deg, #4A5568 0%, #2D3748 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }
    
    .main-header h1 {
        color: white !important;
        font-size: 2.2rem !important;
        margin-bottom: 0.5rem !important;
        font-weight: 600 !important;
    }
    
    .main-header p {
        color: rgba(255,255,255,0.8) !important;
        font-size: 1rem !important;
    }
    
    /* Card Styling */
    .card {
        background: #1A1D24;
        border-radius: 8px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid #2D3748;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    
    .card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
    }
    
    /* Stat Card */
    .stat-card {
        background: #1A1D24;
        border-radius: 8px;
        padding: 1.5rem;
        text-align: center;
        border: 1px solid #2D3748;
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 600;
        color: #63B3ED;
    }
    
    .stat-label {
        color: #A0AEC0;
        font-size: 0.9rem;
        margin-top: 0.5rem;
    }
    
    /* Success/Warning/Error Styling */
    .success-box {
        background: #276749;
        padding: 1rem 1.5rem;
        border-radius: 6px;
        color: white;
        margin: 1rem 0;
    }
    
    .warning-box {
        background: #C05621;
        padding: 1rem 1.5rem;
        border-radius: 6px;
        color: white;
        margin: 1rem 0;
    }
    
    .error-box {
        background: #C53030;
        padding: 1rem 1.5rem;
        border-radius: 6px;
        color: white;
        margin: 1rem 0;
    }
    
    /* Button Styling */
    .stButton > button {
        background: #4A5568;
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 6px;
        font-weight: 500;
        transition: all 0.2s ease;
    }
    
    .stButton > button:hover {
        background: #2D3748;
        transform: translateY(-1px);
    }
    
    /* File Uploader */
    .stFileUploader {
        border: 1px dashed #4A5568;
        border-radius: 8px;
        padding: 1rem;
        transition: border-color 0.2s ease;
    }
    
    .stFileUploader:hover {
        border-color: #63B3ED;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: #0E1117;
        border-right: 1px solid #2D3748;
    }
    
    [data-testid="stSidebar"] .stMarkdown h1 {
        color: #E2E8F0 !important;
    }
    
    /* Input Fields */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div {
        background-color: #1A1D24;
        border: 1px solid #2D3748;
        border-radius: 6px;
        color: #FAFAFA;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: #63B3ED;
        box-shadow: 0 0 0 1px rgba(99, 179, 237, 0.3);
    }
    
    /* Metric Styling */
    [data-testid="stMetricValue"] {
        font-size: 2rem !important;
        color: #63B3ED !important;
    }
    
    [data-testid="stMetricLabel"] {
        color: #A0AEC0 !important;
    }
    
    /* Divider */
    hr {
        border: none;
        height: 1px;
        background: #2D3748;
        margin: 2rem 0;
    }
    
    /* Image Container */
    .image-container {
        border-radius: 8px;
        overflow: hidden;
        border: 1px solid #2D3748;
    }
    
    /* Case Card */
    .case-card {
        background: #1A1D24;
        border-radius: 8px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 3px solid #63B3ED;
        transition: all 0.2s ease;
    }
    
    .case-card:hover {
        transform: translateX(3px);
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
    }
    
    /* Status Badges */
    .status-found {
        background: #276749;
        padding: 0.25rem 0.75rem;
        border-radius: 4px;
        color: white;
        font-size: 0.8rem;
        font-weight: 500;
        display: inline-block;
    }
    
    .status-not-found {
        background: #C53030;
        padding: 0.25rem 0.75rem;
        border-radius: 4px;
        color: white;
        font-size: 0.8rem;
        font-weight: 500;
        display: inline-block;
    }
    
    /* Welcome Text */
    .welcome-text {
        font-size: 1.75rem;
        font-weight: 600;
        color: #E2E8F0;
        margin-bottom: 0.5rem;
    }
    
    .role-badge {
        background: #4A5568;
        padding: 0.25rem 0.75rem;
        border-radius: 4px;
        color: white;
        font-size: 0.8rem;
        font-weight: 500;
        display: inline-block;
    }
    
    /* Info Box */
    .info-box {
        background: rgba(99, 179, 237, 0.1);
        border: 1px solid rgba(99, 179, 237, 0.3);
        border-radius: 6px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem;
        color: #718096;
        border-top: 1px solid #2D3748;
        margin-top: 3rem;
    }
    
    /* Animation */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .animate-fade-in {
        animation: fadeIn 0.3s ease-out forwards;
    }
    
    /* Spinner */
    .stSpinner > div {
        border-top-color: #63B3ED !important;
    }
</style>
"""


def inject_custom_css():
    """Inject custom CSS into the Streamlit app"""
    import streamlit as st
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


def create_header(title: str, subtitle: str = ""):
    """Create a styled header"""
    import streamlit as st
    header_html = f"""
    <div class="main-header">
        <h1>{title}</h1>
        <p>{subtitle}</p>
    </div>
    """
    st.markdown(header_html, unsafe_allow_html=True)


def create_stat_card(number: int, label: str):
    """Create a styled stat card"""
    import streamlit as st
    card_html = f"""
    <div class="stat-card">
        <div class="stat-number">{number}</div>
        <div class="stat-label">{label}</div>
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)


def create_status_badge(status: str):
    """Create a styled status badge"""
    if status == "F" or status.lower() == "found":
        return '<span class="status-found">Found</span>'
    else:
        return '<span class="status-not-found">Not Found</span>'


def create_info_box(content: str):
    """Create an info box"""
    import streamlit as st
    st.markdown(f'<div class="info-box">{content}</div>', unsafe_allow_html=True)


def create_footer():
    """Create a styled footer"""
    import streamlit as st
    footer_html = """
    <div class="footer">
        <p><strong>FaceTrace AI</strong> - AI-Powered Missing Person Identification</p>
        <p>Developed by Md Arif Hasnat</p>
    </div>
    """
    st.markdown(footer_html, unsafe_allow_html=True)
