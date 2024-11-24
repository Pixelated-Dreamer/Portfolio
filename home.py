import streamlit as st

st.set_page_config(
    page_title = "pixelcatt",
    page_icon = "🐱",
    layout = "centered"
)

# Custom CSS for dark theme, grid, and topbar
st.markdown("""
<style>
    /* Dark theme and grid background */
    .stApp {
        max-width: 100%;
        margin: 0;
        background-color: #0E1117;
        background-image: 
            linear-gradient(rgba(50, 50, 50, 0.1) 1px, transparent 1px),
            linear-gradient(90deg, rgba(50, 50, 50, 0.1) 1px, transparent 1px);
        background-size: 20px 20px;
    }
    
    /* Topbar styling */
    .topbar {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        height: 60px;
        background-color: rgba(17, 19, 24, 0.8);
        backdrop-filter: blur(10px);
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 2rem;
        z-index: 1000;
    }
    
    .logo {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        color: white;
        font-size: 1.2rem;
        font-weight: 600;
    }
    
    .nav-links {
        display: flex;
        gap: 2rem;
    }
    
    .nav-link {
        color: #8F9094 !important;
        display: flex;
        align-items: center;
        gap: 0.5rem;
        transition: color 0.2s ease;
    }
    
    .nav-link:hover {
        color: white !important;
        border-bottom: none !important;
    }
    
    /* Content padding to account for fixed topbar */
    .main-content {
        margin-top: 80px;
        padding: 0 2rem;
    }
    
    /* Typography in dark theme */
    h1, h2, h3, p {
        color: white !important;
    }
    
    /* Links */
    a {
        color: #FF69B4 !important;
        text-decoration: none !important;
        transition: color 0.2s ease;
    }
    
    a:hover {
        color: #ff8cc6 !important;
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>

<div class="topbar">
    <div class="logo">
        <img src="https://raw.githubusercontent.com/Pixelated-Dreamer/portfolio/main/assets/logo.png" height="30px">
        pixelcatt
    </div>
    <div class="nav-links">
        <a href="https://www.youtube.com/@pixelcatt" class="nav-link" target="_blank">
            <i class="fab fa-youtube"></i> YouTube
        </a>
        <a href="https://www.twitch.tv/pixelcatt" class="nav-link" target="_blank">
            <i class="fab fa-twitch"></i> Twitch
        </a>
        <a href="https://github.com/Pixelated-Dreamer" class="nav-link" target="_blank">
            <i class="fab fa-github"></i> GitHub
        </a>
        <a href="#about" class="nav-link">
            <i class="fas fa-user"></i> About
        </a>
        <a href="#projects" class="nav-link">
            <i class="fas fa-code"></i> Projects
        </a>
        <a href="#contact" class="nav-link">
            <i class="fas fa-envelope"></i> Contact
        </a>
    </div>
</div>

<!-- Font Awesome for icons -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">

<div class="main-content">
""", unsafe_allow_html = True)

# Rest of your content
st.title("pixelcatt")

# About
st.markdown("""
Hi! I'm a 12-year-old software developer from the US.

I create interactive web applications and enjoy playing chess and Roblox.
""")

# Projects
st.header("projects")

st.markdown("""
<div class="project">
    <h3>story generator</h3>
    <p>An AI-powered story generator that creates unique tales based on user input.</p>
    <a href="https://story-generator-pixelatedreamer.streamlit.app/" target="_blank">view project →</a>
</div>
""", unsafe_allow_html = True)

st.markdown("""
<div class="project">
    <h3>moving average calculator</h3>
    <p>A financial tool for calculating and visualizing moving averages.</p>
    <a href="https://ma-pixelcatt.streamlit.app/" target="_blank">view project →</a>
</div>
""", unsafe_allow_html = True)

# Links
st.header("links")

st.markdown("""
- [github](https://github.com/Pixelated-Dreamer)
- [chess.com](https://www.chess.com/member/pixelcatt391)
- [roblox](https://www.roblox.com/search/users?keyword=checkmate39)
- [email](mailto:nevaankantai@gmail.com)
""")

# Contact
st.header("contact")

st.markdown("""
Feel free to reach out if you'd like to collaborate or just chat!

You can email me at [nevaankantai@gmail.com](mailto:nevaankantai@gmail.com)
""")

# Close the main-content div
st.markdown("</div>", unsafe_allow_html=True) 
