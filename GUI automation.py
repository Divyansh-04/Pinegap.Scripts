import pyautogui
import time
from pynput import keyboard

counter = 0
pause = 0.3


def func():
    pyautogui.press('left')
    pyautogui.press('down')
    pyautogui.hotkey('alt', 'tab')
    time.sleep(pause)
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(pause)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(pause)
    pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(pause)
    pyautogui.click()
    global counter
    counter += 1
    print(counter)




def on_press(key):
    if key == keyboard.Key.num_lock:
        func()
    elif key == keyboard.Key.f9:
        exit()


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
