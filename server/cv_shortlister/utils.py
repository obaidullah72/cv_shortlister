import os
import re
import logging
from django.core.files.storage import default_storage
from pdfminer.high_level import extract_text as pdf_extract_text
from docx import Document
import pytesseract
from pdf2image import convert_from_path
import spacy

logger = logging.getLogger(__name__)

# Load spaCy model with error handling
try:
    nlp = spacy.load("en_core_web_sm")
except OSError as e:
    logger.error(f"Failed to load spaCy model 'en_core_web_sm': {str(e)}")
    logger.error("Please run 'python -m spacy download en_core_web_sm' to install the model.")
    nlp = None

def extract_text_from_file(file_path):
    """Extract text from uploaded file (PDF, DOCX, TXT, or scanned PDF)."""
    try:
        if not default_storage.exists(file_path):
            raise FileNotFoundError(f"File not found at {file_path}")

        ext = os.path.splitext(file_path)[1].lower()
        
        if ext == '.pdf':
            try:
                pages = convert_from_path(file_path)
                text = ""
                for page in pages:
                    text += pytesseract.image_to_string(page)
                if not text.strip():
                    text = pdf_extract_text(file_path)
                return text
            except Exception:
                return pdf_extract_text(file_path)
                
        elif ext == '.docx':
            doc = Document(file_path)
            return '\n'.join([para.text for para in doc.paragraphs])
            
        elif ext == '.txt':
            with default_storage.open(file_path, 'r') as f:
                return f.read()
                
        else:
            raise ValueError(f"Unsupported file type: {ext}")
            
    except Exception as e:
        logger.error(f"Error extracting text from {file_path}: {str(e)}")
        return None

def extract_entities(text):
    """Extract structured data using spaCy NER."""
    if nlp is None:
        logger.error("spaCy model not loaded. Entity extraction unavailable.")
        return {'error': 'NLP model not available'}

    try:
        doc = nlp(text)
        entities = {
            'name': [],
            'education': [],
            'skills': [],
            'experience': [],
            'organizations': []
        }
        
        for ent in doc.ents:
            if ent.label_ == "PERSON":
                entities['name'].append(ent.text)
            elif ent.label_ in ["ORG", "GPE"]:
                entities['organizations'].append(ent.text)
            elif ent.label_ == "DATE":
                if "year" in ent.text.lower():
                    entities['experience'].append(ent.text)

        skill_keywords = {'python', 'java', 'sql', 'django', 'machine learning'}
        education_keywords = {'bachelor', 'master', 'phd', 'high school', 'degree'}
        
        for token in doc:
            if token.text.lower() in skill_keywords:
                entities['skills'].append(token.text)
            if token.text.lower() in education_keywords:
                entities['education'].append(token.text)

        for key in entities:
            entities[key] = list(set(entities[key]))
            
        return entities
    except Exception as e:
        logger.error(f"Error extracting entities: {str(e)}")
        return None

def check_experience(text, min_years):
    """Check if experience meets minimum requirement."""
    pattern = r'(\d+)\s*(years|yrs|yr)'
    matches = re.findall(pattern, text.lower())
    return any(int(num) >= min_years for num, _ in matches) if matches else False