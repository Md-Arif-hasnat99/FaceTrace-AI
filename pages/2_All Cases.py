import streamlit as st
from pages.helper import db_queries
from pages.helper.styles import inject_custom_css, create_header, create_status_badge, create_footer

st.set_page_config(
    page_title="FaceTrace AI - All Cases",
    page_icon=None,
    layout="wide"
)

inject_custom_css()

# Sidebar
with st.sidebar:
    st.markdown("## FaceTrace AI")
    st.markdown("---")
    st.markdown("### All Cases")
    st.markdown("View and manage all registered cases in the system.")


def case_viewer(case):
    """Display a single case in a card format"""
    case = list(case)
    case_id = case.pop(0)
    matched_with_id = case.pop(-1)
    matched_with_details = None

    try:
        matched_with_id = matched_with_id.replace("{", "").replace("}", "")
    except:
        matched_with_id = None

    if matched_with_id:
        matched_with_details = db_queries.get_public_case_detail(matched_with_id)

    # Get status for badge
    status_value = case[2]  # Status is at index 2 after popping
    status_badge = create_status_badge(status_value)
    
    st.markdown(f"""
    <div class="case-card">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
            <h4 style="margin: 0; color: #63B3ED;">Case #{case_id[:8]}...</h4>
            {status_badge}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    data_col, image_col, matched_with_col = st.columns([2, 1, 2])
    
    with data_col:
        for text, value in zip(["Name", "Age", "Status", "Last Seen", "Phone"], case):
            if value == "F":
                value = "Found"
            elif value == "NF":
                value = "Not Found"
            st.markdown(f"**{text}:** {value}")

    with image_col:
        try:
            st.image(
                "./resources/" + str(case_id) + ".jpg",
                width=150,
                use_container_width=False,
            )
        except:
            st.warning("Image not found")
    
    with matched_with_col:
        if matched_with_details:
            st.markdown("**Match Details:**")
            st.markdown(f"Location: {matched_with_details[0][0]}")
            st.markdown(f"Submitted By: {matched_with_details[0][1]}")
            st.markdown(f"Mobile: {matched_with_details[0][2]}")
            st.markdown(f"Birth Marks: {matched_with_details[0][3]}")
        else:
            st.markdown("*No match found yet*")
    
    st.markdown("---")


def public_case_viewer(case: list) -> None:
    """Display a public submission case"""
    case = list(case)
    case_id = str(case.pop(0))
    
    status_value = case[0]
    status_badge = create_status_badge(status_value)
    
    st.markdown(f"""
    <div class="case-card">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
            <h4 style="margin: 0; color: #63B3ED;">Public Submission #{case_id[:8]}...</h4>
            {status_badge}
        </div>
    </div>
    """, unsafe_allow_html=True)

    data_col, image_col, _ = st.columns([2, 1, 2])
    
    with data_col:
        for text, value in zip(
            ["Status", "Location", "Mobile", "Birth Marks", "Submitted on", "Submitted by"],
            case,
        ):
            if text == "Status":
                value = "Found" if value == "F" else "Not Found"
            st.markdown(f"**{text}:** {value}")

    with image_col:
        try:
            st.image(
                "./resources/" + case_id + ".jpg",
                width=150,
                use_container_width=False,
            )
        except Exception as e:
            st.warning("Image not found")

    st.markdown("---")


# Main content
if "login_status" not in st.session_state or not st.session_state["login_status"]:
    create_header("Access Denied", "Please login to access this page")
    st.markdown('<div class="error-box">You need to login to access this page.</div>', unsafe_allow_html=True)

else:
    user = st.session_state.user
    
    create_header("All Cases", "View and manage registered cases")
    
    # Filters
    st.markdown("### Filter Cases")
    
    filter_col1, filter_col2, filter_col3 = st.columns([2, 2, 1])
    
    with filter_col1:
        status = st.selectbox(
            "Status Filter",
            options=["All", "Not Found", "Found", "Public Cases"],
            help="Filter cases by their current status"
        )
    
    with filter_col2:
        date = st.date_input("Date Filter", help="Filter by submission date")
    
    with filter_col3:
        st.markdown("<br>", unsafe_allow_html=True)
        refresh = st.button("Refresh", use_container_width=True)
    
    st.markdown("---")
    
    # Display cases
    if status == "Public Cases":
        st.markdown("### Public Submissions")
        cases_data = db_queries.fetch_public_cases(False, status)
        
        if cases_data:
            st.markdown(f'<div class="info-box">Showing {len(cases_data)} public submission(s)</div>', unsafe_allow_html=True)
            for case in cases_data:
                public_case_viewer(case)
        else:
            st.markdown("""
            <div class="card" style="text-align: center; padding: 2rem;">
                <h3>No Public Submissions</h3>
                <p style="color: #A0AEC0;">No public submissions found.</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown(f"### Registered Cases - {status}")
        cases_data = db_queries.fetch_registered_cases(user, status)
        
        if cases_data:
            st.markdown(f'<div class="info-box">Showing {len(cases_data)} case(s)</div>', unsafe_allow_html=True)
            for case in cases_data:
                case_viewer(case)
        else:
            st.markdown("""
            <div class="card" style="text-align: center; padding: 2rem;">
                <h3>No Cases Found</h3>
                <p style="color: #A0AEC0;">No cases match your current filter. Try changing the filter or register a new case.</p>
            </div>
            """, unsafe_allow_html=True)
    
    create_footer()
