import time
import streamlit as st

# Initialize session state variables
if "running" not in st.session_state:
    st.session_state.running = False
if "remaining_time" not in st.session_state:
    st.session_state.remaining_time = 10

# Countdown timer function
def countdown_timer():
    st.session_state.running = True
    placeholder = st.empty()

    while st.session_state.remaining_time >= 0 and st.session_state.running:
        mins, secs = divmod(st.session_state.remaining_time, 60)
        placeholder.markdown(
            f"""
            <div style="text-align:center; font-size:40px; font-weight:bold; color:#ff5733;">
            🕘 {mins:02}:{secs:02}
            </div>
            """,
            unsafe_allow_html=True
        )
        time.sleep(1)
        st.session_state.remaining_time -= 1

    if st.session_state.remaining_time < 0:
        placeholder.success("✨ Time up! The countdown has finished!")
    else:
        placeholder.warning("🕘 Timer stopped! Click 'Start' to resume.")

# Streamlit UI
st.set_page_config(page_title="Countdown Timer", page_icon="⏳", layout="centered")

# Custom CSS for background wallpaper
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://t3.ftcdn.net/jpg/02/80/01/14/360_F_280011481_MU3nFbbMETASR5On2IexFsir5vRM3ppG.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    h1, p, .stNumberInput, .stButton button {
        color: white !important;
    }
    .stNumberInput input {
        background-color: rgba(255, 255, 255, 0.8);
        color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    "<h1 style='text-align:center; color:#ff5733;'>⏳ Countdown Timer App</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='font-size:18px; color:#333;'>Enter countdown time in seconds:</p>",
    unsafe_allow_html=True
)

# Update remaining time only if the timer is not running
if not st.session_state.running:
    st.session_state.remaining_time = st.number_input(
        "", min_value=1, step=1, value=st.session_state.remaining_time, format="%d",
        key="time_input", help="Set the countdown duration in seconds."
    )

# Custom CSS for the buttons
st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #4CAF50; /* Green for Start */
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 5px;
        padding: 10px 20px;
        border: none;
        transition: background-color 0.3s ease;
        margin: 5px;
    }
    div.stButton > button:first-child:hover {
        background-color: #45a049; /* Darker green on hover */
    }
    div.stButton > button:nth-child(2) {
        background-color: #f44336; /* Red for Stop */
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 5px;
        padding: 10px 20px;
        border: none;
        transition: background-color 0.3s ease;
        margin: 5px;
    }
    div.stButton > button:nth-child(2):hover {
        background-color: #d32f2f; /* Darker red on hover */
    }
    </style>
    """, unsafe_allow_html=True)

# Create two columns for the buttons
col1, col2 = st.columns(2)

# Start Button
with col1:
    if st.button("Start"):
        if not st.session_state.running:
            st.session_state.running = True
            countdown_timer()

# Stop Button
with col2:
    if st.button("Stop"):
        st.session_state.running = False