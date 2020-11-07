import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r=sr.Recognizer()

def add_note(file, text):
    with open(file, 'a+') as f:
        f.write(text + '.\n')


with sr.Microphone() as source:

    print('Where do you want to save this?')

    file=str(r.recognize_google(r.listen(source)))+'.txt'
    print('Start Talking')
    res=''
    text='x'
    while text:
        audio_text=r.listen(source)
        try:
            text=str(r.recognize_google(audio_text))
            res =res + ' ' +text
        except:
            text=''
    print('Stopped')
    print('You said:', res)
    add_note(file, res)
