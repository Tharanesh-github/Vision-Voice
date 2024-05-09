from googletrans import Translator

# Function to translate text to Sinhala
def translate_to_sinhala(text):
    translator = Translator()
    translated_text = translator.translate(text, dest='si').text
    return translated_text

# Function to translate text to Tamil
def translate_to_tamil(text):
    translator = Translator()
    translated_text = translator.translate(text, dest='ta').text
    return translated_text

# Function to load text from a file
def load_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

# Function to save translated text to a file
def save_text_to_file(text, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)

# Example usage
input_file_path = 'F:/University IIT/Coursework 1 (SDGP)/Implementation/MERGE/Text_com/summarized_content.txt'
output_file_path_sinhala = 'F:/University IIT/Coursework 1 (SDGP)/Implementation/MERGE/Text_com/output_sinhala.txt'
output_file_path_tamil = 'F:/University IIT/Coursework 1 (SDGP)/Implementation/MERGE/Text_com/output_tamil.txt'

# Load text from input file
input_text = load_text_from_file(input_file_path)

# Translate text to Sinhala
translated_text_sinhala = translate_to_sinhala(input_text)

# Translate text to Tamil
translated_text_tamil = translate_to_tamil(input_text)

# Save translated text to output files
save_text_to_file(translated_text_sinhala, output_file_path_sinhala)
save_text_to_file(translated_text_tamil, output_file_path_tamil)

print("Translation completed. Output saved to", output_file_path_sinhala, "and", output_file_path_tamil)