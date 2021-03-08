import subprocess
import speech_recognition as sr
import webbrowser
import time
import datetime
import wolframalpha
import pyttsx3


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[0].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()


def cheer():
    hour = datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    elif hour>=23 and hour<24:
        speak("Hello, its too late Good night you can sleep now")
        print("Hello Good Night You can sleep now!")
        exit()
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

def audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"you said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement


speak("Loading your AI personal assistant M1900")
print("Loading your AI personal assistant M1900")
cheer()

if __name__ == '__main__':

    speak("Tell me how can I help you now?" )
    while True:
        statement = audio().lower()
        if statement == 0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant M1900 is shutting down,Good bye')
            print('your personal assistant M1900  is shutting down,Good bye')
            break

        elif "are you there" in statement:
            speak("i am here")

        elif 'open youtube' in statement:
            webbrowser.get().open("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(3)

        elif 'open google' in statement:
            webbrowser.get().open("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(3)

        elif 'open gmail' in statement:
            webbrowser.get().open("gmail.com")
            speak("Google Mail open now")
            time.sleep(3)

        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am M1900 version 1 point O your persoanl assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time' 
                  'get top headline news from times of india and you can ask me computational or geographical questions too!')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Ritik Ranjan")
            print("I was built by Ritik Ranjan")

        elif "open linkedin" in statement:
            webbrowser.get().open("https://linkedin.com")
            speak("Here is linkedin")

        elif 'news' in statement:
            news = webbrowser.get().open("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif "shutdown" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

        elif "answer" in statement:
            speak("i can answer to your question.")
            question = audio()
            app_id = "X4L38Q-RKHH3972QG"
            client = wolframalpha.Client('X4L38Q-RKHH3972QG')
            res = client.query (question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
            time.sleep(3)


time.sleep(3)
