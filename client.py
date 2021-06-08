import socketio
import pyautogui
# standard Python
sio = socketio.Client()
# sio.connect('https://lindura.herokuapp.com')
sio.connect('http://localhost:3000')


@sio.on('keyd')
def on_key(key):
    if(key != 16):
        print(chr(key).lower())
        pyautogui.keyDown(chr(key).lower())


@sio.on('keyu')
def on_key(key):
    if(key != 16):
        print(chr(key).lower())
        pyautogui.keyUp(chr(key).lower())
