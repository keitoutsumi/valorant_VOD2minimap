import pytesseract

def extract_text(image, config):
    return pytesseract.image_to_string(image, config=config)
