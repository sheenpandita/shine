import pyjokes
import pywhatkit
import pyttsx3
import datetime
import wikipedia
import modifycmd

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


talk('hi i am shiny , your personal assistant,how can i help you')


def run_shine():
    command = modifycmd.take_command(cmd='')
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is' + time)
    elif 'who is' or 'what' in command:
        person = command.replace('who is' or 'what', '')
        info = wikipedia.summary(person, 10)
        print(info)
        talk(info)
    elif 'joke' in command:
        laugh = pyjokes.get_joke()
        print(laugh)
        talk(laugh)
    elif 'are you single' in command:
        talk('i am in a relationship with wifi')
    else:
        talk('sorry ! please say it again')


while True:
    run_shine()
