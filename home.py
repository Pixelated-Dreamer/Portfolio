import streamlit as st

st.set_page_config(
    page_title = "pixelcatt",
    page_icon = "🐱",
    layout = "centered"
)

# Custom CSS for minimal design
st.markdown("""
<style>
    /* Global styles */
    .stApp {
        max-width: 1000px;
        margin: 0 auto;
    }
    
    /* Typography */
    h1 {
        font-size: 2.5em !important;
        font-weight: 800 !important;
        margin-bottom: 0.5em !important;
    }
    
    h2 {
        font-size: 1.8em !important;
        font-weight: 600 !important;
        margin-top: 1.5em !important;
    }
    
    p {
        font-size: 1.1em !important;
        line-height: 1.6 !important;
    }
    
    /* Links */
    a {
        color: #FF69B4 !important;
        text-decoration: none !important;
        border-bottom: 2px solid transparent;
        transition: border-color 0.2s ease;
    }
    
    a:hover {
        border-bottom: 2px solid #FF69B4;
    }
    
    /* Project section */
    .project {
        padding: 1em 0;
        border-bottom: 1px solid #eee;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html = True)

# Header
st.title("pixelcatt")

# About
st.markdown("""
Hi! I'm a 11-year-old software developer from the US.

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
