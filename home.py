import streamlit as st
from PIL import Image
import webbrowser

# Page config
st.set_page_config(
    page_title = "Pixelcatt | Portfolio",
    page_icon = "🐱",
    layout = "wide"
)

# Custom CSSL
st.markdown("""
<style>
    .main-header {
        font-size: 3em;
        font-weight: bold;
        color: #FF69B4;  /* Pink color for your pixelcatt theme */
        text-align: center;
        margin-bottom: 1em;
    }
    
    .sub-header {
        font-size: 1.5em;
        color: #808080;
        text-align: center;
    }
    
    .project-card {
        padding: 1em;
        border-radius: 10px;
        background-color: #f0f0f0;
        margin: 1em 0;
    }
    
    a {
        color: #FF69B4;
        text-decoration: none;
    }
    
    a:hover {
        color: #FF1493;
    }
</style>
""", unsafe_allow_html = True)

# Header
st.markdown("<h1 class='main-header'>👋 Hi, I'm Pixelcatt!</h1>", unsafe_allow_html = True)
st.markdown("<p class='sub-header'>12-year-old Software Developer | Chess Player | Roblox Enthusiast</p>", unsafe_allow_html = True)

# About Me Section
col1, col2 = st.columns( [ 1, 2 ] )

with col1:
    # Add your profile picture here
    st.image("path_to_your_profile_picture.jpg", width = 300)

with col2:
    st.markdown("""
    ### About Me
    
    I'm a young developer passionate about creating fun and interactive applications! 
    When I'm not coding, you can find me:
    - ♟️ Playing chess on Chess.com as [pixelcatt391](https://www.chess.com/member/pixelcatt391)
    - 🎮 Having fun on Roblox as [checkmate39](https://www.roblox.com/search/users?keyword=checkmate39)
    - 🌟 Learning new programming concepts
    - 🎨 Working on creative projects
    """)

# Projects Section
st.markdown("## 🚀 My Projects")

col1, col2 = st.columns( 2 )

with col1:
    st.markdown("""
    <div class='project-card'>
        <h3>Story Generator</h3>
        <p>An AI-powered story generator that creates unique tales based on user input.</p>
        <a href='https://story-generator-pixelatedreamer.streamlit.app/' target='_blank'>View Project →</a>
    </div>
    """, unsafe_allow_html = True)

with col2:
    st.markdown("""
    <div class='project-card'>
        <h3>Moving Average Calculator</h3>
        <p>A tool for calculating and visualizing moving averages in financial data.</p>
        <a href='https://ma-pixelcatt.streamlit.app/' target='_blank'>View Project →</a>
    </div>
    """, unsafe_allow_html = True)

# Skills Section
st.markdown("## 💻 Skills")

skills = {
    "Python": 90,
    "Streamlit": 85,
    "Web Development": 70,
    "Problem Solving": 80
}

for skill, level in skills.items():
    st.markdown(f"### {skill}")
    st.progress( level / 100 )

# Contact Section
st.markdown("## 📫 Let's Connect!")

contact_col1, contact_col2, contact_col3, contact_col4 = st.columns( 4 )

with contact_col1:
    if st.button("🐱 GitHub"):
        webbrowser.open("https://github.com/Pixelated-Dreamer")

with contact_col2:
    if st.button("♟️ Chess.com"):
        webbrowser.open("https://www.chess.com/member/pixelcatt391")

with contact_col3:
    if st.button("🎮 Roblox"):
        webbrowser.open("https://www.roblox.com/search/users?keyword=checkmate39")

with contact_col4:
    if st.button("📧 Email"):
        webbrowser.open("mailto:nevaankantai@gmail.com")

# Add a contact form section
st.markdown("### 💌 Send me a message")
st.markdown("""
<div style="background-color: #f8f9fa; padding: 20px; border-radius: 10px;">
    <p>Feel free to reach out to me at: 
        <a href="mailto:nevaankantai@gmail.com">nevaankantai@gmail.com</a>
    </p>
</div>
""", unsafe_allow_html = True) 
