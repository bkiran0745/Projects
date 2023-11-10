import pyttsx3
# import Speech_Recognition as sr
import datetime
import time


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)  # to female voice

# engine.setProperty('voices', voices[1].id) for male voice
# 'voice',voices[1].id to get female voice and
# 'voices',voices[1].id to get male verison of voice


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    if hour >= 0 and hour < 12:
        speak(f"good morning sir..!,its {tt}")
    elif hour >= 12 and hour < 18:
        speak(f"good afternoon sir..!,its{tt}")
    else:
        speak(f"good evening sir..!,its {tt}")


speak("HELLO SIR.....!!")
wishme()
speak("INITIALISING EDITH")
speak("I am EDITH..!")
speak("recognising you sir please wait...")
speak("Hello kishor")
speak("How can i help u..")
# def takecomand():
# if__name__=="__main__":
# while True: