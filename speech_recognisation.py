import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)
def talk(text):
  engine.say(text)
  engine.runAndWait()

def take_command():
  try:
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'mary' in command:
            command = command.replace('mary',"")
            print(command)

  except:
    pass
  return command

def run_mary():
     command = take_command()
     print(command)
     if 'play' in command:
         song = command.replace('play','')
         talk("playing" + song)
         pywhatkit.playonyt(song)
     elif 'time' in command:
         time=datetime.datetime.now().strftime('%I:%M %p')
         print(time)
         talk('current time is'+ time)
     elif 'who is' in command:
         person=command.replace('who is','')
         info=wikipedia.summary(person,1)
         print(info)
         talk(info)
     elif 'date' in command:
         talk("sorry, I am busy")
     elif 'are you single' in command:
         talk("nope,I am in relationship with wifi")
     elif "tea" in command:
         talk("no ,thank you for asking")
     elif "how are you" in command:
         talk("I am doing great,thanks for asking")
     elif 'joke' in command:
         talk(pyjokes.get_joke())
         print(pyjokes.get_joke())
     elif 'friend' in command:
         talk("ya sure, I would love to be  your friend")
     else:
         talk("hey,I am unable to understand , say it again")

run_mary()