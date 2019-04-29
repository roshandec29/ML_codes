

import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
m = sr.Microphone()
c=0
scl = []
engine=pyttsx3.init()
try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))
    while True:
        #print("Say something!")
        with m as source: audio = r.listen(source)
        #print("Got it! Now to recognize it...")
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)
            
            # we need some special handling here to correctly print unicode characters to standard output
            if str is bytes:  # this version of Python uses bytes for strings (Python 2)
                print(u"You said {}".format(value).encode("utf-8"))
            else:  # this version of Python uses unicode for strings (Python 3+)
                print("You said {}".format(value))
            if 'hello' or 'hi' in value:
                print("Hi, What's your Name?")
                engine.say("Hi, What's your Name?")
                engine.runAndWait()
                print("Say->")
                with m as source:
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                value = r.recognize_google(audio)
                name=value[11:20]
                print("Hello {} ,how are you ?".format(name))
                engine.say("Hello {} ,how are you ?".format(name))
                engine.runAndWait()
                print("say-->")
                with m as source:
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                value = r.recognize_google(audio)
                
            if 'fine' or 'well' in value:
                print("That's great {} ,What's your school/college name?".format(name))
                engine.say("That's great {} ,What's your school/college name?".format(name))
                engine.runAndWait()
                print("say-->")
                with m as source:
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                scl=r.recognize_google(audio)
                
            if 'not' in value:
                print("Don't worry buddy everything would be fine")
                engine.say("Don't worry buddy everything would be fine")
                engine.runAndWait()
                with m as source:
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                value = r.recognize_google(audio)
                
            if(scl and c<1):
                print("Great I visited {} it was so cool".format(scl))
                engine.say("Great I visited {} it was so cool".format(scl))
                engine.runAndWait()
                print("say-->")
                c=c+1
                with m as source:
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                value = r.recognize_google(audio)
                
            if 'thanks' or 'thank you' in value:
                print("Mention not buddy ");
                engine.say("Mention not buddy ")
                engine.runAndWait()
            
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass


#use pywin32,speechrecognition,pyaudio,pyttsx3

