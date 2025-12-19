import uuid
import json
import streamlit as st
import numpy as np

from pages.helper import db_queries
from pages.helper.data_models import PublicSubmissions
from pages.helper.utils import image_obj_to_numpy, extract_face_mesh_landmarks
from pages.helper.styles import inject_custom_css, create_header, create_footer

# Page Configuration
st.set_page_config(
    page_title="FaceTrace AI - Report Sighting",
    page_icon=None,
    layout="centered",
    initial_sidebar_state="collapsed"
)

inject_custom_css()

# Header
create_header("Report a Sighting", "Help reunite families by submitting sighting reports")

# Instructions
st.markdown("""
<div class="info-box">
    <strong>How to Submit:</strong><br>
    1. Upload a clear photo of the person you spotted<br>
    2. Fill in your contact details and location information<br>
    3. Click Submit - Your report will be matched against missing persons
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
        "Choose an image",
        type=["jpg", "jpeg", "png"],
        key="user_submission",
        help="Upload a clear photo of the person you spotted"
    )
    
    if image_obj:
        unique_id = str(uuid.uuid4())

        with st.spinner("Processing image..."):
            uploaded_file_path = "./resources/" + str(unique_id) + ".jpg"
            with open(uploaded_file_path, "wb") as output_temporary_file:
                output_temporary_file.write(image_obj.read())

            st.image(image_obj, caption="Uploaded Photo", use_container_width=True)
            image_numpy = image_obj_to_numpy(image_obj)
            face_mesh = extract_face_mesh_landmarks(image_numpy)
        
        if face_mesh:
            st.markdown('<div class="success-box">Face detected successfully!</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="warning-box">Could not detect face clearly. Please try another photo.</div>', unsafe_allow_html=True)

if image_obj and unique_id:
    with form_col:
        st.markdown("### Submission Details")
        
        with st.form(key="new_user_submission"):
            st.markdown("#### Your Information")
            
            name = st.text_input("Your Name *", placeholder="Enter your full name")
            
            contact_col1, contact_col2 = st.columns(2)
            with contact_col1:
                mobile_number = st.text_input("Phone Number *", placeholder="Your contact number")
            with contact_col2:
                email = st.text_input("Email", placeholder="your@email.com")
            
            st.markdown("#### Sighting Details")
            
            address = st.text_input("Location Where Seen *", placeholder="Where did you spot this person?")
            birth_marks = st.text_input("Identifying Features", placeholder="Any notable features you observed")
            
            st.markdown("---")
            
            submit_bt = st.form_submit_button("Submit Report", use_container_width=True)

            if submit_bt:
                if not name or not mobile_number or not address:
                    st.error("Please fill in all required fields marked with *")
                else:
                    public_submission_details = PublicSubmissions(
                        submitted_by=name,
                        location=address,
                        email=email,
                        face_mesh=json.dumps(face_mesh),
                        id=unique_id,
                        mobile=mobile_number,
                        birth_marks=birth_marks,
                        status="NF",
                    )
                    
                    db_queries.new_public_case(public_submission_details)
                    save_flag = 1

        if save_flag == 1:
            st.balloons()
            st.markdown("""
            <div class="success-box">
                <strong>Thank you for your submission!</strong><br>
                Your report has been received and will be compared against our database of missing persons.
                If there's a match, the relevant authorities will be notified.
            </div>
            """, unsafe_allow_html=True)

else:
    with form_col:
        st.markdown("""
        <div class="card" style="text-align: center; padding: 3rem;">
            <h3>Upload a Photo First</h3>
            <p style="color: #A0AEC0;">Please upload a photo of the person you spotted to continue with your submission.</p>
        </div>
        """, unsafe_allow_html=True)

create_footer()
