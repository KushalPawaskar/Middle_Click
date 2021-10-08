import pyautogui as pya
import keyboard as kb
def middleclick():
    x,y=pya.position()
    pya.click(x,y,button='middle')
    pya.FAILSAFE=True
while True:
    if kb.is_pressed('m+c'):
        middleclick()
    elif kb.is_pressed('q+m+c'):
        break