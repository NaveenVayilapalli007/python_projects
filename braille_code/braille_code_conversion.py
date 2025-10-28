# Databricks notebook source
# --- FULL CODE ---
BRAILLE_DICT = {
    'a': '\u2801', 'b': '\u2803', 'c': '\u2809', 'd': '\u2819',
    'e': '\u2811', 'f': '\u280B', 'g': '\u281B', 'h': '\u2813',
    'i': '\u280A', 'j': '\u281A', 'k': '\u2805', 'l': '\u2807',
    'm': '\u280D', 'n': '\u281D', 'o': '\u2815', 'p': '\u280F',
    'q': '\u281F', 'r': '\u2817', 's': '\u280E', 't': '\u281E',
    'u': '\u2825', 'v': '\u2827', 'w': '\u283A', 'x': '\u282D',
    'y': '\u283D', 'z': '\u2835', ' ': ' ',
}

TEXT_DICT = {v: k for k, v in BRAILLE_DICT.items()}

def text_to_braille(text):
    text = text.lower()
    braille_text = ''
    for char in text:
        braille_text += BRAILLE_DICT.get(char, '?')
    return braille_text

def braille_to_text(braille_str):
    text = ''
    for symbol in braille_str:
        text += TEXT_DICT.get(symbol, '?')
    return text

# # --- TESTING ---
# sample_text = "naveen vayilapalli"
# braille = text_to_braille(sample_text)
# decoded = braille_to_text(braille)

# print("Original Text:", sample_text)
# print("To Braille:", braille)
# print("Back to Text:", decoded)

while True:
    choice = input("b for braille, t for text, q to quit: ")
    if choice == 'b':
        text = input("Enter text: ")
        print("Braille:", text_to_braille(text))
    elif choice == 't':
        braille = input("Enter braille: ")
        print("Text:", braille_to_text(braille))
    elif choice == 'q':
        break
    else:
        print("Invalid choice. Please enter 'b', 't', or 'q'.")

