import tkinter as tk
from tkinter import *
from tkinter import ttk
from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import pyttsx3
import datetime
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips, CompositeAudioClip, concatenate_audioclips
import time
from threading import Thread
import random


root = tk.Tk()

background_color = "gray17"
text_color = "cadetblue1"

root.geometry("450x650")
root.title("Reddit Story Gen")
root.configure(background=background_color)

Title = tk.Label(root, text = "Reddit Story Gen", font = ('Arial', 24), fg=text_color, bg=background_color)
Title.pack()

text_box = tk.Entry(fg="black", bg="white", width=20, font= ('Arial', 24))
text_box.insert(0, "Link here")
text_box.pack(pady=5)
text_box.configure(state=DISABLED)

count_words = "Check Word Count"

def checkwordcount():
    link = text_box.get()
    requests_results = requests.get(link)
    raw = BeautifulSoup(requests_results.text, "html.parser")
    bad_text = raw.find('p')
    base_text = raw.find_all('p')

    worse_text = str(bad_text)

    mystring = str(base_text)
    mystring = mystring.replace(worse_text, '')
    mystring = mystring.replace('[, <p>', '')
    mystring = mystring.replace('</p>, <p>', '')
    mystring = mystring.replace('</p>]', '')
    count_words = len(mystring)
    word_count.configure(text = count_words)





word_count = tk.Button(text=count_words,
    width=15,
    height=1,
    bg=text_color,
    fg=background_color,
    font = ('Arial', 25),
    pady=5,
    command= checkwordcount)
word_count.pack()

def on_click(event):
    text_box.configure(state=NORMAL)
    text_box.delete(0, END)

    # make the callback only work once
    text_box.unbind('<Button-1>', on_click_id)

on_click_id = text_box.bind('<Button-1>', on_click)


#SLIDERS







style=ttk.Style()
style.theme_use('clam')
style.configure('Horizontal.TScale', background=text_color, troughcolor='lightblue3', troughrelief='banana')

# slider current value
current_value = tk.DoubleVar()


def get_current_value():
    return '{: .2f}'.format(current_value.get())


def slider_changed(event):
    value_label.configure(text=get_current_value())


# label for the slider
slider_label = ttk.Label(
    root,
    text='Narration Volume:',
    font = ('Arial', 20),
    foreground=text_color,
    background=background_color
)

slider_label.pack()

#  slider
slider = ttk.Scale(
    root,
    from_=0,
    to=2,
    orient='horizontal',  # vertical
    command=slider_changed,
    variable=current_value,
    length=300
    
    
    
)

slider.pack()



# value label
value_label = ttk.Label(
    root,
    text=get_current_value(),
    font = ('Arial', 24), foreground=text_color,
    background=background_color
)
value_label.pack()

current_value1 = tk.DoubleVar()

def get_current_value1():
    return '{: .2f}'.format(current_value1.get())


def slider_changed1(event):
    value_label1.configure(text=get_current_value1())


# label for the slider
slider_label1 = ttk.Label(
    root,
    text='Narration Speed (Words Per Minute):',
    font = ('Arial', 17),
    foreground=text_color,
    background=background_color
)

slider_label1.pack()

#  slider
slider1 = ttk.Scale(
    root,
    from_=150,
    to=400,
    orient='horizontal',  # vertical
    command=slider_changed1,
    variable=current_value1,
    length=300
    
    
    
)

slider1.pack()



# value label
value_label1 = ttk.Label(
    root,
    text=get_current_value1(),
    font = ('Arial', 24), foreground=text_color,
    background=background_color
)
value_label1.pack()

#Paused_Image1 = PhotoImage(file="Pause.png")
#Play_Image1 = PhotoImage(file="Play.png")
#
#Play_Image = Play_Image1.subsample(3, 3)
#Paused_Image = Paused_Image1.subsample(3, 3)
#
#def Pause_Command():
#   button.config(image= Paused_Image, command=Play_Command)
#
#
#def Play_Command():
#    button.config(image= Play_Image, command=Pause_Command)
#
#
#img_label= Label(image=Play_Image)
#
##Let us create a dummy button and pass the image
#button= Button(root, image=Play_Image, command= Pause_Command,
#borderwidth=0)
#button.pack(pady=30)

def change_colour():
    Red = 219
    Green = 91
    Blue = 82

    for i in range(100):
        color_c='#%02x%02x%02x' % Red, Green, Blue

        Red = Red - 0.97
        Green = Green + 1.49
        Blue = Blue + 0.07

        time.sleep(0.1)
        
        Launch.configure(fg=color_c)

def run():
    x = datetime.datetime.now()
    link = text_box.get()
    requests_results = requests.get(link)
    raw = BeautifulSoup(requests_results.text, "html.parser")
    bad_text = raw.find('p')
    base_text = raw.find_all('p')

    worse_text = str(bad_text)

    mystring = str(base_text)
    mystring = mystring.replace(worse_text, '')
    mystring = mystring.replace('[, <p>', '')
    mystring = mystring.replace('</p>, <p>', '')
    mystring = mystring.replace('</p>]', '')


    basename = 'StoryNarrated.mp3'
    time = x.day , x.hour , x.minute
    time_string = str(time)

    engine = pyttsx3.init();

    voice = engine.getProperty('voices')
# eng.setProperty('voice', voice[0].id) #set the voice to index 0 for male voice
    engine.setProperty('voice', voice[0].id)

    rate = (get_current_value1())
    volume = (get_current_value())

    

    rate = rate.replace(' ', '')
    volume = volume.replace(' ', '')
    rate = rate.replace('.00', '')
    volume = volume.replace('.00', '')

    rate = float(rate)
    volume = float(volume)

    rate = round(rate)
    volume = round(volume)

    rate = int(rate)
    volume = int(volume)




    engine.setProperty('rate', int(rate))
    engine.setProperty('volume', int(rate))

    engine.save_to_file(mystring,'StoryNarrated.mp3')


    engine.runAndWait();

    clip = AudioFileClip("StoryNarrated.mp3")
   
  
    # getting duration of the audio
    duration = clip.duration
    
    #print wpm

    print("Wpm:" + str(rate) + 'a')

    # printing duration
    print("Duration : " + str(duration))

    Full_Length = duration + 1
    start_time = random.randint(0,480)
    #Import backbround footage

    Background = VideoFileClip("Background_Footage.mp4").subclip(start_time,start_time+Full_Length)

    audio = AudioFileClip(basename)

    combined = concatenate_videoclips([Background])
    combined.audio = CompositeAudioClip([audio])

    #Process all



    combined.write_videofile("Final.mp4")

#colour 1 is 219, 91, 82
#colour 2 is 122 240 89


    
def Final_Run():
    Thread(target=change_colour).start()
    Thread(target=run).start()












Launch = tk.Button(
    text="Launch",
    width=10,
    height=2,
    bg=text_color,
    fg=background_color,
    font = ('Arial', 30),
    command= Final_Run

)

Launch.pack()









root.mainloop()