import streamlit as st
import os
import time

# --- Page Configuration ---
st.set_page_config(page_title="Market Basket Dashboard", layout="wide")

# --- Session State Initialization ---
if "slide_index" not in st.session_state:
    st.session_state.slide_index = 0
if "autoplay" not in st.session_state:
    st.session_state.autoplay = False

# --- Custom Aesthetic Styling ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(120deg, #9bf6ff 0%, #ebedee 100%);
        color: #111111;
        font-family: 'Segoe UI', sans-serif;
    }
    h1, h2, h3, h4 {
        color: #2c3e50;
    }
    .stButton>button {
        background-color: #3498db;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #2980b9;
    }
    .stCheckbox>div>label, .stRadio>div>label, .stSelectbox label {
        font-weight: 600;
    }
    footer {
        margin-top: 50px;
        text-align: center;
        color: #555;
        font-size: 14px;
    }
    .signature {
        font-family: 'Brush Script MT', cursive;
        font-size: 20px;
        animation: glow 2s ease-in-out infinite alternate;
        color: #2c3e50;
        transition: transform 0.3s ease;
    }
    .signature:hover {
        transform: scale(1.05);
        color: #d35400;
    }
    @keyframes glow {
        from { text-shadow: 0 0 5px #ccc; }
        to { text-shadow: 0 0 15px #aaa; }
    }
    .social-btn {
        display: inline-block;
        margin: 0 10px;
        padding: 6px 12px;
        background-color: ;
        color: white;
        border-radius: 5px;
        text-decoration: none;
        font-weight: bold;
    }
    .social-btn:hover {
        background-color:#e2e2e4 ;
    }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown("<h1 style='font-size:36px;'>📊 Market Basket Dashboard</h1>", unsafe_allow_html=True)

# --- Dataset Display ---
with st.expander(" View Sample of Dataset"):
    st.markdown("Here you can show a preview of your dataset.")

# --- Slideshow Settings ---
st.markdown("<h3>🎞️ Image Slideshow Settings</h3>", unsafe_allow_html=True)
st.session_state.autoplay = st.checkbox(" Enable Autoplay Slideshow", value=st.session_state.autoplay)

col1, col2 = st.columns([2, 1])
with col1:
    timer_option = st.selectbox(" Time per Slide (seconds)", [1,2,3,4,5,6,7,8,9,10], index=2)
with col2:
    if st.session_state.autoplay:
        if st.button("▶️ Start Slideshow"):
            st.session_state.run_autoplay = True

# --- Image List ---
image_folder = "images"
image_files = sorted([img for img in os.listdir(image_folder) if img.endswith(("png", "jpg", "jpeg"))])

# --- Chart Display ---
st.markdown("<h3>📈 Top 10 Association Rules</h3>", unsafe_allow_html=True)
chart_image_path = os.path.join(image_folder, "top_10_chart.png")
if os.path.exists(chart_image_path):
    st.image(chart_image_path, caption="Top 10 Frequent Itemsets", use_container_width=True)

# --- Image Slideshow Display ---
st.markdown("<h3>🖼️ Slideshow</h3>", unsafe_allow_html=True)
current_index = st.session_state.slide_index
image_path = os.path.join(image_folder, image_files[current_index])
st.image(image_path, caption=f"Slide {current_index + 1} of {len(image_files)}", use_container_width=True)

col3, col4 = st.columns(2)
with col3:
    if st.button("⬅️ Previous"):
        st.session_state.slide_index = (st.session_state.slide_index - 1) % len(image_files)
        st.rerun()
with col4:
    if st.button("➡️ Next"):
        st.session_state.slide_index = (st.session_state.slide_index + 1) % len(image_files)
        st.rerun()

# --- Autoplay Logic ---
if st.session_state.autoplay and "run_autoplay" in st.session_state and st.session_state.run_autoplay:
    time.sleep(timer_option)
    st.session_state.slide_index = (st.session_state.slide_index + 1) % len(image_files)
    st.rerun()

# --- Footer ---
st.markdown("""
    <hr style="margin-top: 3rem;">
    <footer>
        <div class="signature">Crafted with  by Aryan Singh</div>
        <br>
        📧 <a href="mailto:itsaryan0710@gmail.com">itsaryan0710@gmail.com</a>
        <br>
        🌐 <a href="https://github.com/aryansingh0710" target="_blank">GitHub</a>
        <a href="https://www.linkedin.com/in/aryansingh0710" target="_blank" class="social-btn">LinkedIn</a>
    </footer>
""", unsafe_allow_html=True)
