import streamlit as st

from pages.helper import db_queries, match_algo, train_model
from pages.helper.styles import inject_custom_css, create_header, create_footer

st.set_page_config(
    page_title="FaceTrace AI - Match Cases",
    page_icon=None,
    layout="wide"
)

inject_custom_css()

# Sidebar
with st.sidebar:
    st.markdown("## FaceTrace AI")
    st.markdown("---")
    st.markdown("### Match Cases")
    st.markdown("Run AI matching algorithm to find potential matches between registered cases and public submissions.")


def case_viewer(registered_case_id, public_case_id):
    """Display matched case details"""
    try:
        case_details = db_queries.get_registered_case_detail(registered_case_id)[0]
        
        st.markdown(f"""
        <div class="case-card" style="border-left-color: #48BB78;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                <h4 style="margin: 0; color: #48BB78;">Match Found!</h4>
                <span class="status-found">Matched</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        data_col, image_col = st.columns([2, 1])
        
        with data_col:
            st.markdown("**Case Details:**")
            for text, value in zip(
                ["Name", "Mobile", "Age", "Last Seen", "Birth marks"], case_details
            ):
                st.markdown(f"**{text}:** {value}")

        with image_col:
            try:
                st.image(
                    "./resources/" + registered_case_id + ".jpg",
                    width=150,
                    use_container_width=False,
                )
            except Exception as img_err:
                st.warning(f"Could not load image")

        # Update status
        db_queries.update_found_status(registered_case_id, public_case_id)
        st.markdown('<div class="success-box">Status updated! This case will now appear in Found cases.</div>', unsafe_allow_html=True)

    except Exception as e:
        import traceback
        traceback.print_exc()
        st.markdown(f'<div class="error-box">Error: {str(e)}</div>', unsafe_allow_html=True)


# Main content
if "login_status" not in st.session_state or not st.session_state["login_status"]:
    create_header("Access Denied", "Please login to access this page")
    st.markdown('<div class="error-box">You need to login to access this page.</div>', unsafe_allow_html=True)

else:
    user = st.session_state.user
    
    create_header("Match Cases", "AI-powered facial recognition matching")
    
    # Info box
    st.markdown("""
    <div class="info-box">
        <strong>How it works:</strong><br>
        The matching algorithm compares facial landmarks from registered missing person cases 
        against public submissions to identify potential matches. Click "Run Matching" to start the process.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Action buttons
    col1, col2, col3 = st.columns([1, 1, 2])
    
    with col1:
        refresh_bt = st.button("Run Matching", use_container_width=True, type="primary")
    
    with col2:
        st.button("Reset", use_container_width=True)
    
    st.markdown("---")
    
    # Results section
    st.markdown("### Matching Results")
    
    if refresh_bt:
        progress_bar = st.progress(0, text="Initializing...")
        
        with st.spinner(""):
            progress_bar.progress(20, text="Fetching data...")
            result = train_model.train(user)
            
            progress_bar.progress(60, text="Training model...")
            matched_ids = match_algo.match()
            
            progress_bar.progress(100, text="Complete!")
            progress_bar.empty()

            if matched_ids["status"]:
                if not matched_ids["result"]:
                    st.markdown("""
                    <div class="card" style="text-align: center; padding: 2rem;">
                        <h3>No Matches Found</h3>
                        <p style="color: #A0AEC0;">The AI couldn't find any matches between registered cases and public submissions.</p>
                        <p style="color: #A0AEC0;">Try again later when more submissions are available.</p>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    match_count = len(matched_ids["result"])
                    st.markdown(f'<div class="success-box">Found {match_count} potential match(es)!</div>', unsafe_allow_html=True)
                    
                    for matched_id, submitted_case_id in matched_ids["result"].items():
                        case_viewer(matched_id, submitted_case_id[0])
                        st.markdown("---")
            else:
                st.markdown("""
                <div class="card" style="text-align: center; padding: 2rem;">
                    <h3>No Data Available</h3>
                    <p style="color: #A0AEC0;">No cases available for matching. Please register cases first.</p>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="card" style="text-align: center; padding: 3rem;">
            <h3>Ready to Match</h3>
            <p style="color: #A0AEC0;">Click the "Run Matching" button above to start the AI matching process.</p>
            <p style="color: #718096;">The algorithm will compare all registered cases against public submissions.</p>
        </div>
        """, unsafe_allow_html=True)
    
    create_footer()
