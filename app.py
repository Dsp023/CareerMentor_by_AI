import requests
import streamlit as st
from streamlit_lottie import st_lottie
import json
import streamlit as st
api_key = st.secrets["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]

st.set_page_config(page_title="CareerWise - AI Career Mentor", page_icon="🎯", layout="wide")

# Load Lottie animation for aesthetics
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Sidebar
with st.sidebar:
    st.markdown("## 🧠 Your Profile")
    skills = st.text_input("Your Skills", "Python, SQL, ML")
    interests = st.text_input("Your Interests", "AI, Web Development")
    goal = st.text_input("Your Career Goal", "Become a Data Scientist")
    get_advice = st.button("🎓 Get Advice")

# Main Title
st.markdown("""
    <div style='text-align: center;'>
        <h1 style='font-size: 3em;'>🎯 CareerWise - AI Career Mentor</h1>
        <h3 style='color: #cccccc;'>(Powered by Groq LLM)</h3>
    </div>
""", unsafe_allow_html=True)

st.markdown("### 📌 Career Recommendations")

if get_advice:
    with st.spinner("Analyzing your profile with AI..."):
        prompt = f"""Based on the user's skills: {skills}, interests: {interests}, and career goal: {goal}, recommend:
        1. Top 3 career paths
        2. Best free and paid courses for each
        3. Related job roles
        4. 2-line motivational career advice."""

        try:
            response = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {st.secrets['GROQ_API_KEY']}"
                },
                json={
                    "model": "llama3-8b-8192",
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0.7,
                    "max_tokens": 700
                }
            )
            reply = response.json()["choices"][0]["message"]["content"]
            st.markdown(f"""
                <div style='background-color: #222; padding: 20px; border-radius: 10px;'>
                    <pre style='color: white; font-size: 1em;'>{reply}</pre>
                </div>
            """, unsafe_allow_html=True)
        except Exception as e:
            st.error(f"❌ Error: {e}")
else:
    st.info("👈 Enter your profile in the sidebar and click 'Get Advice'")
