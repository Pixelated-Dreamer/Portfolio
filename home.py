import streamlit as st

st.set_page_config(
    page_title = "WintrCat",
    page_icon = "🐱",
    layout = "centered"
)

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
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
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
        font-size: 1.5rem;
        transition: all 0.2s ease;
        opacity: 0.7;
    }
    
    .nav-link:hover {
        color: white !important;
        opacity: 1;
        transform: translateY(-2px);
    }
    
    /* Hero section */
    .hero {
        text-align: center;
        padding: 4rem 0;
        max-width: 800px;
        margin: 0 auto;
    }
    
    .hero h1 {
        font-size: 3.5rem;
        margin-bottom: 1rem;
        background: linear-gradient(45deg, #FF69B4, #9F7AEA);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .hero p {
        font-size: 1.2rem;
        color: #8F9094 !important;
        line-height: 1.6;
    }
    
    /* Content sections */
    .section {
        margin: 4rem 0;
        padding: 2rem;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 1rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Main content padding */
    .main-content {
        margin-top: 80px;
        padding: 0 2rem;
    }
</style>

<div class="topbar">
    <div class="logo">
        <img src="your-logo-path.png" height="30px">
        WintrCat
    </div>
    <div class="nav-links">
        <a href="https://www.roblox.com/users/your-profile" class="nav-link" target="_blank">
            <i class="fas fa-gamepad"></i>
        </a>
        <a href="https://github.com/your-username" class="nav-link" target="_blank">
            <i class="fab fa-github"></i>
        </a>
        <a href="https://chess.com/member/your-profile" class="nav-link" target="_blank">
            <i class="fas fa-chess"></i>
        </a>
    </div>
</div>

<!-- Font Awesome -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">

<div class="main-content">
    <div class="hero">
        <h1>hi, i'm Wilson</h1>
        <p>Developer, Video Editor, Chess Player.</p>
    </div>

    <div class="section">
        <h2>About Me</h2>
        <p>I create interactive web applications and enjoy playing chess and Roblox.</p>
    </div>

    <div class="section">
        <h2>Projects</h2>
        <div class="project">
            <h3>story generator</h3>
            <p>An AI-powered story generator that creates unique tales based on user input.</p>
            <a href="https://story-generator-pixelatedreamer.streamlit.app/" target="_blank">view project →</a>
        </div>
        
        <div class="project" style="margin-top: 2rem;">
            <h3>moving average calculator</h3>
            <p>A financial tool for calculating and visualizing moving averages.</p>
            <a href="https://ma-pixelcatt.streamlit.app/" target="_blank">view project →</a>
        </div>
    </div>

    <div class="section">
        <h2>Contact</h2>
        <p>Feel free to reach out if you'd like to collaborate or just chat!</p>
        <a href="mailto:your-email@example.com">your-email@example.com</a>
    </div>
</div>
""", unsafe_allow_html = True)

# Close the main-content div
st.markdown("</div>", unsafe_allow_html=True) 
