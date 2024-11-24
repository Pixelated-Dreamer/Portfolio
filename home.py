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
    
    /* Card Styles */
    .cards-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 2rem;
        margin-top: 2rem;
    }
    
    .card {
        background: rgba(255, 255, 255, 0.05);
        padding: 2rem;
        border-radius: 1rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        text-align: center;
        transition: transform 0.2s ease;
    }
    
    .card:hover {
        transform: translateY(-5px);
    }
    
    .card i {
        font-size: 2.5rem;
        margin-bottom: 1rem;
        background: linear-gradient(45deg, #FF69B4, #9F7AEA);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* Projects Grid */
    .projects-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        margin-top: 2rem;
    }
    
    .project-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 2rem;
        border-radius: 1rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: transform 0.2s ease;
    }
    
    .project-card:hover {
        transform: translateY(-5px);
    }
    
    .project-link {
        display: inline-block;
        margin-top: 1rem;
        color: #FF69B4;
        text-decoration: none;
        transition: color 0.2s ease;
    }
    
    .project-link:hover {
        color: #9F7AEA;
    }
</style>

<div class="topbar">
    <div class="logo">
        <img src="your-logo-path.png" height="30px">
        WintrCat
    </div>
    <div class="nav-links">
        <a href="https://www.roblox.com/users/pixelcatt" class="nav-link" target="_blank">
            <i class="fas fa-gamepad"></i>
        </a>
        <a href="https://github.com/Pixelated-Dreamer" class="nav-link" target="_blank">
            <i class="fab fa-github"></i>
        </a>
        <a href="https://chess.com/member/Pixelcatt391" class="nav-link" target="_blank">
            <i class="fas fa-chess"></i>
        </a>
    </div>
</div>

<!-- Font Awesome -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">

<div class="main-content">
    <div class="hero-center">
        <img src="coffee-cup.png" alt="Coffee Cup" class="coffee-icon">
        <h1>hi, i'm Nevaan</h1>
        <p class="subtitle">Developer, Video Editor, Chess Player.</p>
    </div>
</div>

<style>
    .hero-center {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 100vh;
        text-align: center;
        padding: 2rem;
    }
    
    .coffee-icon {
        width: 120px;
        height: auto;
        margin-bottom: 2rem;
    }
    
    .hero-center h1 {
        font-size: 4rem;
        font-weight: 600;
        margin: 1rem 0;
        color: white;
    }
    
    .subtitle {
        font-size: 1.2rem;
        color: rgba(255, 255, 255, 0.7) !important;
        font-style: italic;
    }
</style>
""", unsafe_allow_html = True) 
