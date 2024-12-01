import streamlit as st
from PIL import Image

# Set page config
st.set_page_config(
    page_title="Solar Panels Fault Detection",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject custom CSS
st.markdown("""
    <style>
        /* Background for the app */
        body {
            background-color: #F9F6EE;
            font-family: 'Arial', sans-serif;
        }

        /* Header and title styles */
        h1, h2, h3, h4 {
            color: #F9F6EE;
            font-weight: bold;
        }

        /* File upload styling */
        .stFileUploader {
            background-color: default;
            border-radius: 10px;
            border: 1px solid #d1d5db;
            padding: 15px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }

        /* Buttons styling */
        .stButton button {
            background-color: #2563eb;
            color: #ffffff;
            border-radius: 8px;
            padding: 10px 20px;
            border: none;
            font-size: 16px;
            font-weight: bold;
        }
        .stButton button:hover {
            background-color: #1d4ed8;
            color: white;
        }

        /* Sidebar styling */
        [data-testid="stSidebar"] {
            background-color: #111827;
            color: white;
        }
        [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2 {
            color: white;
        }
        [data-testid="stSidebar"] p {
            color: #d1d5db;
        }

        /* Center alignment for content */
        .centered {
            text-align: center;
        }

        /* Image container */
        .image-container {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }

        /* Box shadow for images */
        img {
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        }
    </style>
""", unsafe_allow_html=True)

# Main content
st.title("Solar Panels Fault Detection")
st.header("Upload an Image for Fault Detection")
st.write("This application detects faults in solar panels using state-of-the-art object detection techniques.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Show image and simulate detection
if uploaded_file is not None:
    # Display uploaded image
    st.image(Image.open(uploaded_file), caption="Uploaded Image", use_column_width=True)

    # Simulate detection results
    st.subheader("Detection Results:")
    st.write("""
        - Fault Type: **Crack**
        - Confidence: **95%**
        - Panel ID: **12345ABC**
    """)

# Sidebar content
# st.sidebar.title("About")
# st.sidebar.write("This tool uses YOLOv8 for detecting faults in solar panels.")
# st.sidebar.write("Upload an image to see the results.")