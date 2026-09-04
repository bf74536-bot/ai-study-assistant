import streamlit as st
from google import genai

st.set_page_config(page_title="AI Study Assistant", page_icon="📚", layout="wide")
st.title("📚 AI Smart Notes & Quiz Generator")
st.write("Paste your textbook text below to generate revision notes and diagnostic practice questions.")

raw_text = st.text_area("Paste Textbook Chapter Material Here:", height=250, placeholder="Type or paste textbook content...")

if st.button("Generate Learning Assets ✨"):
    if raw_text.strip():
        with st.spinner("Processing study material..."):
            try:
                client = genai.Client()
                prompt = f"""
                Analyze the following educational content: '{raw_text}'.
                Provide two clear sections:
                1. CORE STUDY NOTES: Summarize key theories, formulas, or timelines using clean bullet points.
                2. QUICK SELF-ASSESSMENT QUIZ: Generate 3 multiple-choice questions with solutions.
                """
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt,
                )
                st.success("Study materials prepared successfully!")
                st.markdown("---")
                st.write(response.text)
            except Exception as e:
                st.error(f"API Execution Failure: Check that your Gemini key is properly assigned. Details: {e}")
    else:
        st.warning("Please input some study material text before compiling.")
