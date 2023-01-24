import requests
from pynput import keyboard
from pynput.keyboard import Key
#Provide Roku device's IP here
#This program assumes the Roku is OFF
rokuip = "192.168.50.155"
rokuip = "http://" + rokuip + ":8060"
def on_key_release(key):
    if key == Key.right:
        requests.post(rokuip + "/keypress/right")
    elif key == Key.left:
        requests.post(rokuip + "/keypress/left")
    elif key == Key.down:
        requests.post(rokuip + "/keypress/down")
    elif key == Key.up:
        requests.post(rokuip + "/keypress/up")
    elif key == Key.esc:
        exit()
    elif key == Key.f1:
        requests.post(rokuip + "/keypress/poweroff")
    elif key == Key.f2:
        requests.post(rokuip + "/keypress/poweron")
    elif key == Key.f3:
        requests.post(rokuip + "/keypress/home")
    elif key == Key.page_down:
        requests.post(rokuip + "/keypress/volumedown")
    elif key == Key.page_up:
        requests.post(rokuip + "/keypress/volumeup")
    elif key == Key.space:
        requests.post(rokuip + "/keypress/select")
    elif key == Key.enter:
        requests.post(rokuip + "/keypress/select")

inp = input("Option: ")
inp = inp.lower()
powerstate = False
if inp == "on":
    powerstate = True
    requests.post(rokuip + "/keypress/poweron")
if inp == "off":
    powerstate = False
    requests.post(rokuip + "/keypress/poweroff")
if inp == "remote":
    requests.post(rokuip + "/keypress/findremote")
if inp == "control":
    with keyboard.Listener(on_release=on_key_release) as listener:
        listener.join()