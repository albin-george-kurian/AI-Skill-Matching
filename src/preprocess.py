import pdfminer.high_level
import docx2txt
import os

def extract_text_from_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    
    if ext == ".pdf":
        return pdfminer.high_level.extract_text(file_path)
    
    elif ext == ".docx":
        return docx2txt.process(file_path)
    
    elif ext == ".txt":
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    
    else:
        raise ValueError("Unsupported file format!")

    
if __name__ == "__main__":
    resume_text = extract_text_from_file("./data/resumes/sample_resume.pdf")
    print(resume_text)
