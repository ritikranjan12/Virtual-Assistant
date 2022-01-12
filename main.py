import random
import instaloader
import pyautogui
import requests
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
import tkinter as tk
from tkinter import *




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[1].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def cheer():
    hour = datetime.datetime.now().hour
    strTime = time.strftime('%I:%M %p')

    if hour>=0 and hour<12:
        speak(f"Hello,Good Morning sir it's {strTime}")
    elif hour>=12 and hour<18:
        speak(f"Hello,Good Afternoon sir it's {strTime}")
    elif hour>23.6:
        speak(f"Hello, its {strTime} Good night  sir you can sleep now")
        exit()
    else:
        speak(f"Hello,Good Evening sir it's {strTime}")

def audio():
        r = sr.Recognizer ()
        with sr.Microphone () as source:
            audio = r.listen (source)

            try:
                statement = r.recognize_google (audio, language='en-in')  # en at hi for english

            except Exception as e:
                return "None"
            return statement

def main():

        speak ("sir am Jarvis ! Tell me how can I help you")

        while True:
            statement = audio ().lower ()
            if statement == 0:
                continue


            if "good bye" in statement or "ok bye" in statement or "stop" in statement:
                speak ('Jarvis is shutting down,Good bye')
                exit ()


            elif "are you there" in statement:
                speak ("i am here")


            elif 'open youtube' in statement:
                speak ("What do you want to see on Youtube sir?")
                video = audio ()
                kit.playonyt (video)
                time.sleep (3)


            elif 'open facebook' in statement:
                webbrowser.get ().open ("https://www.facebook.com")
                speak ("facebook is open now")


            elif "open instagram" in statement:
                webbrowser.get().open("https://www.instagram.com")
                speak("Instagram is open now")


            elif "open telegram" in statement:
                tpath = "C:\\Users\\Ritik\\OneDrive\\Telegram Desktop\\Telegram.exe"
                os.startfile(tpath)


            elif 'open stack overflow' in statement:
                webbrowser.get ().open ("https://www.stackoverflow.com")
                speak ("stackoverflow is open now")


            elif 'open gmail' in statement:
                webbrowser.get ().open ("gmail.com")
                speak ("Google Mail open now")


            elif 'who are you' in statement or 'what can you do' in statement:
                speak ('I am Jarvis your personal assistant. I am programmed to minor tasks like'
                       'opening youtube,google chrome,gmail and stackoverflow ,predict time'
                       'get top headline news from times of india and you can ask me computational or geographical questions too!,built by Ritik Ranjan')


            elif "open linkedin" in statement:
                webbrowser.get ().open ("https://linkedin.com")
                speak ("Here is linkedin")


            elif 'search' in statement:
                statement = statement.replace ("search", "")
                webbrowser.open_new_tab (statement)


            elif "shutdown" in statement or "sign out" in statement:
                speak ("Ok , your pc will log off  make sure you exit from all applications")
                subprocess.call (["shutdown", "/s"])


            elif "notepad" in statement:
                npath = "C:\\Windows\\System32\\notepad.exe"
                os.startfile (npath)


            elif "open camera" in statement:
                capture = cv2.VideoCapture (0)
                while (True):
                    ret, frame = capture.read (0)
                    cv2.imshow ('VIDEO', frame)
                    d = audio ().lower ()
                    if "close" in d:
                        break

                capture.release ()
                cv2.destroyAllWindows ()
                time.sleep (3)


            elif "play music" in statement:
                    music_dir = "C:\\Users\\Ritik\\OneDrive\\nfs\\song"
                    songs = os.listdir (music_dir)
                    speak("this is a random song sir")
                    a = random.randint (1, 100)
                    os.startfile (os.path.join (music_dir, songs[a]))


            elif 'wikipedia' in statement:
                speak ('Searching Wikipedia...')
                query = statement.replace ("wikipedia", "")
                results = wikipedia.summary (query)
                speak ("According to Wikipedia")
                print (results)
                speak (results)


            elif "i want to know something" in statement:
                speak ("What do you want to know sir?")
                question =audio ()
                app_id = "X4L38Q-RKHH3972QG"
                client = wolframalpha.Client ('X4L38Q-RKHH3972QG')
                res = client.query (question)
                answer = next (res.results).text
                speak (answer)
                print (answer)

            elif "reccord" in statement:
                def engine():
                    pg.keyDown("win")
                    pg.keyDown("alt")
                    pg.press("r")
                    pg.keyUp("alt")
                    pg.keyUp("win")

                speak('Screen Recording Started')
                engine()
                n=audio()
                if "stop" in n:
                    engine()
                    speak('Screen Recording Ended')
                    
            elif "send" in statement:
                speak ("What is the message sir?")
                message =audio ()
                kit.sendwhatmsg ("Mobile no.", message, hour, minute)


            elif "open desktop" in statement:
                speak ("You are on desktop sir...")
                d = "C:\\Users\\Ritik\\OneDrive\\Desktop"
                os.startfile (os.path.join (d))


            elif 'open website' in statement:
                speak ("which website sir ")
                d = audio().lower()
                webbrowser.get().open("https://" + d + ".com")
                speak("ok sir i will open " + d)


            elif "what is the temperature" in statement:

                BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
                speak ("where are you sir?...")
                city = audio ()
                api_key = "92bad23e10f926d81bd613de3a2c03b9"
                URL = BASE_URL + "q=" + city + "&appid=" + api_key
                response = requests.get (URL)
                if response.status_code == 200:
                    data = response.json ()
                    main = data ['main']
                    temperature = main ['temp'] - 273.15
                    t = round (temperature, 2)
                    weather_description = z[0]["description"]
                    speak (f"The temperature of {city} is {t} degree celcius")
                else:
                    speak ("can't find the city sir")


            elif "thanks jarvis" in statement:
                speak ("it's my pleasure sir...")


            elif "instagram profile" in statement:
                speak ("sir plesase enter the username correctly")
                name = "underrated_chap"
                webbrowser.open (f"https://www.instagram.com/{name}")
                speak (f"here is the profile pic of {name}")
                time.sleep (5)
                speak ("sir do you want to download the profile pic of this acount")
                d = audio ()
                if "yes" in d:
                    mod = instaloader.Instaloader ()
                    mod.download_profile (name, profile_pic_only=True)
                    speak ("Done sir profile pic is saved in our main file")
                else:
                    pass


            elif "take screenshot" in statement:
                speak ("tell me the name of this screenshot")
                name = audio ().lower ()
                speak ("please hold the screenshot for few seconds i am taking screenshot...")
                time.sleep (2)
                img = pyautogui.screenshot ()
                img.save (f"{name}.png")
                speak (f" Done sir screenshot has been saved as {name}.png")


            elif "jarvis" in statement:
                speak("yes sir tell me how can i help you")


            elif "increase volume" in statement:
                pyautogui.press("volumeup")


            elif "decrease volume" in statement:
                pyautogui.press("volumedown")


            elif "mute" in statement:
                pyautogui.press("volumemute")


            elif "hang on" in statement:
                speak ("okay sir ! i am going to sleep you can call me anytime")
                time.sleep (5)
                d1 = audio ().lower ()
                if "wake up" in d1:
                    start ()


def start():
    d = audio().lower()
    if "wake up" in d:
        cheer()
        main()
    elif "" in d:
        start()


root = Tk()

root.geometry("1300x800")

root.title("J.A.R.V.I.S")


# Add image file
bg = PhotoImage( file = "C:\\Users\\Ritik\\OneDrive\\nfs\\Bgm\\jarvis.gif")

# Show image using label
label1 = Label( root, image = bg)

label1.place(x = 0,y = 0)


bttn = tk.Button(text = 'RUN', command=start,fg = 'yellow',
                 bg = 'black',font = (("Times New Roman"),15))

bttn.place(x=100,y=70)

root.mainloop()
