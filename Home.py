import yaml
import streamlit as st
from yaml import SafeLoader
import streamlit_authenticator as stauth

from pages.helper import db_queries
from pages.helper.styles import inject_custom_css, create_header, create_stat_card, create_footer

# Page Configuration
st.set_page_config(
    page_title="FaceTrace AI",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject Custom CSS
inject_custom_css()

# Initialize session state
if "login_status" not in st.session_state:
    st.session_state["login_status"] = False

# Load configuration
try:
    with open("login_config.yml") as file:
        config = yaml.load(file, Loader=SafeLoader)
except FileNotFoundError:
    st.error("Configuration file 'login_config.yml' not found")
    st.stop()

# Initialize authenticator
authenticator = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
)

# Sidebar branding
with st.sidebar:
    st.markdown("## FaceTrace AI")
    st.markdown("---")

# Check authentication status
if not st.session_state.get("authentication_status"):
    # Show login page
    create_header("FaceTrace AI", "AI-Powered Missing Person Identification System")
    
    st.markdown("### Login to Continue")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        authenticator.login(location="main")
    
    if st.session_state.get("authentication_status") == False:
        st.markdown('<div class="error-box">Username/password is incorrect</div>', unsafe_allow_html=True)
    elif st.session_state.get("authentication_status") == None:
        st.markdown('<div class="info-box">Please enter your credentials to access the system</div>', unsafe_allow_html=True)
        
        # Features showcase
        st.markdown("---")
        st.markdown("### Key Features")
        
        feat_col1, feat_col2, feat_col3 = st.columns(3)
        
        with feat_col1:
            st.markdown("""
            <div class="card">
                <h3>Case Registration</h3>
                <p>Register missing person cases with photo uploads and automatic facial feature extraction</p>
            </div>
            """, unsafe_allow_html=True)
        
        with feat_col2:
            st.markdown("""
            <div class="card">
                <h3>AI Matching</h3>
                <p>Advanced facial recognition using MediaPipe to match and identify potential matches</p>
            </div>
            """, unsafe_allow_html=True)
        
        with feat_col3:
            st.markdown("""
            <div class="card">
                <h3>Public Submissions</h3>
                <p>Allow public to submit sightings through mobile-friendly interface</p>
            </div>
            """, unsafe_allow_html=True)
    
    create_footer()

else:
    # User is logged in
    authenticator.logout("Logout", "sidebar")
    
    st.session_state["login_status"] = True
    user_info = config["credentials"]["usernames"][st.session_state["username"]]
    st.session_state["user"] = user_info["name"]
    
    # Welcome header
    create_header("FaceTrace AI", "AI-Powered Missing Person Identification System")
    
    # User info section
    st.markdown(f"""
    <div class="card">
        <div class="welcome-text">Welcome, {user_info["name"]}</div>
        <p style="color: #A0AEC0; margin-bottom: 0.5rem;">{user_info["area"]}, {user_info["city"]}</p>
        <span class="role-badge">{user_info["role"]}</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Dashboard Stats
    st.markdown("### Dashboard Overview")
    
    found_cases = db_queries.get_registered_cases_count(user_info["name"], "F")
    non_found_cases = db_queries.get_registered_cases_count(user_info["name"], "NF")
    
    stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)
    
    with stat_col1:
        create_stat_card(len(found_cases), "Found Cases")
    
    with stat_col2:
        create_stat_card(len(non_found_cases), "Active Cases")
    
    with stat_col3:
        create_stat_card(len(found_cases) + len(non_found_cases), "Total Cases")
    
    with stat_col4:
        if len(found_cases) + len(non_found_cases) > 0:
            success_rate = round((len(found_cases) / (len(found_cases) + len(non_found_cases))) * 100)
        else:
            success_rate = 0
        create_stat_card(f"{success_rate}%", "Success Rate")
    
    st.markdown("---")
    
    # Quick Actions
    st.markdown("### Quick Actions")
    
    action_col1, action_col2, action_col3 = st.columns(3)
    
    with action_col1:
        st.markdown("""
        <div class="card">
            <h4>Register New Case</h4>
            <p style="color: #A0AEC0;">Add a new missing person case with photo and details</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Register Case", key="btn_register", use_container_width=True):
            st.switch_page("pages/1_Register New Case.py")
    
    with action_col2:
        st.markdown("""
        <div class="card">
            <h4>View All Cases</h4>
            <p style="color: #A0AEC0;">Browse and manage all registered cases</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("View Cases", key="btn_view", use_container_width=True):
            st.switch_page("pages/2_All Cases.py")
    
    with action_col3:
        st.markdown("""
        <div class="card">
            <h4>Match Cases</h4>
            <p style="color: #A0AEC0;">Run AI matching to find potential matches</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Run Matching", key="btn_match", use_container_width=True):
            st.switch_page("pages/3_Match Cases.py")
    
    create_footer()
