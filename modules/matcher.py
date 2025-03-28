import spacy


nlp = spacy.load("en_core_web_sm")

def calculate_similarity(resume_text, job_desc_text):
    """
    Calculate similarity between resume text and job description text using spaCy.
    Returns a similarity score (0 to 1).
    """
    doc_resume = nlp(resume_text)
    doc_job = nlp(job_desc_text)
    score = doc_resume.similarity(doc_job)
    return score

def generate_match_score(similarity, scale=100):
    """
    Convert the similarity score to a match score out of the given scale (default 100).
    """
    return round(similarity * scale)
