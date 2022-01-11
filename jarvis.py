from sys import exc_info
import pyttsx3
import datetime   #no need to install already present
import speech_recognition as sr   #to recognize what we say
import wikipedia
import webbrowser
import os
import smtplib  # for email


engine= pyttsx3.init('sapi5')   #to accept our voice
voices= engine.getProperty('voices')
#print(voices[1].id)    #for my pc voice[0]==boy   && voice[1]==girl
engine.setProperty('voice',voices[1].id)

def speak(audio):            #function to speak
    engine.say(audio)
    engine.runAndWait()

def wishme():               #function to wish and tell about him
    hour=int(datetime.datetime.now().hour)  #to get hour from 1-24
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I m jarvis mam. Please tell me how may i help you")

def takecommand():
    #it takes microphone input from user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1       #to know more about these functions just press 'ctrl + click'
        r.adjust_for_ambient_noise(source)
        audio= r.listen(source)

    try:
        print("Recognizing...")
        query= r.recognize_google(audio , language='en-in')   #en-in==indian english
        print("User said : {query}\n")  #f-string

    except Exception as e:        #if our voice is not recognized
        #print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("yourmail@gmail.com","abc")
    server.sendmail("yourmail@gmail.com",to,content)
    server.close()

if __name__=="__main__" :
    #speak("Hello everyone")
    wishme()
    while True:
       query=takecommand().lower()
    #logic for executing tasks based on query
       if 'wikipedia' in query:
           speak('searching wikipedia...')
           query=query.replace("wikipedia","")
           results=wikipedia.summary(query,sentences=2)
           speak("According to wikipedia")
           print(results)
           speak(results)

       elif 'open youtube' in query:
            webbrowser.open("youtube.com")

       elif 'open google' in query:
            webbrowser.open("google.com")

       elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

       elif 'play music' in query:
            music_dir = 'C:\\Users\\Moti Beker\\Music\\papa ke songs'
            songs= os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

       elif 'the time' in query:
           strTime= datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"The time is {strTime}")

       elif 'open code' in query:
           codepath= "D:\\Microsoft VS Code\\Code.exe"
           os.startfile(codepath)

       elif 'email to abc' in query:
           try:
               speak("what should i say?")
               content=takecommand()
               to="yourmail@gmail.com"
               sendEmail(to,content)
               speak("Email has been sent")

           except Exception as e:
               print(e)
               speak("sorry mam i am not able to send Email")


