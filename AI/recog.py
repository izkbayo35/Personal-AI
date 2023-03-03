import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
#
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
#
#
def talk(text):
    engine.say(text)
    engine.runAndWait()
#pip
#
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Hey I am Listening ')
        r.adjust_for_ambient_noise(source, duration=2)
        audio = r.listen(source)
    try:
        print("Trying to process the audio...")
        command=r.recognize_google(audio)
        command = command.lower()
        print(command,"+++_______-")
        if 'alexa' in command:
            # command = command.replace('alexa', '')
            print(command)
            return command

    except Exception as ex:
        print("Some error....")
        print(ex.__cause__,"+++++++++++++++++++")
        pass
#
#
def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with bayo so fuck of ire')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        # talk('Please say the command again.')
        print("Sorry that's not in my code")
#
#
while True:
    run_alexa()

# print("hello world")
