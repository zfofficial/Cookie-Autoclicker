from win32gui import GetWindowText, GetForegroundWindow, GetWindowRect, FindWindow
from pyautogui import position
from time import sleep
from pynput.mouse import Button, Controller
from os import system

system("mode 150,25")
system("color 04")
system("title Cookie Autoclicker ~100CPS")

print("""
 ▄████▄  ▒█████  ▒█████  ██ ▄█▀██▓█████     ▄▄▄      █    ██▄▄▄█████▓▒█████  ▄████▄  ██▓    ██▓▄████▄  ██ ▄█▓█████ ██▀███     
▒██▀ ▀█ ▒██▒  ██▒██▒  ██▒██▄█▒▓██▓█   ▀    ▒████▄    ██  ▓██▓  ██▒ ▓▒██▒  ██▒██▀ ▀█ ▓██▒   ▓██▒██▀ ▀█  ██▄█▒▓█   ▀▓██ ▒ ██▒   
▒▓█    ▄▒██░  ██▒██░  ██▓███▄░▒██▒███      ▒██  ▀█▄ ▓██  ▒██▒ ▓██░ ▒▒██░  ██▒▓█    ▄▒██░   ▒██▒▓█    ▄▓███▄░▒███  ▓██ ░▄█ ▒   
▒▓▓▄ ▄██▒██   ██▒██   ██▓██ █▄░██▒▓█  ▄    ░██▄▄▄▄██▓▓█  ░██░ ▓██▓ ░▒██   ██▒▓▓▄ ▄██▒██░   ░██▒▓▓▄ ▄██▓██ █▄▒▓█  ▄▒██▀▀█▄     
▒ ▓███▀ ░ ████▓▒░ ████▓▒▒██▒ █░██░▒████▒    ▓█   ▓██▒▒█████▓  ▒██▒ ░░ ████▓▒▒ ▓███▀ ░██████░██▒ ▓███▀ ▒██▒ █░▒████░██▓ ▒██▒   
░ ░▒ ▒  ░ ▒░▒░▒░░ ▒░▒░▒░▒ ▒▒ ▓░▓ ░░ ▒░ ░    ▒▒   ▓▒█░▒▓▒ ▒ ▒  ▒ ░░  ░ ▒░▒░▒░░ ░▒ ▒  ░ ▒░▓  ░▓ ░ ░▒ ▒  ▒ ▒▒ ▓░░ ▒░ ░ ▒▓ ░▒▓░   
  ░  ▒    ░ ▒ ▒░  ░ ▒ ▒░░ ░▒ ▒░▒ ░░ ░  ░     ▒   ▒▒ ░░▒░ ░ ░    ░     ░ ▒ ▒░  ░  ▒  ░ ░ ▒  ░▒ ░ ░  ▒  ░ ░▒ ▒░░ ░  ░ ░▒ ░ ▒░   
░       ░ ░ ░ ▒ ░ ░ ░ ▒ ░ ░░ ░ ▒ ░  ░        ░   ▒   ░░░ ░ ░  ░     ░ ░ ░ ▒ ░         ░ ░   ▒ ░       ░ ░░ ░   ░    ░░   ░    
░▄▄▄▄▓██   ██▓░  ▒███████▒ █████▒   ░  ░         ░  ░  ░                ░ ░ ░ ░         ░  ░░ ░ ░     ░  ░     ░  ░  ░        
▓█████▒██  ██▒   ▒ ▒ ▒ ▄▀▓██   ▒                                            ░                 ░                               
▒██▒ ▄█▒██ ██░   ░ ▒ ▄▀▒░▒████ ░                                                                                              
▒██░█▀ ░ ▐██▓░     ▄▀▒   ░▓█▒  ░                                                                                              
░▓█  ▀█░ ██▒▓░   ▒███████░▒█░                                                                                                 
░▒▓███▀▒██▒▒▒    ░▒▒ ▓░▒░▒▒ ░                                                                                                 
▒░▒   ▓██ ░▒░    ░░▒ ▒ ░ ▒░                                                                                                   
 ░    ▒ ▒ ░░     ░ ░ ░ ░ ░░ ░                                                                                                 
 ░    ░ ░          ░ ░                                                                                                        
      ░ ░        ░                 
""")

while True:
    if "cookies - Cookie Clicker" in GetWindowText(GetForegroundWindow()):
        window = GetWindowRect(GetForegroundWindow())
        wx = window[0]
        wy = window[1]
        ww = window[2] - wx
        wh = window[3] - wy
        x, y = position()
        if wx<x<wx+ww and wy<y<wy+wh:
            centerx = wx+(ww/100)*15
            centery= wy+(wh/100)*40
            if centerx-128<x<centerx+128 and centery-128<y<centery+128:
                Controller().click(Button.left)
        sleep(0.01)