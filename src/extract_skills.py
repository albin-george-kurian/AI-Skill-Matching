import spacy
import os
import fitz  # PyMuPDF for PDF text extraction
from spacy.matcher import Matcher

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Define a Matcher for detecting skills
matcher = Matcher(nlp.vocab)

# Define patterns for technical skills
skill_patterns = [
    [{"LOWER": "python"}],
    [{"LOWER": "java"}],
    [{"LOWER": "tensorflow"}],
    [{"LOWER": "pytorch"}],
    [{"LOWER": "machine"}, {"LOWER": "learning"}],
    [{"LOWER": "deep"}, {"LOWER": "learning"}],
    [{"LOWER": "data"}, {"LOWER": "science"}],
    [{"LOWER": "sql"}],
    [{"LOWER": "git"}],
    [{"LOWER": "nlp"}],
    [{"LOWER": "scikit-learn"}]
]

# Add patterns to matcher
for pattern in skill_patterns:
    matcher.add("SKILL", [pattern])

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file using PyMuPDF (fitz).
    """
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text("text") + "\n"
    return text

def extract_entities(text):
    """
    Extracts skills, education, and experience from resumes using spaCy Matcher.
    """
    doc = nlp(text)

    # Find skills using pattern matching
    matches = matcher(doc)
    skills = [doc[start:end].text for match_id, start, end in matches]

    # Extract education and experience using spaCy NER
    education = [ent.text for ent in doc.ents if ent.label_ in ["ORG", "EDUCATION"]]
    experience = [ent.text for ent in doc.ents if ent.label_ == "DATE"]

    return {
        "skills": list(set(skills)),  # Remove duplicates
        "education": list(set(education)),
        "experience": list(set(experience)),
    }

# Example Usage
if __name__ == "__main__":
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    resume_path = os.path.join(BASE_DIR, "../data/resumes/sample_resume.pdf")

    # Extract text from PDF
    resume_text = extract_text_from_pdf(resume_path)

    extracted_data = extract_entities(resume_text)
    print(extracted_data)
