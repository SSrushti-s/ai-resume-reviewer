import streamlit as st
import json
from app.pdf_loader import extract_text_from_pdf 
from app.agent import get_resume_review

# Set up the web page title and icon
st.set_page_config(page_title="AI Resume Reviewer", page_icon="📄", layout="centered")

st.title("📄 AI Resume Reviewer")
st.write("Upload your resume and paste the job description to get instant AI feedback.")

# Create the input UI components
uploaded_file = st.file_uploader("Upload your Resume (PDF format)", type=["pdf"])

job_desc = st.text_area(
    "Paste the Job Description here", 
    placeholder="Looking for a Front-End Developer proficient in React, Node.js..."
)

# Add an action button
if st.button("Analyze Resume", type="primary"):
    if not uploaded_file:
        st.error("Please upload a PDF resume first.")
    elif not job_desc.strip():
        st.error("Please paste a job description.")
    else:
        with st.spinner("Analyzing Resume... please wait."):
            try:
                # 1. Read the uploaded file directly from Streamlit's buffer
                resume_content = extract_text_from_pdf(uploaded_file)
                
                # 2. Run your existing AI agent logic
                result = get_resume_review(resume_content, job_desc)
                
                # 3. Display the results visually in the UI
                st.success("Analysis Complete!")
                
                # Display Score using a large metric visual
                score = result.get('match_percentage', 0)
                st.metric(label="Job Match Score", value=f"{score}%")
                
                # Display the full structured breakdown
                st.subheader("Detailed AI Evaluation")
                st.json(result)
                
            except Exception as e:
                st.error(f"An error occurred during analysis: {e}")