import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.set_page_config( 
    page_title = "Chess Stats | Pixelcatt",
    page_icon = "♟️",
    layout = "wide"
)

st.markdown("""
<style>
    .chess-header {
        font-size: 2.5em;
        font-weight: bold;
        color: #2E2E2E;
        text-align: center;
        margin-bottom: 1em;
    }
    
    .stat-card {
        padding: 1.5em;
        border-radius: 10px;
        background-color: #f8f9fa;
        margin: 1em 0;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
</style>
""", unsafe_allow_html = True)

st.markdown("<h1 class='chess-header'>♟️ My Chess Journey</h1>", unsafe_allow_html = True)

col1, col2 = st.columns( [ 2, 1 ] )

with col1:
    st.markdown("""
    <div class='stat-card'>
        <h3>About My Chess Journey</h3>
        <p>I started playing chess when I was young and have been improving ever since! 
        Check out my Chess.com profile to play with me or analyze my games.</p>
        <p>My Chess.com username: pixelcatt391</p>
    </div>
    """, unsafe_allow_html = True)

with col2:
    st.markdown("""
    <div class='stat-card'>
        <h3>Quick Stats</h3>
        <ul>
            <li>Rapid Rating: ~1000</li>
            <li>Favorite Opening: Queen's Gambit</li>
            <li>Games Played: 100+</li>
        </ul>
    </div>
    """, unsafe_allow_html = True)

# Embed Chess.com Profile
st.markdown("### 🎮 My Live Chess.com Games")
st.components.v1.iframe(
    f"https://www.chess.com/member/pixelcatt391/games/archive",
    height = 600
) 
