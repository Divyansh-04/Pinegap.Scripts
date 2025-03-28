
import pyautogui
import time
from pynput import keyboard
import pyperclip

counter = 0
pause = 0.5

def pinegapDoc():
    global counter
    counter += 1
    print(counter)

    url = "https://web.pinegap.ai/"
    for i in range(3):
        pyautogui.press('left')
    pyautogui.press('down')
    pyautogui.hotkey('ctrl', 'c')
    url += pyperclip.paste() + "/documents?id="
    pyautogui.press('left')
    pyautogui.hotkey('ctrl', 'c')
    url += pyperclip.paste() + "&view=Document"
    pyperclip.copy(url)
    for i in range(4):
        pyautogui.press('right')
    pyautogui.hotkey('alt', 'tab')
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    pyautogui.hotkey('alt', 'tab')


def on_press(key):
    if key == keyboard.Key.num_lock:
        pinegapDoc()
    # elif key == keyboard.Key.caps_lock:
    #     search_company()
    # elif key == keyboard.Key.f9:
    #     pasty()
    elif key == keyboard.Key.f3:
        exit()




with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
