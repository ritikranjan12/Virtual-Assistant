import subprocess
import speech_recognition as sr
import webbrowser
import time
import datetime
import wikipedia
import wolframalpha
import pyttsx3
import os
import cv2
import pywhatkit as kit




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
        print("Listening.....")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print ("Recognizing....")
            print(f"you said:{statement}\n")

        except Exception as e:
            return "None"
        return statement

cheer()

if __name__ == '__main__':

    speak("I am Jarvis! Tell me how can I help you" )
    print("I am Jarvis! Tell me how can I help you")
    while True:
        statement = audio().lower()
        if statement == 0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('Jarvis is shutting down,Good bye')
            print('jarvis  is shutting down,Good bye')
            break

        elif "are you there" in statement:
            speak("i am here")

        elif 'open youtube' in statement:
            speak("What do you want to see on Youtube sir?")
            video = audio()
            kit.playonyt(video)
            time.sleep(3)

        elif 'open facebook' in statement:
            webbrowser.get().open("https://www.facebook.com")
            speak("facebook is open now")

        elif 'open stack overflow' in statement:
            webbrowser.get().open("https://www.stackoverflow.com")
            speak("stackoverflow is open now")

        elif 'open gmail' in statement:
            webbrowser.get().open("gmail.com")
            speak("Google Mail open now")


        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am Jarvis your personal assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time' 
                  'get top headline news from times of india and you can ask me computational or geographical questions too!,built by Ritik Ranjan')

        elif "open linkedin" in statement:
            webbrowser.get().open("https://linkedin.com")
            speak("Here is linkedin")


        elif 'news' in statement:
            news = webbrowser.get().open("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')


        elif "shutdown" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

        elif "notepad" in statement:
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)

        elif "open camera" in statement:
            capture = cv2.VideoCapture (0)
            while (True):
                ret, frame = capture.read (0)
                LUV = cv2.cvtColor (frame, cv2.COLOR_BGR2LUV)
                cv2.imshow ('VIDEO', LUV)
                if cv2.waitKey (1) & 0xFF == ord ('0'):
                    break

            capture.release ()
            cv2.destroyAllWindows ()
            time.sleep(3)


        elif "play music" in statement:
            music_dir = "C:\\Users\\Ritik\\OneDrive\\games"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))
            time.sleep (10)

        elif 'wikipedia' in statement:
            speak ('Searching Wikipedia...')
            query = statement.replace ("wikipedia", "")
            results = wikipedia.summary (query, sentences=2)
            speak ("According to Wikipedia")
            print (results)
            speak (results)

        elif "i want to know something" in statement:
            speak("What do you want to know sir?")
            question = statement
            app_id = "X4L38Q-RKHH3972QG"
            client = wolframalpha.Client ('X4L38Q-RKHH3972QG')
            res = client.query (question)
            answer = next (res.results).text
            speak (answer)
            print (answer)

time.sleep(3)
