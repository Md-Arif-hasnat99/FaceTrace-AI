import streamlit as st
from pages.helper.styles import inject_custom_css, create_header, create_footer

st.set_page_config(
    page_title="FaceTrace AI - Help",
    page_icon=None,
    layout="wide"
)

inject_custom_css()

# Sidebar
with st.sidebar:
    st.markdown("## FaceTrace AI")
    st.markdown("---")
    st.markdown("### Help Center")
    st.markdown("Find answers to common questions and learn how to use the system.")

create_header("Help Center", "Everything you need to know about FaceTrace AI")

# About Section
st.markdown("""
<div class="card">
    <h3>About FaceTrace AI</h3>
    <p>
        <strong>FaceTrace AI</strong> is an AI-powered application designed to help locate missing persons using 
        advanced facial recognition technology. It leverages <strong>MediaPipe Face Mesh</strong> for accurate 
        facial landmark detection and matching, extracting 468 unique facial landmarks for precise identification.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# How to Use Section
st.markdown("### How to Use")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <h4>1. Register a New Case</h4>
        <ol>
            <li>Navigate to <strong>"Register New Case"</strong> from the sidebar</li>
            <li>Upload a clear photo (JPG, JPEG, or PNG)</li>
            <li>Wait for facial feature extraction</li>
            <li>Fill in all required details</li>
            <li>Click <strong>"Save"</strong> to register</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <h4>2. View All Cases</h4>
        <ul>
            <li>Go to <strong>"All Cases"</strong></li>
            <li>Filter by status: All, Found, Not Found, or Public</li>
            <li>View matched cases and their details</li>
            <li>Track case progress over time</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h4>3. Match Cases</h4>
        <ul>
            <li>Navigate to <strong>"Match Cases"</strong></li>
            <li>Click <strong>"Run Matching"</strong> to start AI analysis</li>
            <li>The system compares facial landmarks</li>
            <li>Potential matches are displayed with details</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <h4>4. Public Submissions</h4>
        <ul>
            <li>Use the mobile app for public sightings</li>
            <li>Anyone can submit a photo anonymously</li>
            <li>Submissions are matched against registered cases</li>
            <li>Helps crowdsource the search effort</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Login Info
st.markdown("### Login Credentials")

st.markdown("""
<div class="info-box">
    <table style="width: 100%;">
        <tr>
            <th style="text-align: left; padding: 0.5rem;">Username</th>
            <th style="text-align: left; padding: 0.5rem;">Password</th>
            <th style="text-align: left; padding: 0.5rem;">Role</th>
        </tr>
        <tr>
            <td style="padding: 0.5rem;"><code>arif</code></td>
            <td style="padding: 0.5rem;"><code>abc</code></td>
            <td style="padding: 0.5rem;">Admin</td>
        </tr>
    </table>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Tips Section
st.markdown("### Tips for Best Results")

tips_col1, tips_col2, tips_col3 = st.columns(3)

with tips_col1:
    st.markdown("""
    <div class="card" style="text-align: center;">
        <h4>Clear Photos</h4>
        <p style="color: #A0AEC0;">Use well-lit photos with the face clearly visible</p>
    </div>
    """, unsafe_allow_html=True)

with tips_col2:
    st.markdown("""
    <div class="card" style="text-align: center;">
        <h4>Front-Facing</h4>
        <p style="color: #A0AEC0;">Front-facing photos work best for landmark detection</p>
    </div>
    """, unsafe_allow_html=True)

with tips_col3:
    st.markdown("""
    <div class="card" style="text-align: center;">
        <h4>High Resolution</h4>
        <p style="color: #A0AEC0;">Higher resolution images provide better accuracy</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Technical Info
st.markdown("### Technical Information")

tech_col1, tech_col2 = st.columns(2)

with tech_col1:
    st.markdown("""
    <div class="card">
        <h4>AI Technology</h4>
        <ul>
            <li><strong>Face Mesh:</strong> MediaPipe Face Mesh</li>
            <li><strong>Landmarks:</strong> 468 facial points</li>
            <li><strong>Matching:</strong> Euclidean distance algorithm</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with tech_col2:
    st.markdown("""
    <div class="card">
        <h4>Tech Stack</h4>
        <ul>
            <li><strong>Frontend:</strong> Streamlit</li>
            <li><strong>Database:</strong> SQLite</li>
            <li><strong>Language:</strong> Python 3.10+</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Contact Section
st.markdown("""
<div class="card" style="text-align: center;">
    <h3>Need More Help?</h3>
    <p style="color: #A0AEC0;">For technical support or feature requests, please contact the administrator.</p>
    <p><strong>Developer:</strong> Md Arif Hasnat</p>
</div>
""", unsafe_allow_html=True)

create_footer()
