import speech_recognition as sr
import pyttsx3


nombreAsistente = 'samira'

listener = sr.Recognizer()

asistente = pyttsx3.init()


voices = asistente.getProperty("voices")
asistente.setProperty("voice", voices[1].id)



def talk(text):
    asistente.say(text) #ASI HABLA LA ASISTENTE
    asistente.runAndWait()  

def listen():
    try:
        with sr.Microphone() as source:
            voice = listener.listen(source)
            rec = listener.recognize_google(voice)
            rec = rec.lower()
            if nombreAsistente in rec:
                talk(rec)
    except:
 	  pass



def run():
    rec = listen()
