import speech_recognition
from datetime import date
import pyttsx3
today=date.today()
Texttoday=today.strftime("%B, %D, %Y")
print(Texttoday)
voice = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
    print("I am listenning...")
    audio=voice.listen(mic)
try:
    input_text=voice.recognize_google(audio)
except:
    input_text= "I do not understand"
print(input_text)
out_text=" "
if input_text == "hello":
    out_text="Hello, I am AI python"
elif input_text == "what is today":
    out_text= "to day is" + Texttoday
else:
    out_text= "I do not understand"
c=pyttsx3.init()
c.say(out_text)
c.runAndWait()