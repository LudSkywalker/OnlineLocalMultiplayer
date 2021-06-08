import socketio
import pyautogui
# standard Python
sio = socketio.Client()
sio.connect('https://lindura.herokuapp.com')
#sio.connect('http://localhost:3000')
nd=0
nu=0

@sio.on('keyd')
def on_key(key):
    global nd
    if(key != 16 and nd<6):
        nd+=1
        #print(chr(key).lower())
        pyautogui.keyDown(chr(key).lower())
        nd-=1


@sio.on('keyu')
def on_key(key):
    global nu
    if(key != 16 and nu<6):
        nu+=1
        #print(chr(key).lower())
        pyautogui.keyUp(chr(key).lower())
        nu-=1
    
