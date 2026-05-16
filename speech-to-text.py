"""
Speech Recognition using Microphone
-----------------------------------
This program listens through the microphone
and converts speech into text using Google Speech API.
"""

# Import library
import speech_recognition as sr


# Create recognizer object
recognizer = sr.Recognizer()


# Access microphone
with sr.Microphone() as source:

    print("Adjusting for background noise...")

    # Reduce noise effect
    recognizer.adjust_for_ambient_noise(source, duration=1)

    print("Speak something...")
    
    # Listen from microphone
    audio = recognizer.listen(source)

    print("Processing...")


# Convert speech to text
try:

    text = recognizer.recognize_google(audio)

    print("\nYou said:")
    print(text)

except sr.UnknownValueError:

    print("Could not understand audio")

except sr.RequestError:

    print("Internet connection issue")