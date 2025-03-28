import spacy

# Load spaCy model (ensure you have downloaded "en_core_web_sm")
nlp = spacy.load("en_core_web_sm")

def analyze_resume(text):
    """
    Analyze resume text using spaCy to extract entities and keywords.
    Returns a dictionary with:
      - entities: list of (text, label) tuples.
      - keywords: list of noun chunks deduplicated.
      - full_text: the original text.
    """
    doc = nlp(text)
    # Extract entities
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    # Extract noun chunks as potential keywords
    noun_chunks = [chunk.text for chunk in doc.noun_chunks]
    keywords = list(set(noun_chunks))  # deduplicate
    return {
        "entities": entities,
        "keywords": keywords,
        "full_text": text
    }
