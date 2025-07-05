# Import library
import streamlit as st
import joblib
from clean_text_func import clean_text


# Load saved model and vectorizer
model = joblib.load("fake_news_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")


# Streamlit UI
st.title("Fake News Detector")  # Page title

# News placement area
news_input = st.text_area("Enter news content")

word_count = len(news_input.strip().split())
st.markdown("*Min: 300 words*")
st.caption(f"You have entered {word_count}")

# Minimum word count intake
#disable_button = word_count < 300


if st.button("Check News"):     # or st.button("Check News, disabled=disable_button) to disable button if word count not up to 300
    if word_count < 300:
        st.warning("Please enter a minimum of 300 words")
    else:
        cleaned = clean_text(news_input)
        vectorized = vectorizer.transform([cleaned])
        result = model.predict(vectorized)
        st.write("✅Real News" if result[0] == 1 else "❌Fake News")
