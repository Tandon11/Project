# pyttsx3 is a text-to-speech conversion library in Python.
# Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3.

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import requests
import json
import time
import pyautogui
import pymysql
import pygame as py
import random
import math
from aigui import *

obj1 = gui()
obj1.start()

engine = pyttsx3.init('sapi5')              # object creation, The Speech Application Programming Interface or SAPI is an API developed
                                            # by Microsoft to allow the use of speech recognition and speech synthesis within Windows applications.

voices = engine.getProperty("voices")       # getting deatils of current speaking voices                                             #print(voices[0].id) It will all voices available in syste, We only have female voice Zira
engine.setProperty('voice' , voices[1].id)  # setting up a new voice voices[0]

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour <= 16:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Hazel at your service")
    speak("How may i help you")

def speak(audio):
    gui.wave = False
    gui.circle = True
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    '''
    It takes microphone input from user and returns string output and for converting speech to text it requires internet
    '''

    gui.wave = True
    gui.circle = False
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 0.8    # kitna tej bole yaha se control hoga
        r.adjust_for_ambient_noise(source , duration=1)
        r.non_speaking_duration = 0.3
        audio = r.listen(source)  # It listens what ever we say


    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print("User Said : ", query)

    except Exception as e:
        print(e)
        print("Say that Again Please....")
        speak("Say that Again Please....")
        return "None"
    return query

def yourself():
    speak("Hi i am Hazel ")
    print("Hi i am Hazel ")
    speak("I am Your Personal Assistant ")
    print("I am Your Personal Assistant ")
    speak("I was Dervelped in Python ")
    print("I was Dervelped in Python ")
    speak("I was developed by Mr. Abhishekh Tandon and Mr. Vaibhav Biturwar and Mr.Setu Jha ")
    print("I was developed by Mr. Abhishekh Tandon and Mr. Vaibhav Biturwar and Mr.Setu Jha ")
    speak("I am currently in my development stage ")
    print("I am currently in my development stage ")
    speak("My first version was released on 19th of july ")
    print("My first version was released on 19th of july ")
    speak("There are various modules combined to present my presence ")
    print("There are various modules combined to present my presence ")
    speak("some of which include p y t t s x 3  , speech recognition , py game  , and many more ")
    print("some of which include p y t t s x 3  , speech recognition , py game  , and many more ")
    speak("I will be at my  100 % to help you ")
    print("I will be at my  100 % to help you ")

def what_can_you_do():
    speak("I can send E-mail to any of your friend, colleague")
    speak("I can get you the daily headlines when requested")
    speak("I am also able to capture your entire screen")
    speak("I can search all images you want")
    speak("I can get you the weather updates")
    speak("When you are upset I can put up a smile on your face with my jokes")
    speak("I am also capable of converting values from one unit to the other")
    speak("When you are bored i can refresh you with my snake game")

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Sender-Email', 'password')
    server.sendmail('Sender-Email',to , content)
    server.close()

def newsfromBBC():
    # BBC news API
    main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=a05cf53c56bf4c0882db52aed506e3bc"

    # Fetching Data in Json format
    open_page = requests.get(main_url).json()

    # Gettting all articles in a string article
    article = open_page["articles"]

    # Empty list which will contain all trending news
    results = []

    for ar in article:
        results.append(ar["title"])
    speak('The headlines are')

    for i in range(len(results)):

        # Print all trending news
        print(i + 1, results[i])
        speak(results[i])

t = time.localtime()
timestamp = time.strftime('%b-%d-%Y_%H%M', t).lower()
filename = 'Screenshot' + timestamp + '.jpeg'

def capture():
    # Takes screenshot
    img = pyautogui.screenshot()

    # Save the image
    img.save("G:\\Python Training 2019\\Hazel\\Screenshot\\" + filename)

    # Show the image
    # img.show()

def imgsearch(text):
    urlp = "https://www.google.com/search?hl=en&tbm=isch&source=hp&biw=1745&bih=861&ei=bVgwXcSvKMzUvASsvr24BQ&q="+text
    urlm = urlp+"&oq="+text+"&gs_l=img.3..0l10.6121.7120..7308...0.0..0.242.1136.2j5j1......0....1..gws-wiz-img.....0..35i39.IvSjTlBizUM&ved=0ahUKEwiEmr2Kr77jAhVMKo8KHSxfD1cQ4dUDCAU&uact=5"
    webbrowser.open(urlm)

def weather(text):
    try:
        main_url = "http://api.openweathermap.org/data/2.5/weather?q="+text+",in&appid=6084135645af283cc622078dcddff59b"
        open_page = requests.get(main_url).json()

        condition = open_page['weather'][0]['description']  # weather condition in string
        temp = str(round(open_page['main']['temp'] - 273.165)) + 'degree celsius'  # temp in C
        pressure = str(open_page['main']['pressure']) + 'milli Bar'  # pressure in mBar
        humidity = str(open_page['main']['humidity']) + 'percent'  # humidity in percentage %
        wind_speed = str(open_page['wind']['speed']) + 'meter per second'  # wind speed in m/s
        wind_angle = str(open_page['wind']['deg']) + 'degree'  # angle of wind

        print(f"Weather at {text.capitalize()} is as follows")
        speak(f"Weather at   {text} is as follows")

        print(f"Condition       {condition}")
        speak(f"condition       {condition}")

        print(f"Temperature     {temp}")
        speak(f"Temperature     {temp}")

        print(f"Pressure        {pressure}")
        speak(f"Pressure        {pressure}")

        print(f"Humidity        {humidity}")
        speak(f"Humidity        {humidity}")

        print(f"Wind Speed      {wind_speed}")
        speak(f"Wind Speed      {wind_speed}")

        print(f"At an Angle of  {wind_angle}")
        speak(f"At an Angle of  {wind_angle}")

        database_weather(condition, temp, pressure, humidity, wind_speed, wind_angle, text)



    except Exception as e:
        print("Sorry! Connection Failed - Please try again ")
        speak("Sorry ")
        speak("connection Failed Please try again")


def say_joke():
    main_url = "http://api.icndb.com/jokes/random"
    open_page = requests.get(main_url).json()
    joke = open_page["value"]["joke"]
    print(f"Joke : {joke}")
    speak(joke)

def converter(text):
    if "convert" in text:
        text = text.split(" ")
        text = "+".join(text[1:])
        urlp = 'https://www.google.com/search?ei=sqExXYyiCtTVz7sPt8y9kAc&q='
        urlm = '&oq='
        urls = '&gs_l=psy-ab.3..0j0i22i30l9.1636.9226..9363...2.0..0.395.4581.0j11j5j4....2..0....1..gws-wiz.....10..35i39j0i67j0i131j0i20i263.GsXvyMxzL-0'
        url = urlp + text + urlm + text + urls
        print(url)
        webbrowser.open(url)

def snake():
    x = py.init()

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 155, 0)
    BLUE = (0, 0, 255)
    canvas_w, canvas_h = 800, 600

    canvas = py.display.set_mode([canvas_w, canvas_h])
    py.display.set_caption("Slither")

    speed = 15
    size = 10
    change = 10
    applesize = 10

    font = py.font.SysFont(None, 25)

    def display_messsage(msg, color):
        message = font.render(msg, True, color)
        canvas.blit(message, [canvas_w / 2, canvas_h / 2])
        py.display.update()

    def print_snake(snakelist, size):
        for val in snakelist:
            canvas.fill(GREEN, rect=[val[0], val[1], size, size])

    def game_loop():
        play = True
        gameover = False
        head_x = canvas_w / 2
        head_y = canvas_h / 2
        change_x = 0
        change_y = 0
        score = 1
        clock = py.time.Clock()
        snakelist = []

        applex = random.randint(30, canvas_w - 30)
        applex = round(applex / 10.0) * 10.0
        appley = random.randint(30, canvas_h - 30)
        appley = round(appley / 10.0) * 10.0

        count = 1
        while play:

            while gameover == True:
                display_messsage("Game Over! Press C to continue and Q to exit", RED)
                if count == 1:
                    speak("Game Over")
                    speak("Your score is")
                    speak(score)
                    count += 1
                    database_snake(score)

                for event in py.event.get():
                    if event.type == py.KEYDOWN:
                        if event.key == py.K_q:
                            play = False
                            gameover = False
                        elif event.key == py.K_c:
                            gameover = False
                            game_loop()
                    elif event.type == py.QUIT:
                        print("Quit")
                        play = False
                        gameover = False

            for event in py.event.get():
                if event.type == py.QUIT:
                    print("Quit")
                    play = False
                elif event.type == py.KEYDOWN:
                    if event.key == py.K_LEFT:
                        change_x = -change
                        change_y = 0

                    elif event.key == py.K_RIGHT:
                        change_x = change
                        change_y = 0

                    elif event.key == py.K_UP:
                        change_y = -change
                        change_x = 0

                    elif event.key == py.K_DOWN:
                        change_y = change
                        change_x = 0

            if head_x > canvas_w - 29 or head_y > canvas_h - 29 or head_y <= 15 or head_x <= 15:
                gameover = True

            background_image = py.image.load("BG.jpg").convert()
            canvas.blit(background_image, [0, 0])
            head_x += change_x
            head_y += change_y
            canvas.fill(RED, rect=[applex, appley, applesize, applesize])

            snakehead = []
            snakehead.append(head_x)
            snakehead.append(head_y)
            snakelist.append(snakehead)
            if len(snakelist) > score:
                del snakelist[0]

            for eachsegment in snakelist[:-1]:
                if eachsegment == snakehead:
                    gameover = True

            print_snake(snakelist, size)
            py.display.update()

            if head_x == applex and head_y == appley:
                applex = random.randint(30, canvas_w - 30)
                applex = round(applex / 10.0) * 10.0
                appley = random.randint(30, canvas_h - 30)
                appley = round(appley / 10.0) * 10.0
                score += 1

            clock.tick(speed)

        py.quit()
        # quit()
        return 0

    game_loop()
    return 0


def database(name, age, gender, hobbies, qualification, favfood):

    try:
        conn = pymysql.connect(host="127.0.0.1", user="root", passwd='', db='my_python') # creates connection object

        mycursor = conn.cursor()  # It will allow to fire SQL Query

        url = "INSERT INTO information (Name, Age, Gender, Hobbies, Qualification, Favfood) VALUES('"+name+"','"+age+"','"+gender+"','"+hobbies+"','"+qualification+"','"+favfood+"')"
        mycursor.execute(url)
        print()
        # Fires Query

        conn.commit()  # Save changes in Mysql
    except Exception as e:
        print(e)
    finally:
        speak("Thankyou for the co-operation")
        conn.close()

def database_snake(score):

    print(type(score))
    try:
        conn = pymysql.connect(host="127.0.0.1", user="root", passwd='', db='my_python') # creates connection object
        mycursor = conn.cursor()  # It will allow to fire SQL Query
        score = str(score)

        url12 = "INSERT INTO snake (score) VALUES("+score+")"

        mycursor.execute(url12)

        # Fires Query

        conn.commit()  # Save changes in Mysql
    except Exception as e:
        print(e)
    finally:
        conn.close()

def database_weather(condition, temp, pressure, humidity, wind_speed, wind_angle, place):
    try:

        conn = pymysql.connect(host="127.0.0.1", user="root", passwd='', db='my_python')  # creates connection object
        mycursor = conn.cursor()  # It will allow to fire SQL Query

        date = datetime.datetime.now()
        date = str(date)

        url2 = "INSERT INTO weather (conditions, temperature, pressure, humidity, speed, angle, datetime, place) VALUES('"+condition+"','"+temp+"','"+pressure+"','"+humidity+"','"+wind_speed+"','"+wind_angle+"','"+date+"','"+place+"')"
        mycursor.execute(url2)
        print()
        # Fires Query

        conn.commit()  # Save changes in Mysql
    except Exception as e:
        print(e)
    finally:
        conn.close()


if __name__ == '__main__':

    wish()

    while True:
        query = takecommand().lower() # We are converting the query in lower while searching any word we pass it in lower case
        #Logic to execute tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', "") # replace wikipedia in query with null string
            results = wikipedia.summary(query, sentences=2) # It will only fetch 2 sentences from wikipedia
            speak('According to wikipedia...')
            speak(results)

        elif 'surfing' in query:
            speak("Sure but please tell me want you want to search")
            text = takecommand().lower()
            if "youtube" in text:
                text = text.replace('search', "")
                text = text.replace("youtube", "")
                text = text.split(" ")
                text = "+".join(text[4:])
                url = 'https://www.youtube.com/results?search_query='
                url = url + text
                print(url)
                webbrowser.open(url)

            elif "search" in text:
                text = text.replace('search', "").split(" ")
                text = "+".join(text[1:])
                urlp = 'https://www.google.com/search?source=hp&ei=txgvXfO1Cov_vAT_9oq4Dg&q='
                urlm = '&oq='
                urls = '&gs_l=psy-ab.3..0j0i22i30l9.1636.9226..9363...2.0..0.395.4581.0j11j5j4....2..0....1..gws-wiz.....10..35i39j0i67j0i131j0i20i263.GsXvyMxzL-0'
                url = urlp + text + urlm + text + urls
                print(url)
                webbrowser.open(url)

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open notepad plus plus' in query:
            path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Notepad++"
            os.startfile(path)

        elif 'pycharm' in query:
            path = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains\\JetBrains PyCharm Community Edition 2019.1.3'
            os.startfile(path)

        elif 'quickheal' in query:
            path = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Quick Heal Total Security\\Quick Heal Total Security'
            os.startfile(path)

        elif 'g drive' in query:
            path = "G:\\"
            os.startfile(path)

        elif 'c drive' in query:
            path = "C:\\"
            os.startfile(path)

        elif 'h drive' in query:
            path = "H:\\"
            os.startfile(path)

        elif 'play music' in query:
            music_dir = 'G:\\Songs'
            songs = os.listdir(music_dir) # It will list all the songs in our music directory
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0])) # It will play the first song we can use random number technique to play any random song

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S") # Gives the current time in given format in form of a string
            speak(f"Sir,the time is {strtime}")

        elif 'open notepad' in query:
            path = 'C:\\Users\\dell\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad'
            os.startfile(path)

        elif 'email to abhishek' in query:
            try:
                speak('What should I say?')
                content = takecommand()
                to = 'Reciever-Email'
                sendemail(to, content)
                speak("Your Email has been sent successfully")
            except Exception as e:
                print(e)
                speak("Sorry Sir I am unable to send your email")

        elif 'headlines' in query:
            newsfromBBC()

        elif 'capture' in query:
            capture()
            print("Sir your image has been captured successfully")
            speak("Sir your image has been captured successfully")
            speak("Do you want to see it")
            query = takecommand()
            if 'yes' in query:
                path = "G:\\Python Training 2019\\Hazel\\Screenshot\\" + filename
                os.startfile(path)

        elif 'search' in query:
            speak("Sure Sir tell me what you want to search")
            img = takecommand()
            imgsearch(img)

        elif 'weather' in query:
            speak("Tell me the place whose weather report you want")
            place = takecommand()
            weather(place)

        elif 'jokes' in query:
            speak("Get Ready you won't be able to control your laughter")
            say_joke()
            say_joke()
            say_joke()
            say_joke()

        elif 'convert' in query:
            speak("Welcome to SIRI's converter")
            converter(query)

        elif 'bored' in query:
            speak("Seems like you are free and relaxing")
            speak("Well I have something interesting for you a snake game")
            gui.running = False
            snake()
            gui.running = True

        elif 'yourself' in query:
            yourself()

        elif 'what can you do' in query:
            speak("Sure Sir I would be happy sharing details about me with you")
            what_can_you_do()

        elif 'my friend' in query:
            speak("Welcome friend How Are you?")
            speak("Could you help me with your name please...")
            name = 'None'
            age = 'None'
            gender = 'None'
            hobbies = 'None'
            qualification = 'None'
            favfood = 'None'

            speak("What is Your Name")
            print("Name")
            while name == 'None':
                name = takecommand()


            speak("I also keen to know you gender...")
            while gender == 'None':
                gender = takecommand()

            speak('What is your age')
            while age == 'None':
                age = takecommand()


            speak("I am also interested in knowing your hobbies")
            while hobbies == 'None':
                hobbies = takecommand()

            speak("Can you tell me something about your Qualifications..")
            while qualification == 'None':
                qualification = takecommand()

            speak("Lastly tell me something which food item you love to eat")
            while favfood == 'None':
                favfood = takecommand()
            print(name, age, gender, hobbies, qualification, favfood)

            database(name, age, gender, hobbies, qualification, favfood)

        elif 'exit' in query:
            exit()