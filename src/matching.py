from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from gensim.models import Word2Vec
import numpy as np


sample_skills = [
    ["seo", "digital marketing", "content marketing", "google analytics"],
    ["python", "machine learning", "deep learning", "nlp"],
    ["java", "spring boot", "microservices", "backend development"]
]


w2v_model = Word2Vec(sample_skills, vector_size=100, min_count=1, window=5)

def skill_similarity(skill1, skill2):
    if skill1 in w2v_model.wv and skill2 in w2v_model.wv:
        return w2v_model.wv.similarity(skill1, skill2)
    return 0.0

def match_skills(resume_skills, job_desc):
    corpus = [" ".join(resume_skills), job_desc]
    
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(corpus)
    
    tfidf_similarity = cosine_similarity(vectors[0], vectors[1])[0][0]
    
    w2v_scores = [skill_similarity(skill, job_desc) for skill in resume_skills]
    w2v_score = np.mean(w2v_scores) if w2v_scores else 0.0

    final_score = (tfidf_similarity + w2v_score) / 2
    
    return final_score


