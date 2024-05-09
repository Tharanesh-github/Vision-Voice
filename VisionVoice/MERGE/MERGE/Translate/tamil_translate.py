from googletrans import Translator
#Here the translator is imported from the googletrans library

def translate_to_tamil(text):
    try:
        translator = Translator()
        translated_text = translator.translate(text, dest='ta').text
        return translated_text
    except Exception as e:
        error = "An error happened when trying to translate text: " + str(e)
        return error

# Function to load text from a file
def load_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

# Function to save translated text to a file
def save_text_to_file(text, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)

input_file_path = '../Text_com/summarized_content.txt'
output_file_path_tamil = '../Text_com/output_tamil.txt'

# Load text from input file
input_text = load_text_from_file(input_file_path)
print("Loaded the input text which is the summarized content")

# Translate text to Tamil
translated_text_tamil = translate_to_tamil(input_text)
print("Translated text to tamil")
save_text_to_file(translated_text_tamil, output_file_path_tamil)

print("Translation completed. Output saved to", output_file_path_tamil)