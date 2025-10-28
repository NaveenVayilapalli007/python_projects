# Databricks notebook source
# Morse code dictionary
MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': '.......',  # Use ...... for space between words
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--'
}

def text_to_morse(text):
    """Convert text to Morse code."""
    morse = ""
    for char in text:
        upper_char = char.upper()
        if upper_char in MORSE_CODE:
            morse += MORSE_CODE[upper_char] + " "
        else:
            morse += "? "  # Unknown character placeholder
    return morse.strip()

def morse_to_text(morse):
    """Convert Morse code to text."""
    text = ""
    morse_words = morse.split(" ")
    for morse_word in morse_words:
        for char, morse_code in MORSE_CODE.items():
            if morse_code == morse_word:
                text += char
                break
        else:
            text += "?"
    return text

# morse = input("Enter Morse code: ")
# print("Text:", morse_to_text(morse))

# # Input from user
# text = input("Enter text: ")
# print("Morse Code:", text_to_morse(text))

while True:
    input_choice = input("Enter 'm' to convert Morse code to text, or 't' to convert text to Morse code, or e to exit")
    if input_choice == 'm':
        morse = input("Enter Morse code: ")
        print("Text:", morse_to_text(morse))
    elif input_choice == 't':
        text = input("Enter text: ")
        print("Morse Code:", text_to_morse(text))
    elif input_choice == 'e':
        break
    else:
        print("Invalid input. Please enter 'm', 't', or 'e'.")

# COMMAND ----------

# optimized version of above code
# Morse Code Translator (Text ↔ Morse)

MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    ' ': '/'  # standard word separator in Morse
}

REVERSE_MORSE = {v: k for k, v in MORSE_CODE.items()}

def text_to_morse(text):
    return ' '.join(MORSE_CODE.get(char.upper(), '?') for char in text)

def morse_to_text(morse):
    return ''.join(REVERSE_MORSE.get(code, '?') for code in morse.split())

while True:
    choice = input("\nEnter 't' for Text→Morse, 'm' for Morse→Text, or 'e' to Exit: ").lower()
    
    if choice == 't':
        text = input("Enter text: ")
        print("Morse Code:", text_to_morse(text))
    elif choice == 'm':
        morse = input("Enter Morse code: ")
        print("Text:", morse_to_text(morse))
    elif choice == 'e':
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid input. Please enter 't', 'm', or 'e'.")


# COMMAND ----------

import numpy as np
from IPython.display import Audio, display
import time

# Morse code dictionary
MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': '.......',  # Use ...... for space between words
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--'
}

# Audio and timing configuration
FREQ = 700        # tone frequency (Hz)
DOT_DURATION = 0.1  # seconds
DASH_DURATION = DOT_DURATION * 3
SAMPLE_RATE = 44100  # Hz
SILENCE_UNIT = DOT_DURATION  # 1 unit of silence

def tone(duration):
    """Generate a sine wave tone for the given duration."""
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
    wave = np.sin(FREQ * 2 * np.pi * t)
    return wave

def silence(duration):
    """Generate silence for the given duration."""
    return np.zeros(int(SAMPLE_RATE * duration))

def text_to_morse_audio(text):
    """Convert text to Morse code and generate audio data."""
    audio_sequence = np.array([], dtype=np.float32)
    
    for char in text.upper():
        if char == ' ':
            # Word gap = 7 units
            audio_sequence = np.concatenate((audio_sequence, silence(SILENCE_UNIT * 7)))
            continue
        
        code = MORSE_CODE.get(char)
        if not code:
            continue
        
        for symbol in code:
            if symbol == '.':
                audio_sequence = np.concatenate((audio_sequence, tone(DOT_DURATION)))
            elif symbol == '-':
                audio_sequence = np.concatenate((audio_sequence, tone(DASH_DURATION)))
            # Space between parts of same letter (1 unit)
            audio_sequence = np.concatenate((audio_sequence, silence(SILENCE_UNIT)))
        
        # Space between letters (3 units)
        audio_sequence = np.concatenate((audio_sequence, silence(SILENCE_UNIT * 3)))
    
    # Normalize volume
    audio_sequence = audio_sequence * 0.5
    return audio_sequence

# Get user input
text = input("Enter text to play as Morse code: ")
morse = ' '.join(MORSE_CODE.get(ch.upper(), '') for ch in text)
print(f"Morse Code: {morse}")

# Generate and play audio
audio_data = text_to_morse_audio(text)
display(Audio(audio_data, rate=SAMPLE_RATE))
