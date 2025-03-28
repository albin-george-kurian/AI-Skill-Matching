import streamlit as st
import os
from modules.pdf_extractor import extract_text_from_pdf
from modules.resume_analyzer import analyze_resume
from modules.matcher import calculate_similarity, generate_match_score
from modules.feedback import generate_recommendations
import csv
import datetime

st.title("AI Resume Analyzer")
st.write("Upload your PDF resume and enter a job description to get a match score, recommendations, and analytics.")


uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_description = st.text_area("Job Description", height=150)

if st.button("Analyze"):
    if uploaded_file is not None and job_description.strip() != "":
        
        temp_file_path = "temp_resume.pdf"
        with open(temp_file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        
        resume_text = extract_text_from_pdf(temp_file_path)
        
        if not resume_text:
            st.error("Failed to extract text from the uploaded PDF.")
        else:
            
            resume_data = analyze_resume(resume_text)
            
            
            similarity = calculate_similarity(resume_text, job_description)
            match_score = generate_match_score(similarity)
            
            
            feedback = generate_recommendations(resume_data, job_description, match_score)
            
            
            st.subheader("Analysis Results")
            st.write(f"**Match Score:** {match_score} / 100")
            st.write("**Extracted Keywords:**", ", ".join(resume_data.get("keywords", [])))
            
            
            st.subheader("Detailed Recommendations")
            for rec in feedback.get("recommendations", []):
                st.write("- " + rec)
            st.write(f"**Estimated Improvement:** {feedback['estimated_improvement']} points")
            st.write(f"**Estimated New Score if Missing Skills are Added:** {feedback['estimated_new_score']} / 100")
            
            
            st.subheader("Feedback")
            rating = st.slider("Rate the Analysis (1 - Poor to 5 - Excellent)", 1, 5, 3)
            if st.button("Save Feedback"):
                
                feedback_data = {
                    "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "match_score": match_score,
                    "rating": rating,
                    "missing_keywords": ";".join(feedback.get("missing_keywords", [])),
                    "recommendations": " | ".join(feedback.get("recommendations", [])),
                    "estimated_improvement": feedback["estimated_improvement"],
                    "estimated_new_score": feedback["estimated_new_score"]
                }
                file_exists = os.path.isfile("feedback.csv")
                with open("feedback.csv", "a", newline="") as csvfile:
                    fieldnames = ["timestamp", "match_score", "rating", "missing_keywords", "recommendations", "estimated_improvement", "estimated_new_score"]
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    if not file_exists:
                        writer.writeheader()
                    writer.writerow(feedback_data)
                st.success("Feedback saved successfully!")
        
        
        os.remove(temp_file_path)
    else:
        st.error("Please upload a PDF resume and enter a job description.")
