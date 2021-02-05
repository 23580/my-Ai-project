import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes
import pyaudio
import webbrowser
import os



listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir ")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir")

    else:
        speak("Good Evening sir") 

    speak("I am Jarvis here. Please tell me how may I help you.")


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
    except:
        pass
    return command 


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        speak('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak('Sir,Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        speak(info)
    elif 'date' in command:
        speak('sorry sir, I have a headache')


    elif 'are you single' in command:
        speak('sorry sir! im in relationship with alexa')


    elif 'joke' in command:
        speak(pyjokes.get_joke())


    elif 'open youtube' in command:
        webbrowser.open("youtube.com")
        speak('opening youtube for you sir')


    elif 'open google' in command:
        webbrowser.open("google.com")
        speak('opening google for you sir')

    elif 'open gmail' in command:
        webbrowser.open("gmail.com")
        speak('opening gmail for you sir')    


    elif 'feeling so sad' in command:
        music_dir = 'C:\\Users\\91967\\Music\\Playlists\\'
        songs = os.listdir(music_dir)
        speak('playing songs in me to change your mood sir')
        os.startfile(os.path.join(music_dir, songs[0]))


    elif 'open vs code' in command:
            codePath = "C:\\Users\\91967\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak('opening visual code edtior sir!')


    elif 'hey jarvis' in command:
        speak('yes sir im here ,tell me ')

        
    else:
        speak('Please say the command again.')


if __name__ == "__main__":
    wishMe()
    while True: 
         run_alexa()