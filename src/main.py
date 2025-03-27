from rank_candidates import rank_resumes

if __name__ == "__main__":
    job_description = "We are hiring an expert in Python, NLP, and Machine Learning."
    ranked_candidates = rank_resumes("./data/resumes/", job_description)
    
    print("Candidate Rankings:")
    for rank, (resume, score) in enumerate(ranked_candidates, start=1):
        print(f"Rank {rank}: {resume} - Score: {score:.2f}")


