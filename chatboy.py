import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
import pyowm
import smtplib
import pyautogui

engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print(voices[10])
engine.setProperty('voices',voices[10])

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("listening . . .")
        audio = r.listen(source,timeout=10)
    try:
        print("recognising . . .")
        query = r.recognize_google(audio,language='en-in')
        print(f"USER: {query}\n") 
    except Exception as e:
        print(e)
        print("speak again .")
        return "None"
    return query

def sendemail(to,msg):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("yourid@gmail.com","yourpassword")
    server.sendmail("yourid@gmail.com", to, msg)
    server.close()
    


if __name__ == "__main__":
    speak("yo dog what up?")
    while True:
        querry= takecommand().lower()
        
        if 'wikipedia' in querry:
            speak("searching that on wikipedia.")
            querry = querry.replace("wikipedia","")
            result = wikipedia.summary(querry,sentences =1)
            speak("according to wikipedia")
            speak(result)
            
        elif 'youtube' in querry:
            speak("here we go to to youtube.com")
            webbrowser.open("https://www.youtube.com/")
        elif 'play music' in querry:
            speak("lets listen some music.")
            webbrowser.open("https://www.youtube.com/watch?v=d-JBBNg8YKs")
        elif 'the time' in querry:
            stime = datetime.datetime.now().strftime("%H:%M %p")
            speak(f"it's {stime}.")
            
        elif "weather" in querry:
            owm =pyowm.OWM('c31ac708d107fc2df2a90219b9725f0f')
            mgr = owm.weather_manager()
            speak("which city")
            place = takecommand()
            obv = mgr.weather_at_place(place)
            w = obv.weather
            temo = w.temperature('celsius')
            speak(f"it's {temo['temp']}degree celsius in {place} right now.")
             
        elif "send an email to ___" in querry:
            try:
                speak("alright say what you wanna say to ___")
                msg = takecommand()
                to = "RECIVERID@gmail.com"
                sendemail(to,msg)
                speak("email has been sent.")
                print("email has been sent.")
            except Exception(e):
                print(e)
                speak("sorry i was unable to send an email please try again.")
             
        elif "pause music" in querry:
            pyautogui.keyDown("space")
            
        elif "shutdown" in querry:
            speak("signing out take care stay safe from covid!")
            break