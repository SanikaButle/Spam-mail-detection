import streamlit as st
import numpy as np
from model import clf, vectorizer

st.markdown("# Spam Score")
mail_text = st.text_area("Enter the email text:")
if st.button("Score"):
    if mail_text:
        X = vectorizer.transform([mail_text])
        prediction = clf.predict_proba(X)
        score = prediction[0][1]
        st.markdown(f"The spam score is {score:.2f}.")
    else:
        st.markdown("Please enter an email text.")