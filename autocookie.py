#!venv/bin/python
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import PyQt5
import pyautogui
import sys
import threading
import time
import os
from pynput.keyboard import Key, Listener
from notifypy import Notify
from PIL import Image
lock=False
click=False
loop=True
#NOTIFIES USER OF CLICKER STATUS
def notify(TEXT,TOGGLE):
    notifier= Notify()
    notifier.title="AutoCookie"
    notifier.message=TEXT+str(TOGGLE).replace("True","ENABLED").replace("False","DISABLED")
    notifier.icon="autocookie_icon.ico"
    notifier.send()

#SAFETY LOCK TOGGLE
def lock_toggle():
    global lock
    global click
    if lock == True:
        lock=False
        notify("Lock: ",lock)
    else:
        click=False
        lock=True
        notify("Lock: ",lock)

#EXIT CLICKER EVENT        
def clicker_exit(tray_provider):
    global click
    global lock
    lock=False
    click=False
    t=threading.Thread(target=lambda : tray_provider.quit).start()
    
    
#RUNS CLICKER LOOP ON BG AWAITING ACTIVATION
def clicker_loop(refresh):
    global lock
    global click
    while loop:
        if click == True and lock==False:
            pyautogui.mouseDown()
            pyautogui.mouseUp()
        time.sleep(refresh)

#ON PRESS EVENT UNUSED REQUIRED FOR LISTENER BINDING THOUGH
def on_press(key):
    pass

#ON KEY RELEASE EVENT
def on_release(key):
    global click
    #TEST IF KEY VALID
    try:
        #CHECK IF KEYPRESSED IS BINDING KEY =>TOGGLE
        if key.char == 'c':
            if click == False:
                click = True
                not_t = threading.Thread(target=notify, args=("AutoClick: ",click)) 
                not_t.start() #THREAD START
            else:
                click = False 
                not_t = threading.Thread(target=notify,args=("AutoClick: ",click)) 
                not_t.start()  #THREAD START
    except:
        pass


#SYSTEM TRAY DROPDOWN FOR LOCK TOGGLE AND APP EXIT


#SYSTEM TRAY AND APP
def init_tray():
    global lock
    tray_provider = QApplication([]) 
    menu = QMenu() 
    lock_it = QAction("lock/toggle")
    lock_it.triggered.connect(lock_toggle)
    exit_it = QAction("exit")
    exit_it.triggered.connect(tray_provider.quit)
    menu.addAction(lock_it) 
    menu.addAction(exit_it)
    tray_provider.setQuitOnLastWindowClosed(False) 
    tray = QSystemTrayIcon()
    tray.setIcon(QIcon("cookie.png"))
    tray.show()
    tray.setContextMenu(menu)   
    tray_provider.exec_() 

def key_listen():
    pass
def main():
    global lock
    global notifier
    global click
    global loop
    #LOWERS PYAUTOGUI DELAY
    listener = Listener(on_press=on_press,on_release=on_release)
    listener.start()
    clicker_t=threading.Thread(target=clicker_loop,args=(0.01,)).start()
    pyautogui.PAUSE = 0.0001
    init_tray()
    loop=False
   
    

if __name__ =="__main__":
    main()

    


