import socketio
import pyautogui
# standard Python
sio = socketio.Client()
sio.connect('http://localhost:3000')

@sio.on('key')
def on_key(key):
    print(key)
    pyautogui.press(key)
    