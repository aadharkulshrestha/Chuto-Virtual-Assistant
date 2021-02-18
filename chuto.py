import wolframalpha
import random
import pyttsx3
import pyjokes
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import googletrans
import smtplib 

gt = googletrans.Translator()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am chotu Sir. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:   
        speak("I can not understand that ! , You can ask questions like Send Email, Wikipedia, Opening Softwares, Playing music")
        print("Say that again please...")  
        return "None" 
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('aadharkulshrestha3150@gmail.com', '')
    server.sendmail('aadharkulshrestha3150@gmail.com', to, content)
    server.close()

app = wolframalpha.Client("KHKPPH-35PPJH3YX4")

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching on wiki")
            try:
                query = query.replace("Wikipedia", "")
                results = wikipedia.summary(query, sentences = 2)
                
                speak("so, wikipedia says")
                speak(results)
                
            except:
                speak("Not available on wikipedia")
         
        # for stoping/breaking the code
        if 'stop' in query or 'over' in query or 'bye' in query or 'quit' in query or 'see you' in query or 'go' in query:
            f = "bye sir", "ok bye sir", "see you again sir", "bye bye", "As your wish sir", "Waiting for Activation sir", "As your wish, but I dont want to go sir!"
            speak(random.choice(f))
            
            break
        
        # for opening Youtube
        elif 'open youtube' in query or 'play youtube' in query or 'play a video' in query or 'search on youtube' in query:
            dg = 'what should i search on youtube', 'what would you like to search on youtube', 'say the words you like to search on youtube'
            speak(random.choice(dg))
            x = takeCommand().lower()
            webbrowser.open(f"https://www.youtube.com/results?search_query={x}")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'recipe' in query or "want to make" in query:
            r = takeCommand().lower()
            webbrowser.open(f"https://www.youtube.com/results?search_query={r}")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'open white hat' in query or "whiteHat" in query:
            webbrowser.open("https://code.whitehatjr.com/s/dashboard")

        elif 'thanks' in query or 'thank you' in query or 'ok' in query:
            t = "It's my pleasure, sir", "Welcome", "Your Welcome, Boss!"
            speak(random.choice(t))

        elif 'name' in query:
            speak("You, Know My Name as you call me but i am telling once again ,  My name is Chuto  , I am your assistant . Please tell me how may I help you ")   

        elif 'temperature' in query or 'weathher' in query:
            res = app.query(query)
            speak(" i am getting the tempreature")
            speak(next(res.results).text 
        )
        elif 'calculate' in query:
            speak("what should i calculate?")
            gh = takeCommand().lower()
            res = app.query(gh)
            speak(next(res.results).text)
        
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        
        elif 'play music' in query:
            music_dir = 'F:\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
        
        elif "play bhajan" in query or 'play shri Ram' in query or 'shri Ram' in query:
            speak("Ok sir opening your favourite bhajan!")
            music_dir = 'F:\Music'
            songs = os.listdir(music_dir)
            print(songs) 
            os.startfile(os.path.join(music_dir, songs[3]))
       
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Aadha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to aadhar' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "deepakulshrestha13@gmail.com"
                sendEmail(to, content)
                print("Email has been sent!.,,.")
                speak("Email has been sent!")
            except Exception as e:
                print()
                speak("Sorry my friend aadhar. I am not able to send this email")
