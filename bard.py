import pyttsx3
import speech_recognition as sr
import os



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said : {query}")

    except Exception as e:
        speak("say that again!!!")
        return "none"
    return query

def wish():
    speak("Initializing system mainframe!! ")
    speak("Advancing voice recognition.")
    speak("super user privileges are disabled!!")


if __name__ == "__main__":
    wish()
    # # while True:
    if 1:
        query = takecommand().lower()
        #logic for tasks.
        # if "notepad" or "open notepad" or "text editor" in query:
        #     notepad = "C:\\Windows\\system32\\notepad.exe"
        #     speak("ADVANCING notepad!!!")
        #     os.startfile(notepad)
        if "chrome" or "open chrome" in query:
            chrome = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
            speak("ADVANCING chrome!!!")
            os.startfile(chrome)
        elif "VS code" or "open vs code" or "vscode" or "code editor" in query:
            vs_code = "C:\\Windows\\system32\\notepad.exe"
            speak("ADVANCING!!!")
            os.startfile(vs_code)
        elif "dc" or "open discord" or "discord" in query:
            dc = "C:\\Users\\user\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord.lnk"
            speak("ADVANCING!!!")
            os.startfile(dc)
        else:
            print("pata nahi")
        



