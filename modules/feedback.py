def generate_recommendations(resume_data, job_description, current_score):
    """
    Generate detailed recommendations based on resume keywords and the job description.
    It compares the resume keywords with words from the job description, identifies missing keywords,
    and estimates a potential match score improvement if those keywords were added.
    
    The heuristic assumes that each missing keyword may improve the match score by 3 percentage points.
    """
    # Normalize keywords from resume and job description
    resume_keywords = set([kw.lower() for kw in resume_data.get("keywords", [])])
    job_keywords = set([word.strip(",.").lower() for word in job_description.split() if len(word) > 3])
    
    missing_keywords = job_keywords - resume_keywords
    
    recommendations = []
    if missing_keywords:
        recommendations.append("Consider adding the following skills or keywords: " + ", ".join(list(missing_keywords)[:5]))
    else:
        recommendations.append("Your resume appears to cover the key aspects of the job description.")
    
    recommendations.append("Review your resume formatting to ensure clarity and readability.")
    
    # Heuristic: Each missing keyword contributes a 3% improvement, capped so that maximum score is 100.
    improvement = min(100, current_score + len(missing_keywords) * 3) - current_score
    estimated_new_score = current_score + improvement
    
    detailed_feedback = {
        "missing_keywords": list(missing_keywords),
        "recommendations": recommendations,
        "estimated_improvement": improvement,
        "estimated_new_score": estimated_new_score
    }
    return detailed_feedback
