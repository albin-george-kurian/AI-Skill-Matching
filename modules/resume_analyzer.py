import spacy


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
    
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    noun_chunks = [chunk.text for chunk in doc.noun_chunks]
    keywords = list(set(noun_chunks))  
    return {
        "entities": entities,
        "keywords": keywords,
        "full_text": text
    }
