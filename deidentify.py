import re

def remove_pii(text):
    """Remove sensitive patient information like SSN, age"""
    text = re.sub(r"\b\d{2,3}yr\b", "[AGE]", text)  # Replace age
    text = re.sub(r"\b\d{3}-\d{2}-\d{4}\b", "[SSN]", text)  # Replace SSN
    return text

if "_name_" == "_main_":
    sample_text = "John Doe, 29yr, 123-45-6789, flu symptoms."
    print(remove_pii(sample_text))