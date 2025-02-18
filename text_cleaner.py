import re
import spacy
from fuzzywuzzy import process

nlp = spacy.load("en_core_web_sm")

# Standard medical terms dictionary
medical_terms = {
    "diabties": "diabetes",
    "insuln": "insulin",
    "Hypertensn": "Hypertension",
    "possble": "possible"
}

def correct_spelling(text):
    """Correct misspelled words using predefined medical terms"""
    words = text.split()
    corrected_words = [medical_terms.get(word.lower(), word) for word in words]
    return " ".join(corrected_words)

def remove_special_chars(text):
    """Remove unwanted characters"""
    return re.sub(r"[^a-zA-Z0-9\s]", "", text)

def lemmatize_text(text):
    """Lemmatize words using spaCy"""
    doc = nlp(text)
    return " ".join([token.lemma_ for token in doc])

def clean_text(text):
    """Apply all text preprocessing steps"""
    text = correct_spelling(text)
    text = remove_special_chars(text)
    text = lemmatize_text(text)
    return text

if "_name_" == "_main_":
    sample_text = "Pt. has diabties, recommend insuln."
    print(clean_text(sample_text))