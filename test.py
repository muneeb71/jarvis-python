
from tkinter import Tk, StringVar, PhotoImage, Button, Label
import PIL.Image
import PIL.ImageTk
import pyttsx3
from datetime import datetime
import speech_recognition as sr
from PIL import Image
import threading


numbers = {'hundred': 100, 'thousand': 1000, 'lakh': 100000}
a = {'name': 'your email'}
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

window = Tk()

global var
global var1
var = StringVar()
var1 = StringVar()



def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")


def chat():

    while True:
        from DataBase.ChatBot.ChatBot import ChatterBot
        query = TakeCommand()

        if 'exit' in query:
            Speak('Returning To Main Menu.')
            break
        else:
            Query = query.replace("Hello jarvis", "")
            Query = query.replace("chatbot", "")
            print(Query)

            reply = ChatterBot(Query)
            Speak(reply)


def menu():
    wishme()
    btn0.configure(bg='orange')
    while True:
        Speak("Initiate Task Execution or Chatbot")
        query = TakeCommand()

        if 'task' in query:
            Speak("Task Execution in process. Please Speak A Command")
            TaskExe()
        elif 'chatbot' in query:
            Speak("Please Speak A Command To Interact")
            chat()
        else:
            if 'terminate' in query:

                window.destroy()

                break

            elif 'exit' in query:
                window.destroy()
                break

            elif 'go' in query:
                window.destroy()
                break


def wishme():

    hour = datetime.now().hour
    print(hour)
    if (hour >= 6) and (hour < 12):
        Speak(f"Good Morning Sir")
    elif (hour >= 12) and (hour < 16):
        Speak(f"Good afternoon Sir")
    elif (hour >= 16) and (hour < 24):
        Speak(f"Good Evening Sir")
    Speak(f"I am 2.6CGPA Assistant.")


def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(": Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print(": Recognizing...")
            query = r.recognize_google(audio, language='en-us')
            print(f": Your Command : {query}\n")
            var.set(query)
        except:
            return ""
        return query.lower()


def TaskExe():

    while True:
        query = TakeCommand()
        if 'google search' in query:
            from Features import GoogleSearch
            GoogleSearch(query)
        elif 'youtube search' in query:
            Query = query.replace("jarvis", "")
            query = Query.replace("youtube search", "")
            from Features import YouTubeSearch
            YouTubeSearch(query)
        elif 'set alarm' in query:
            from Features import Alarm
            Alarm(query)
        elif 'download' in query:
            from Features import DownloadYouTube
            DownloadYouTube()
        elif 'speed test' in query:
            from Features import SpeedTest
            SpeedTest()
        elif 'whatsapp message' in query:
            name = query.replace("whatsapp message", "")
            name = name.replace("send ", "")
            name = name.replace("to ", "")
            Name = str(name)
            Speak(f"Whats The Message For {Name}")
            MSG = TakeCommand()
            from Automations import WhatsappMsg
            WhatsappMsg(Name, MSG)
        elif 'call' in query:
            from Automations import WhatsappCall
            name = query.replace("call ", "")
            name = name.replace("jarvis ", "")
            Name = str(name)
            WhatsappCall(Name)
        elif 'show chat' in query:
            Speak("With Whom ?")
            name = TakeCommand()
            from Automations import WhatsappChat
            WhatsappChat(name)
        elif 'space news' in query:
            Speak("Tell Me The Date For News Extracting Process .")
            Date = TakeCommand()
            from Features import DateConverter
            Value = DateConverter(Date)
            from Nasa import NasaNews
            NasaNews(Value)
        elif 'mars images' in query:
            from Nasa import MarsImage
            MarsImage()
        elif 'near earth' in query:
            from Features import DateConverter
            from Nasa import Astro
            Speak("Tell Me The Starting Date .")
            start = TakeCommand()
            start_date = DateConverter(TakeCommand)
            Speak("And Tell Me The End Date .")
            end = TakeCommand()
            end_date = DateConverter(end)
            Astro(start_date, end_date=end_date)
        elif 'my location' in query:
            from Features import My_Location
            My_Location()
        elif 'where is' in query:
            from Automations import GoogleMaps
            Place = query.replace("where is ", "")
            Place = Place.replace("jarvis", "")
            GoogleMaps(Place)
        elif 'online' in query:
            from Automations import OnlinClass
            Speak("Tell Me The Name Of The Class .")
            Class = TakeCommand()
            OnlinClass(Class)
        elif 'write a note' in query:
            from Automations import Notepad
            Notepad()
        elif 'dismiss' in query:
            from Automations import CloseNotepad
            CloseNotepad()
        elif 'time table' in query:
            from Automations import TimeTable
            TimeTable()
        elif 'corona cases' in query:
            from Features import CoronaVirus
            Speak("Which Country's Information ?")
            cccc = TakeCommand()
            CoronaVirus(cccc)
        elif 'chrome' in query:
            from Automations import ChromeAuto
            Speak("What To do Sir?")
            command = TakeCommand()
            ChromeAuto(command)
        elif 'auto youtube' in query:
            from Automations import YouTubeAuto
            Speak("What To do Sir?")
            command = TakeCommand()
            YouTubeAuto(command)
        elif 'windows' in query:
            from Automations import WindowsAuto
            Speak("What To do Sir?")
            command = TakeCommand()
            WindowsAuto(command)
        elif 'terminate' in query:
            Speak('Returning To Main Menu.')
            break
        else:
            Speak('Sorry. Could not get you. Can you Speak Again?')
            break


def update(ind):
    frame = frames[(ind) % 100]
    ind += 1
    label.configure(image=frame)
    window.after(100, update, ind)


label2 = Label(window, textvariable=var1, bg='#FAB60C')
label2.config(font=("Courier", 20))
var1.set('User Said:')
label2.pack()

label1 = Label(window, textvariable=var, bg='#ADD8E6')
label1.config(font=("Courier", 20))
var.set('Welcome')
label1.pack()

frames = [PhotoImage(file='Assistant.gif', format='gif -index %i' % (i))
          for i in range(100)]
window.title('JARVIS')

label = Label(window, width=500, height=500)
label.pack()
window.after(0, update, 0)

btn0 = Button(text='START', width=20, command=lambda: threading.Thread(
    target=menu).start(), bg='#5C85FB')
btn0.config(font=("Courier", 12))
btn0.pack()
# btn1 = Button(text = 'PLAY',width = 20,command = lambda: threading.Thread(target=TaskExe).start(), bg = '#5C85FB')
# btn1.config(font=("Courier", 12))
# btn1.pack()
# btn3 = Button(text = 'CHATBOT',width = 20, command = lambda: threading.Thread(target=chat).start(), bg = '#5C85FB')
# btn3.config(font=("Courier", 12))
# btn3.pack()
btn2 = Button(text='EXIT', width=20, command=window.destroy, bg='#5C85FB')
btn2.config(font=("Courier", 12))
btn2.pack()


window.mainloop()
