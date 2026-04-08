import streamlit as st

# Page config
st.set_page_config(page_title="Fake News Detector", layout="centered")

# Header
st.markdown("<h1 style='text-align: center; color: #2E86C1;'>📰 Fake News Detection</h1>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center;'>Detect whether a news article is <b>Real</b> or <b>Fake</b> using Machine Learning.</p>", unsafe_allow_html=True)

st.write("---")

# Input section
st.subheader("Enter News Content")

user_input = st.text_area("Paste the news article below:", height=200)

# Button centered
col1, col2, col3 = st.columns([1,2,1])
with col2:
    check = st.button("🔍 Analyze News")

# Output section
st.write("---")

if check:
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some news text.")
    else:
        st.info("⏳ Analyzing... (Model will be connected next step)")