from googletrans import Translator

def translate_hinglish_to_english(text):
    translator = Translator()
    translated = translator.translate(text, src='hi', dest='en')
    return translated.text

def translate_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        hinglish_text = file.readlines()

    translated_text = []
    for line in hinglish_text:
        translated_line = translate_hinglish_to_english(line)
        translated_text.append(translated_line)

    with open(output_file, 'w', encoding='utf-8') as file:
        for line in translated_text:
            file.write(line + '\n')

# Input and output file paths
input_file_path = 'hinglish_input.txt'
output_file_path = 'translated_english.txt'

# Translate the Hinglish file to English
translate_file(input_file_path, output_file_path)

print("Translation completed. Translated text saved in", output_file_path)
