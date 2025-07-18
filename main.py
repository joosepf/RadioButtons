import PySimpleGUI as sg
import vlc
import os
from enum import Enum, auto

class Buttons(Enum):
    RADIO1 = 0
    RADIO2 = 1
    RADIO3 = 2
    RADIO4 = 3
    RADIO5 = 4
    RADIO6 = 5
    RADIO7 = 6
    RADIO8 = 7
    RADIO9 = 8
    PLAYER = 9
    PAUS = 10
    MINIMIZE = 11
    STOP = 12
    SOUND = 13

radioImages = []
radioLinks = []

#Read files and links
try:  
    with open("1source.txt", "r") as source:
        a = 0
        for line in source:
            name, link = line.strip().split(',', 1)    
            radioImages.append(f"1imgs/{name}")
            radioLinks.append(link)
except:
    print("Couldn't find source file. Exiting.....")
    exit()


bigLayout =  [[sg.Button(key=Buttons.RADIO1.value,image_filename=radioImages[Buttons.RADIO1.value], image_size=(84, 84)),
            sg.Button(key=Buttons.RADIO2.value,image_filename=radioImages[Buttons.RADIO2.value], image_size=(84, 84)),
            sg.Button(key=Buttons.RADIO3.value,image_filename=radioImages[Buttons.RADIO3.value], image_size=(84, 84))],
           
           [sg.Button(key=Buttons.RADIO4.value,image_filename=radioImages[Buttons.RADIO4.value], image_size=(84, 84)),
            sg.Button(key=Buttons.RADIO5.value,image_filename=radioImages[Buttons.RADIO5.value], image_size=(84, 84)),
            sg.Button(key=Buttons.RADIO6.value,image_filename=radioImages[Buttons.RADIO6.value], image_size=(84, 84))],
           
           [sg.Button(key=Buttons.RADIO7.value,image_filename=radioImages[Buttons.RADIO7.value], image_size=(60, 60)),
            sg.Button(key=Buttons.RADIO8.value,image_filename=radioImages[Buttons.RADIO8.value], image_size=(60, 60)),
            sg.Button(key=Buttons.RADIO9.value,image_filename=radioImages[Buttons.RADIO9.value], image_size=(60, 60)),
            sg.Button(key=Buttons.PLAYER.value,image_filename=radioImages[Buttons.PLAYER.value], image_size=(60, 60))],
            
            [sg.Button(key=Buttons.PAUS.value,image_filename='imgs/pause.png', image_size=(35, 35)),
             sg.Button(key=Buttons.STOP.value,image_filename='imgs/close.png', image_size=(35, 35)),
             sg.Button(key=Buttons.MINIMIZE.value,image_filename='imgs/minimize.png', image_size=(35, 35)),
             sg.Slider(range=(0,100),default_value=75, size=(15,17), orientation='h', enable_events=True, key=Buttons.SOUND.value)]]


smallLayout =   [[sg.Button(key=Buttons.PAUS.value,image_filename='imgs/pause.png', image_size=(35, 35)),
             sg.Button(key=Buttons.STOP.value,image_filename='imgs/close.png', image_size=(35, 35)),
             sg.Button(key=Buttons.MINIMIZE.value,image_filename='imgs/minimize.png', image_size=(35, 35)),
             sg.Slider(range=(0,100),default_value=75, size=(10,17), orientation='h', enable_events=True, key=Buttons.SOUND.value)]]


bigWindow = sg.Window("panel", bigLayout, keep_on_top=True,no_titlebar=True,grab_anywhere=True,finalize=True)
smallWindow = sg.Window("minimized", smallLayout,keep_on_top=True,no_titlebar=True,grab_anywhere=True,finalize=True)
smallWindow.Hide()

#init VLC
instance = vlc.Instance('--input-repeat=-1', '--fullscreen')
player=instance.media_player_new()
#init default values
minimized = False
prevButton = Buttons.RADIO1.value
prevRadio = Buttons.RADIO1.value
media = instance.media_new(radioLinks[prevButton])
player.set_media(media)

while True:
    if minimized:
        event, values = smallWindow.read()
    else:
        event, values = bigWindow.read()
    if event == Buttons.MINIMIZE.value:
        if minimized:
            bigWindow.UnHide()
            smallWindow.Hide()
        else:
            smallWindow.UnHide()
            bigWindow.Hide()
        minimized = not minimized
    elif event == Buttons.SOUND.value:
        player.audio_set_volume(int(values[Buttons.SOUND.value]))
    elif event in range (Buttons.RADIO1.value, Buttons.PLAYER.value):
        prevRadio = event
        media = instance.media_new(radioLinks[event])
        player.set_media(media)
        player.play()
        #bigWindow[Buttons.PAUS.value].Update(button_color=('#FFFFFF', '#283b5b'))    
    elif event == Buttons.PLAYER.value:
        os.startfile (radioLinks[Buttons.PLAYER.value])
        break
    elif event == sg.WIN_CLOSED or event == Buttons.STOP.value:
        break
    elif Buttons.PAUS.value:
        if prevButton == Buttons.PAUS.value:
            player.play()
            smallWindow[Buttons.PAUS.value].Update(button_color=('#FFFFFF', '#283b5b')) 
            event = prevRadio
        else:
            player.stop()
            smallWindow[Buttons.PAUS.value].Update(button_color=('#FFFFFF', 'yellow'))

            
    if event != Buttons.SOUND.value and event != Buttons.MINIMIZE.value:
       bigWindow[prevButton].Update(button_color=('#FFFFFF', '#283b5b'))    
       bigWindow[event].Update(button_color=('#FFFFFF', 'yellow'))
    
    if event != Buttons.SOUND.value and event != Buttons.MINIMIZE.value:
        prevButton = event
        
player.stop()
smallWindow.close()
bigWindow.close()
