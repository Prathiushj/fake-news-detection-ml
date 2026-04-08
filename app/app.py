import streamlit as st
import pickle

# ---------------- LOAD CSS ---------------- #
def load_css():
    with open("app/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# ---------------- LOAD MODEL ---------------- #
model = pickle.load(open("model/model.pkl", "rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(page_title="Fake News Detector", layout="centered")

# ---------------- SIDEBAR ---------------- #
st.sidebar.title("📌 About Project")
st.sidebar.write("""
This system detects whether a news article is **Real or Fake** using Machine Learning.

**Technologies Used:**
- Python
- Scikit-learn
- NLP (TF-IDF)
- Streamlit

**Developed by:**
- Yedhu Krishnan TA 
-  Prathiush Jayaprakash
""")

# ---------------- HEADER ---------------- #
st.markdown("""
<h1 style='text-align: center; color: #4A90E2;'>📰 Fake News Detection</h1>
<p style='text-align: center;'>Analyze news content using Machine Learning</p>
""", unsafe_allow_html=True)

st.write("---")

# ---------------- INPUT SECTION ---------------- #
st.markdown("### 📝 Enter News Content")

user_input = st.text_area(
    "Paste your news article here:",
    height=200,
    placeholder="Type or paste news content..."
)

# Center button
col1, col2, col3 = st.columns([1,2,1])
with col2:
    check = st.button("🔍 Analyze News")

st.write("---")

# ---------------- RESULT SECTION ---------------- #
if check:
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some news text.")
    else:
        with st.spinner("Analyzing news..."):
            transformed = vectorizer.transform([user_input])
            prediction = model.predict(transformed)[0]

            # Confidence score
            try:
                proba = model.predict_proba(transformed)[0]
                confidence = max(proba) * 100
            except:
                confidence = None

        # Decide label + style
        if prediction == 0:
            label = "FAKE"
            css_class = "fake"
            icon = "🚨"
        else:
            label = "REAL"
            css_class = "real"
            icon = "✅"

        # Display result card
        st.markdown(f"""
        <div class="result-card {css_class}">
            <h3>{icon} Prediction: {label}</h3>
            <p>The model predicts that this news is <b>{label}</b>.</p>
            {"<p class='confidence'>Confidence: " + f"{confidence:.2f}%" + "</p>" if confidence else ""}
        </div>
        """, unsafe_allow_html=True)