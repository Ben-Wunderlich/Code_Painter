import keyboard
import time
import pyautogui

all_keys = {'alt', 'alt gr', 'ctrl', 'left alt', 'left ctrl', 'left shift',
 'left windows', 'right alt', 'right ctrl', 'right shift', 'right windows',
  'shift', 'windows'}

def test():
    if(keyboard.is_pressed("left ctrl")):
        print("this works")
    else:
        print("it didnt work")

#use ctrl + 0
#keyboard.add_hotkey('left ctrl', test)
time.sleep(4)
keyboard.block_key("q")
print("test")
keyboard.wait('0')
print("it pressed")
keyboard.wait('0')
print("it unpressed")
print(time.clock())
test()
