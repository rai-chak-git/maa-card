import streamlit as st
import time

# --- Page Configuration ---
st.set_page_config(page_title="For Maa 💖", page_icon="🌸", layout="centered")

# --- Custom Styling for Animations & Card ---
st.markdown("""
    <style>
    .stApp {
        background-color: #fff5f7;
    }
    .main-title {
        font-family: 'Georgia', serif;
        color: #d63384;
        text-align: center;
        font-size: 50px;
        font-weight: bold;
        margin-top: 100px;
        animation: fadeIn 3s;
    }
    .card-container {
        border: 10px double #ffb6c1;
        padding: 30px;
        background-color: white;
        border-radius: 15px;
        font-family: 'Palatino', serif;
        color: #444;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
    </style>
    """, unsafe_allow_html=True)

# --- Session State to manage page transitions ---
if 'page' not in st.session_state:
    st.session_state.page = 1

def next_page():
    st.session_state.page += 1

# --- Logic for Transitions ---

# PAGE 1: Intro
if st.session_state.page == 1:
    st.markdown('<div class="main-title">Happy Mother\'s Day <br> to my beautiful Maa 🌸</div>', unsafe_allow_html=True)
    time.sleep(1) # Slight pause for effect
    if st.button("Next ➔"):
        next_page()
        st.rerun()

# PAGE 2: The Hook
elif st.session_state.page == 2:
    st.markdown('<div class="main-title">I have a surprise for you... 🎁</div>', unsafe_allow_html=True)
    if st.button("What is it? ➔"):
        next_page()
        st.rerun()

# PAGE 3: The Question
elif st.session_state.page == 3:
    st.markdown('<div class="main-title">Are you ready to receive the surprise?</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Yes"):
            next_page()
            st.rerun()
    with col2:
        if st.button("Option One"): # As requested
            next_page()
            st.rerun()

# PAGE 4: The Digital Card[span_0](start_span)[span_0](end_span)[span_1](start_span)[span_1](end_span)
elif st.session_state.page == 4:
    st.balloons()
    st.markdown("""
    <div class="card-container">
        <h2 style="text-align:center; color:#d63384;">💖 A SPECIAL MOTHER'S DAY TRIBUTE 💖</h2>
        <hr style="border: 1px solid #ffb6c1;">
        <p><b>My Dearest Maa,</b></p>
        <p>Happy Mother's Day! Today is all about celebrating you. As I was thinking about everything you mean to me, a few special things came to mind:</p>
        
        <p>🌟 <b>One of my absolute favorite memories:</b><br>
        The winter afternoons we had spent together among the Merigold garden when I was younger. That moment always brings a smile to my face.</p>
        
        <p>🌟 <b>Words that describe you best:</b><br>
        I think of how remarkably <b>Most powerful</b> and truly <b>Most beautiful</b> you are.</p>
        
        <p>🌟 <b>Thank you for teaching me:</b><br>
        How to see the good things in any kind of places or situations. That lesson has shaped who I am today.</p>
        
        <p>🌟 <b>Taste of home:</b><br>
        It would definitely be your <b>Aalu posto</b>. Nothing else compares!</p>
        
        <p>Above all, I just want you to know how much I appreciate your <b>Patience and belief</b>.</p>
        
        <p>I love you more than words can say.</p>
        <p style="text-align:right;"><b>All my love,<br>Babin</b><br>May 12, 2024</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    # Display the hug gif at the end
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM2o0Zmt4ZzRndmN4ZzRndmN4ZzRndmN4ZzRndmN4ZzRndmN4ZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Vz58J8shFW6BvqnYTz/giphy.gif", caption="A big hug for you!")
