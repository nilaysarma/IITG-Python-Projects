# Week 6 Lab: Language Detection
# Description: Create a small text sample (~50 sentences) by copy pasting translations from the following link. Note the 50 sentences should be drawn from multiple languages (e.g., English, Russian, Hindi, Chinese, Arabic, Spanish, French, German, Japanese, Korean, and more!). Let the resulting file.txt you thus created named as file.txt and this resides in your system.

import unicodedata

def detect_script(char):
    try:
        return unicodedata.name(char).split()[0]
    except ValueError:
        return "UNKNOWN"
    
def analyze_text_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()

    script_counts = {}
    for char in text:
        if char.isalpha():
            script = detect_script(char)
            script_counts[script] = script_counts.get(script, 0) + 1

    return script_counts

file_results = analyze_text_file("file.txt")
print(file_results)
