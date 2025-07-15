import streamlit as st
from text_cleaner import TextClean
import joblib

# Load model
model = joblib.load("sentiment_pipeline.pkl")
label_map = {0: "Negative", 4: "Positive"}

# Page setup
st.set_page_config(page_title="Sentiment Analyzer", layout="centered")

# Header
st.title("🧠 Sentiment Analyzer")
st.markdown("Analyze sentiment (Positive or Negative) from any tweet or sentence.")

# Input section
st.subheader("🔤 Enter Your Text:")
user_input = st.text_area("", placeholder="Type or paste a tweet here...", height=150)

# Predict and show result
if st.button("🔍 Analyze"):
    if user_input.strip() == "":
        st.warning("🚫 Please enter some text before analyzing.")
    else:
        predicted_label = int(model.predict([user_input])[0])
        prediction = label_map[predicted_label]

        if predicted_label == 0:
            st.markdown(
                f"<div style='background-color:#ffe6e6;padding:10px;border-radius:10px'>"
                f"<h4 style='color:red;'>😠 Predicted Sentiment: Negative</h4></div>",
                unsafe_allow_html=True)
        else:
            st.markdown(
                f"<div style='background-color:#e6ffe6;padding:10px;border-radius:10px'>"
                f"<h4 style='color:green;'>😊 Predicted Sentiment: Positive</h4></div>",
                unsafe_allow_html=True)
