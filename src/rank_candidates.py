from matching import match_skills
from extract_skills import extract_entities
from preprocess import extract_text_from_file
import os

def rank_resumes(resume_folder, job_description):
    resumes = [f for f in os.listdir(resume_folder) if f.endswith((".pdf", ".docx", ".txt"))]
    
    candidates = []
    for resume in resumes:
        text = extract_text_from_file(os.path.join(resume_folder, resume))
        extracted_data = extract_entities(text)
        
        score = match_skills(extracted_data["skills"], job_description)
        
        candidates.append((resume, score))
    
    ranked_candidates = sorted(candidates, key=lambda x: x[1], reverse=True)
    
    return ranked_candidates


