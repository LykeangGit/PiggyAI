# app.py  ← Copy-paste this exact file
import streamlit as st
import time          # ← this line was missing before

st.set_page_config(page_title="My Video Demo", page_icon="video", layout="centered")

# ─────────────────── RESPONSIVE MOBILE-FIRST CSS ───────────────────
st.markdown("""
<style>
    html, body, .stApp {background:#000; margin:0; padding:0; height:100%;}
    .main {max-width:100%; padding:0; background:#000;}
    .header {text-align:center; padding:50px 20px 20px; color:white;}
    .header h1 {font-size:42px; margin:0;}
    .header p  {font-size:18px; color:#aaa; margin-top:8px;}
    .video-container {
        width:100vw;
        margin-left:calc(-50vw + 50%);
        position:relative;
        left:50%;
        right:50%;
    }
    .footer {text-align:center; padding:40px 20px 60px; color:#888; font-size:14px;}
    .loading {
        height:100vh; display:flex; flex-direction:column;
        justify-content:center; align-items:center; color:white; background:#000;
    }
</style>
""", unsafe_allow_html=True)

# ─────────────────── LOADING SCREEN (only once) ───────────────────
if "ready" not in st.session_state:
    st.markdown("""
        <div class="loading">
            <h1>My App</h1>
            <p>Loading your experience...</p>
        </div>
    """, unsafe_allow_html=True)

    bar = st.progress(0)
    status = st.empty()

    for i in range(100):
        time.sleep(0.04)   # ← correct: time.sleep(), not st.time.sleep()
        bar.progress(i + 1)
        status.text(["Initializing", "Preparing video", "Almost ready", "Done!"][i//25])

    st.session_state.ready = True
    st.rerun()

# ─────────────────── MAIN PAGE ───────────────────
st.markdown('<div class="header"><h1>My Video Demo</h1><p>Best viewed on mobile • Tap to play</p></div>', 
            unsafe_allow_html=True)

# ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←
# REPLACE WITH YOUR OWN VIDEO URL
VIDEO_URL = "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4"
# ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←

with st.container():
    st.markdown('<div class="video-container">', unsafe_allow_html=True)
    st.video(VIDEO_URL)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
    <div class="footer">
        <p>Your Name • 2025 • Made with Streamlit</p>
    </div>
""", unsafe_allow_html=True)