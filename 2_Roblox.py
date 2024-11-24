import streamlit as st

st.set_page_config(
    page_title = "Roblox | Pixelcatt",
    page_icon = "🎮",
    layout = "wide"
)

st.markdown("""
<style>
    .roblox-header {
        font-size: 2.5em;
        font-weight: bold;
        color: #FF4444;
        text-align: center;
        margin-bottom: 1em;
    }
    
    .game-card {
        padding: 1.5em;
        border-radius: 10px;
        background-color: #f8f9fa;
        margin: 1em 0;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
</style>
""", unsafe_allow_html = True)

st.markdown("<h1 class='roblox-header'>🎮 My Roblox Adventures</h1>", unsafe_allow_html = True)

col1, col2 = st.columns( 2 )

with col1:
    st.markdown("""
    <div class='game-card'>
        <h3>Favorite Games</h3>
        <ul>
            <li>Blox Fruits</li>
            <li>Adopt Me</li>
            <li>Brookhaven</li>
            <li>Murder Mystery 2</li>
        </ul>
    </div>
    """, unsafe_allow_html = True)

with col2:
    st.markdown("""
    <div class='game-card'>
        <h3>My Profile</h3>
        <p>Username: checkmate39</p>
        <p>Join me in game or add me as a friend!</p>
    </div>
    """, unsafe_allow_html = True)

# Embed Roblox Profile
st.markdown("### 🎯 My Roblox Profile")
st.components.v1.iframe(
    "https://www.roblox.com/search/users?keyword=checkmate39",
    height = 600
) 
