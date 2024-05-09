import pyttsx3
import speech_recognition as sr
import webbrowser

def start_speech_recognition():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        handle_response(text)
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    start_speech_recognition()

def handle_response(text):
    if 'hello' in text.lower():
        reply = "Hi! Welcome to Vision Voice. Which website would you like to go to?"
        print(reply)
        text_to_speech(reply)
    elif 'maths is fun' in text.lower():
        print("Opening mathsisfun website...")
        webbrowser.open_new_tab("https://www.mathsisfun.com/")
    elif 'aux notes' in text.lower() or 'ox notes' in text.lower():
        print("Opening aux notes website...")
        webbrowser.open_new_tab("https://www.oxnotes.com/igcse-mathematics.html")
    elif 'mathplanet' in text.lower() or 'math planet' in text.lower():
        print("Opening mathplanet website...")
        webbrowser.open_new_tab("https://www.mathplanet.com/")
    elif 'math notes' in text.lower() or 'mathnotes' in text.lower() or 'maths notes' in text.lower():
        print("Opening math notes website...")
        webbrowser.open_new_tab("https://tutorial.math.lamar.edu/Classes/Alg/Alg.aspx")

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    start_speech_recognition()
