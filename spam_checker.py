import streamlit as st
import numpy as np
from model import clf, vectorizer
import feature_extraction, logistic_regressionn_model

st.markdown("# Spam Checker")
mail_text = st.text_area("Enter the email text:")
if st.button("Check"):
    if mail_text:
        X = feature_extraction.transform([mail_text])
        prediction = logistic_regressionn_model.predict(X)
        if prediction[0] == 1:
            st.markdown("This email is spam.")
        else:
            st.markdown("This email is not spam.")
    else:
        st.markdown("Please enter an email text.")