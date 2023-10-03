import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
        try:
            print("recognizing...")
            data=recognizer.recognize_google(audio)
            return data
        except sr.UnknownValueError:
            print("not understanding")
            
def speechtx(x):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate=engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()
    
if __name__ == '__main__':
        data1=sptext().lower()
        if "your name" in data1:
            name="my name is peter"
            speechtx(name)
        elif "old are you" in data1:
            age="i am two years old"
            speechtx(age)
        elif 'now time' in data1:
            time=datetime.datetime.now().strftime("%I%M%p")
            speechtx(time)
        elif "youtube" in data1:
            webbrowser.open("https://www.youtube.com/watch?v=N-iO1tDmP1A&list=PLjVLYmrlmjGfAUdLiF2bQ-0l8SwNZ1sBl&index=6")
        elif "joke" in data1:
            joke_1=pyjokes.get_joke(language="en",category="neutral")
            speechtx(joke_1)
        elif 'play song' in data1:
            add="addres of song"
            listsong=os.listdir(add)
            print(listsong)
            os.startfile(os.path.join(add,listsong[0]))

