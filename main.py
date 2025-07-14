import PySimpleGUI as sg
import vlc
import os

vaike=False
raadio=["Elmar","capitalfm","Power","MyHits","Retro","Viker","Kadi","Rock","Star","Spotify"]

layout =  [[sg.Button(key="Elmar",image_filename='imgs/elmar.png', image_size=(84, 84)),
            sg.Button(key="MyHits",image_filename='imgs/myhits.png', image_size=(84, 84)),
            sg.Button(key="Power",image_filename='imgs/phr.png', image_size=(84, 84))],
           
           [sg.Button(key="capitalfm",image_filename='imgs/capitalfm.png', image_size=(84, 84)),
            sg.Button(key="Retro",image_filename='imgs/retro.png', image_size=(84, 84)),
            sg.Button(key="Viker",image_filename='imgs/viker.png', image_size=(84, 84))],
           
           [sg.Button(key="Kadi",image_filename='imgs/kadi.png', image_size=(60, 60)),
            sg.Button(key="Rock",image_filename='imgs/rock.png', image_size=(60, 60)),
            sg.Button(key="Star",image_filename='imgs/star.png', image_size=(60, 60)),
            sg.Button(key="Spotify",image_filename='imgs/spotify.png', image_size=(60, 60))],
            
            [sg.Button(key="Paus",image_filename='imgs/paus.png', image_size=(35, 35)),
             sg.Button(key="Kinni",image_filename='imgs/kinni.png', image_size=(35, 35)),
             sg.Button(key="Minimize",image_filename='imgs/minimize.png', image_size=(35, 35)),
             sg.Slider(range=(0,100),default_value=75, size=(15,17), orientation='h', enable_events=True, key="Heli2")]]


vlayout =   [[sg.Button(key="Paus",image_filename='imgs/paus.png', image_size=(35, 35)),
             sg.Button(key="Kinni",image_filename='imgs/kinni.png', image_size=(35, 35)),
             sg.Button(key="Minimize",image_filename='imgs/minimize.png', image_size=(35, 35)),
             sg.Slider(range=(0,100),default_value=75, size=(10,17), orientation='h', enable_events=True, key="Heli1")]]

#sg.theme("Dark")
window = sg.Window("Raadio", layout, keep_on_top=True,no_titlebar=True,grab_anywhere=True,finalize=True)
aken = sg.Window("Vaike", vlayout,keep_on_top=True,no_titlebar=True,grab_anywhere=True,finalize=True)
aken.Hide()

instance = vlc.Instance('--input-repeat=-1', '--fullscreen')
player=instance.media_player_new()

##lingid
elmari="https://le08.euddn.net/50d351778cb0245e994eaabc73fc6778132b420baff7be3a611bcf4b6f8e059cc32385b5143bfda7170362106c1e586d7b74b3542c461419e511a8e7f24f1b80de6265959d6197111551e0b2eebfa675ba99e8eea717b6488a220c581159550a0c0099c10d6de704dc2377382a28cd4012e7ef5dd78eb00919adbb6e871486dd73b3909607139df07463b2c02186b21d5e588f04112eb00d4d8b8a165ae663b0387428428d5cb67ae042c72f928c9af3/elmar.aac"
poweri="https://ice.leviracloud.eu/phr96-aac?t1611686480595"
capitalfmi="https://media-ice.musicradio.com/CapitalMP3"

myhitsi="https://le04.euddn.net/3da1448ba7d598516fbb71ef2c179ffa78a9d1c7fd84a79ba05b6777fa7323d30c83469e17fe009aa38ca2c2f80a7275e58e7e3d73bd0b952dc36796698d80f28f6e089c48ff3378a6bcc90ec096a23fb0a707a427ee932114ec08a3c81b9d7daf1b169c89cdf672d05e3288f1b0a8a8274ae5ffba183d3d1bd8a676c56f866179c00a50ed65666f0f55aa153a4595f4b1a8c56e1c7e4f43445391e3d4310aa884270a97eb822ae51e64073641390405/myhits.aac"
retroi="https://skymedia-live.bitflip.ee/RETRO"
vikeri="http://icecast.err.ee/vikerraadio.mp3"

kadii="https://kadi.babahhcdn.com/kadi"
rocki="https://skymedia-live.bitflip.ee/rck"
stari="https://ice.leviracloud.eu/star96-aac?t1609956412673"
spotifyi=r"C:\Users\Lapakas\Desktop\Elektra\Koodilised\Python\Raadio\Spotify.lnk"

vana="Paus"
vraadio="Power"
# Create an event loop
while True:
    if vaike:
        event, values = aken.read()
        player.audio_set_volume(int(values["Heli1"]))
    else:
        event, values = window.read()
        player.audio_set_volume(int(values["Heli2"]))
    # End program if user closes window
#    print(event)
    
    
    if event == "Minimize":
        if vaike:
            window.UnHide()
            aken.Hide()
        else:
            aken.UnHide()
            window.Hide()
        vaike=not vaike
    if event=="Elmar":
        media=instance.media_new(elmari)
    elif event=="Power":
        media=instance.media_new(poweri)
    elif event == "capitalfm":
        media=instance.media_new(capitalfmi)
    elif event == "MyHits":
        media=instance.media_new(myhitsi)
    elif event == "Retro":
        media=instance.media_new(retroi)
    elif event == "Viker":
        media=instance.media_new(vikeri)
    elif event == "Kadi":
        media=instance.media_new(kadii)
    elif event == "Rock":
        media=instance.media_new(rocki)
    elif event == "Star":
        media=instance.media_new(stari)
    elif event == "Spotify":
        os.startfile (spotifyi)
        break
    if event in raadio:
        player.set_media(media)
        player.play()
        vraadio = event
    if event == "Paus":
        player.stop()
        if vana =="Paus":
            player.play()
            event=vraadio
    if event == sg.WIN_CLOSED or event == "Kinni":
        break
    if event != "Heli1" and event != "Heli2" and event !="Minimize":
        window.FindElement(vana).Update(button_color=('#FFFFFF', '#283b5b'))    
        vana=event
        window.FindElement(event).Update(button_color=('#FFFFFF', 'yellow'))
    
        
player.stop()
window.close()
aken.close()
