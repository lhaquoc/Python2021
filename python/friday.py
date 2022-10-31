import queue
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os
import sys
import subprocess

friday = pyttsx3.init()
voice = friday.getProperty('voices')
friday.setProperty('voice', voice[1].id)


def speak(audio):
    print('F.R.I.D.A.Y' + '-> ' + audio)
    friday.say(audio)
    friday.runAndWait()


def time():
    time = datetime.datetime.now().strftime('%I:%M:%p')
    speak(time)


def welcome():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak('Good morning!')
    elif hour >= 12 and hour < 18:
        speak('Good afternoon!')
    elif hour >= 18 and hour <= 24:
        speak('Good evening!')
    speak('How can I help you?')


def command():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold = 2
        audio = c.listen(source)
    try:
        query = c.recognize_google(audio, language='en')
        print('command: ' + query)
    except sr.UnknownValueError:
        print('Please repeat or enter command')
        query = str(input('Your order is: '))
    return query


def open_file(url):
    if sys.platform == 'win32':
        os.startfile(url)
    else:
        opener = 'open' if sys.platform == 'darwin' else 'xdg-open'
        subprocess.call([opener, url])


def main():
    # speak('Hello Youtube')
    # time()
    welcome()
    while True:
        query = command().lower()
        if 'google' in query:
            speak('What should I search?')
            search = command().lower()
            url = f'https://www.google.com/search?q={search}'
            wb.get().open(url)
            speak(f'Here is your search {search} on google')
        if 'youtube' in query:
            speak('What should I search?')
            search = command().lower()
            url = f'https://www.youtube.com/search?q={search}'
            wb.get().open(url)
            speak(f'Here is your search {search} on google')
        elif 'open video' in query:
            speak('opening video')
            video = '/Users/anhquoc/Desktop/thanos.mp4'
            open_file(video)
        elif 'time' in query:
            time()
        elif 'quit' in query:
            speak('Friday is quitting, goodbye')
            quit()


if __name__ == '__main__':
    main()
