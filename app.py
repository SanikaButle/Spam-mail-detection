import streamlit as st
import os
import feature_extraction, logistic_regressionn_model

# Add CSS file to app
with open(os.path.join(os.path.dirname(__file__), 'styles/style.css')) as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)



# Define pages
def home():
    with open('feature_extraction.pkl','rb') as f:
        feature_extraction = pickle.load(f)
    with open('logistic_regressionn_model.pkl','rb') as f:
        logistic_regressionn_model = pickle.load(f)
    st.markdown("## Spam Savvy🔎")
    st.markdown("• Web application for spam email classification and spam score calculation.")
    st.markdown("• Utilizes machine learning algorithms to analyze email content and provide accurate classifications.")
    st.markdown("• Provides users with instant feedback on the likelihood of an email being spam.")
    st.image(r"C:\Users\Purva\OneDrive\Desktop\Spam detection\images\trial-removebg-preview (1).png", use_column_width=True)


    

def spam_checker():
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

def spam_score():
    # Define the layout using Streamlit's columns
    col1, col2 = st.columns([0.1, 1])  # Adjust the column widths as needed

    # Add the image to the first column
    col1.image(r"C:\Users\Purva\OneDrive\Desktop\Spam detection\images\speedometer (1).png", width=50)  # Adjust the width as needed

    # Add the text to the second column
    col2.markdown("# Spam Score")

    mail_text = st.text_area("Enter the email text:")
    if st.button("Score"):
        if mail_text:
            X = feature_extraction.transform([mail_text])
            prediction = logistic_regressionn_model.predict_proba(X)
            score = prediction[0][1]
            st.markdown(f"The spam score is {score:.2f}.")
        else:
            st.markdown("Please enter an email text.")

# Add pages to app
pages = {
    "Home": home,
    "Spam Checker": spam_checker,
    "Spam Score": spam_score
}

current_page = st.sidebar.selectbox("Navbar", list(pages.keys()))
pages[current_page]()