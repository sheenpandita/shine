import speech_recognition as sr
listener = sr.Recognizer()


def take_command(cmd):
    try:
        with sr.Microphone() as source:
            print('listening....')
            voice = listener.listen(source)
            cmd = listener.recognize_google(voice)
            cmd = cmd.lower()
            if 'shiny' in cmd:
                cmd = cmd.replace('shiny', '')
                print(cmd)
    except:
        pass
    return cmd
