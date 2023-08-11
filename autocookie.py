import threading
import time
import pyautogui
import random
from pynput.keyboard import Key, Listener
from win10toast import ToastNotifier
toaster = ToastNotifier()
pyautogui.PAUSE = 0.0001
A = 0
click = False

def notify():
    toaster.show_toast("CookieClick","Autoclicker "+str(click).replace("True","enabled").replace("False","disabled"),icon_path='autocookie_icon.ico', duration=5)

    

def run(refresh):
 global A
 while True:
  if click == True:
   pyautogui.mouseDown(); pyautogui.mouseUp()
   pyautogui.mouseDown(); pyautogui.mouseUp()
   pyautogui.mouseDown(); pyautogui.mouseUp()
   pyautogui.mouseDown(); pyautogui.mouseUp()
   pyautogui.mouseDown(); pyautogui.mouseUp()
   pyautogui.mouseDown(); pyautogui.mouseUp()
   pyautogui.mouseDown(); pyautogui.mouseUp()
   pyautogui.mouseDown(); pyautogui.mouseUp()
   pyautogui.mouseDown(); pyautogui.mouseUp()
   pyautogui.mouseDown(); pyautogui.mouseUp()
   pyautogui.mouseDown(); pyautogui.mouseUp()
   pyautogui.mouseDown(); pyautogui.mouseUp()
   pyautogui.mouseDown(); pyautogui.mouseUp()
   pyautogui.mouseDown(); pyautogui.mouseUp()
   pyautogui.mouseDown(); pyautogui.mouseUp()
   pyautogui.mouseDown(); pyautogui.mouseUp()
   pyautogui.mouseDown(); pyautogui.mouseUp()
   pyautogui.mouseDown(); pyautogui.mouseUp()
   pyautogui.mouseDown(); pyautogui.mouseUp()
   pyautogui.mouseDown(); pyautogui.mouseUp()
   pyautogui.mouseDown(); pyautogui.mouseUp()
  time.sleep(refresh)

def on_press(key):
    pass

def on_release(key):
    note= True
    global toaster
    try:
       if key.char == 'c':
          pass
    except:
        note = False

    if note == True:
      
       if key.char == 'c':
          global click
          if click == False:
             click = True
             y = threading.Thread(target=notify, args=())
             y.start()
          else:
             click = False
             y = threading.Thread(target=notify, args=())
             y.start()
    
       

x = threading.Thread(target=run, args=(0.01,))
x.start()


with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()




