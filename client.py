import socketio
import pyautogui
# standard Python
sio = socketio.Client()
sio.connect('https://lindura.herokuapp.com')

@sio.on('key')
def on_key(key):
    print(key)
    pyautogui.press(key)
