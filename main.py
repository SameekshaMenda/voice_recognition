import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak the recognized text
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech in a loop
def recognize_speech_loop():
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        while True:
            print("\nListening... Please say something:")
            try:
                # Listen to the audio
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
                # Use Google Web API to recognize speech
                text = recognizer.recognize_google(audio).strip()
                if text:
                    print(f"You said: {text}")
                    speak_text(text)
            except sr.UnknownValueError:
                # Handle cases where speech wasn't understood
                print("Sorry, muje samaj nahi ayya.")
                speak_text("Sorry, muje samaj nahi ayya.")
            except sr.WaitTimeoutError:
                # Handle timeout scenarios to avoid unnecessary waits
                print("Listening timed out.")
            except sr.RequestError as e:
                # Handle issues connecting to the speech API
                print(f"Could not request results; {e}")
                speak_text(f"Could not request results; {e}")

# Run the speech recognition loop
recognize_speech_loop()
