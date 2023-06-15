import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import os
import pyttsx3
# text to speech
engine = pyttsx3.init('dummy')


def speak_now():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def set_voice():
        if gender == 'Male':
            engine.setProperty('voice', voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            engine.say(text)
            engine.runAndWait()

    if text:
        if speed == 'Fast':
            engine.setProperty('rate', 250)
            set_voice()
        elif speed == 'Normal':
            engine.setProperty('rate', 150)
            set_voice()
        else:
            engine.setProperty('rate', 60)
            set_voice()
    print('speaking')


def download():
    print('downloading')


root = Tk()
root.title('Text to Speech')
root.geometry('900x450+100+100')
root.resizable(False, False)
root.configure(bg='#305065')

# icon
image_icon = PhotoImage(file='speak.png')
root.iconphoto(False, image_icon)

# top frame
top_frame = Frame(root, bg='white', width=900, height=100)
top_frame.place(x=0, y=0)
logo = PhotoImage(file='speaker_logo.png')
Label(top_frame, image=logo, bg='white').place(x=10, y=5)
Label(top_frame, text='TEXT TO SPEECH', font='arial 20 bold', bg='white', fg='black').place(x=100, y=40)

# input
text_area = Text(root, font='Robote 20', bg='white', fg='black', relief=GROOVE, wrap=WORD)
text_area.place(x=10, y=150, width=500, height=250)

# output
Label(root, text='VOICE', font='arial 15 bold', bg='#305065', fg='white').place(x=580, y=160)
Label(root, text='SPEED', font='arial 15 bold', bg='#305065', fg='white').place(x=760, y=160)

genders = ['Male', 'Female']
gender_combobox = Combobox(root, values=genders, font='arial 14', state='r', width=14)
gender_combobox.place(x=550, y=200)
gender_combobox.set(genders[0])

speeds = ['Fast', 'Normal', 'Slow']
speed_combobox = Combobox(root, values=speeds, font='arial 14', state='r', width=14)
speed_combobox.place(x=730, y=200)
speed_combobox.set(speeds[1])

icon_speak = PhotoImage(file='speak.png')
button_speak = Button(root, text='Speak', compound=LEFT, width=133, font='arial 14 bold', image=icon_speak, command=speak_now)
button_speak.place(x=550, y=280)

icon_download = PhotoImage(file='download.png')
button_download = Button(root, text='Download', compound=LEFT, width=133, bg='#39c790', font='arial 14 bold', image=icon_download, command=download)
button_download.place(x=730, y=280)


root.mainloop()
