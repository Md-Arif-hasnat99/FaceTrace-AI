import uuid
import numpy as np
import streamlit as st
import json

from pages.helper.data_models import RegisteredCases
from pages.helper import db_queries
from pages.helper.utils import image_obj_to_numpy, extract_face_mesh_landmarks
from pages.helper.styles import inject_custom_css, create_header, create_footer

st.set_page_config(
    page_title="FaceTrace AI - Register Case",
    page_icon=None,
    layout="wide"
)

inject_custom_css()

# Sidebar
with st.sidebar:
    st.markdown("## FaceTrace AI")
    st.markdown("---")
    st.markdown("### Register New Case")
    st.markdown("Upload a photo and fill in the details to register a new missing person case.")

if "login_status" not in st.session_state or not st.session_state["login_status"]:
    create_header("Access Denied", "Please login to access this page")
    st.markdown('<div class="error-box">You need to login to access this page. Please go to the Home page to login.</div>', unsafe_allow_html=True)

else:
    user = st.session_state.user
    
    create_header("Register New Case", "Add a new missing person case to the system")
    
    # Instructions
    st.markdown("""
    <div class="info-box">
        <strong>Instructions:</strong><br>
        1. Upload a clear photo of the missing person<br>
        2. Wait for facial feature extraction<br>
        3. Fill in all required details<br>
        4. Click Save to register the case
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")

    image_col, form_col = st.columns([1, 2])
    image_obj = None
    save_flag = 0
    unique_id = None
    face_mesh = None

    with image_col:
        st.markdown("### Upload Photo")
        
        image_obj = st.file_uploader(
            "Choose an image file",
            type=["jpg", "jpeg", "png"],
            key="new_case",
            help="Upload a clear, front-facing photo for best results"
        )

        if image_obj:
            unique_id = str(uuid.uuid4())
            uploaded_file_path = "./resources/" + str(unique_id) + ".jpg"
            with open(uploaded_file_path, "wb") as output_temporary_file:
                output_temporary_file.write(image_obj.read())

            with st.spinner("Extracting facial features..."):
                st.image(image_obj, caption="Uploaded Photo", use_container_width=True)
                image_numpy = image_obj_to_numpy(image_obj)
                face_mesh = extract_face_mesh_landmarks(image_numpy)
                
            if face_mesh:
                st.markdown('<div class="success-box">Facial features extracted successfully!</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="warning-box">Could not detect face. Try a clearer photo.</div>', unsafe_allow_html=True)

    if image_obj and unique_id:
        with form_col:
            st.markdown("### Case Details")
            
            with st.form(key="new_case_form"):
                # Personal Information
                st.markdown("#### Personal Information")
                
                name_col, father_col = st.columns(2)
                with name_col:
                    name = st.text_input("Full Name *", placeholder="Enter full name")
                with father_col:
                    fathers_name = st.text_input("Father's Name *", placeholder="Enter father's name")
                
                age_col, id_col = st.columns(2)
                with age_col:
                    age = st.number_input("Age *", min_value=1, max_value=100, value=10, step=1)
                with id_col:
                    adhaar_card = st.text_input("Aadhaar Card", placeholder="12-digit Aadhaar number")
                
                # Location Details
                st.markdown("#### Location Details")
                
                address = st.text_input("Address *", placeholder="Full address")
                last_seen = st.text_input("Last Seen Location *", placeholder="Where was the person last seen?")
                
                # Physical Description
                st.markdown("#### Identifying Features")
                birthmarks = st.text_input("Birth Marks / Identifying Features", placeholder="Any birthmarks or unique features")
                description = st.text_area("Additional Description", placeholder="Any other details that might help identify the person")
                
                # Complainant Details
                st.markdown("#### Complainant Information")
                
                comp_col1, comp_col2 = st.columns(2)
                with comp_col1:
                    complainant_name = st.text_input("Complainant Name *", placeholder="Your name")
                with comp_col2:
                    complainant_phone = st.text_input("Contact Number *", placeholder="Phone number")
                
                mobile_number = complainant_phone  # Using complainant phone as mobile
                
                st.markdown("---")
                
                submit_bt = st.form_submit_button("Save Case", use_container_width=True)

                if submit_bt:
                    if not name or not fathers_name or not address or not last_seen or not complainant_name or not complainant_phone:
                        st.error("Please fill in all required fields marked with *")
                    else:
                        new_case_details = RegisteredCases(
                            id=unique_id,
                            submitted_by=user,
                            name=name,
                            fathers_name=fathers_name,
                            age=age,
                            complainant_mobile=mobile_number,
                            complainant_name=complainant_name,
                            face_mesh=json.dumps(face_mesh),
                            adhaar_card=adhaar_card,
                            birth_marks=birthmarks,
                            address=address,
                            last_seen=last_seen,
                            status="NF",
                            matched_with="",
                        )
                        
                        db_queries.register_new_case(new_case_details)
                        save_flag = 1

            if save_flag:
                st.balloons()
                st.markdown('<div class="success-box">Case registered successfully! The case is now active and will be included in matching.</div>', unsafe_allow_html=True)
    
    else:
        with form_col:
            st.markdown("""
            <div class="card" style="text-align: center; padding: 3rem;">
                <h3>Upload a Photo First</h3>
                <p style="color: #A0AEC0;">Please upload a photo of the missing person to continue with registration.</p>
            </div>
            """, unsafe_allow_html=True)
    
    create_footer()
