import speech_recognition as sr

r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print("speak: ")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print(format(text))

        except:
            print("speak again") 
