import pyautogui
import time
from pynput import keyboard
import pyperclip

counter = 0
pause = 0.5


def vafunc():
    global counter
    counter += 1
    print("Count ", counter)
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    for i in range(7):
        pyautogui.press('right')
        # time.sleep(pause/3)
    cpy_cnt = 0
    while True:
        pyautogui.press('up')
        time.sleep(pause)
        pyautogui.hotkey('ctrl', 'c')
        cpy_cnt += 1
        if pyperclip.paste() or cpy_cnt > 5:
            break
    sequence = [['alt', 'tab'],
                ['ctrl', 'tab'],
                ['g'], ['ctrl', 'v']]
    s2 = [['enter'], ['ctrl', 'l'], ['ctrl', 'c']]
    for keys in sequence:
        pyautogui.hotkey(*keys)
        time.sleep(pause)
    time.sleep(pause*5)
    for keys in s2:
        pyautogui.hotkey(*keys)
        time.sleep(pause)


    pyautogui.moveTo(1500, 200)
    pyautogui.click()
    va_ticker = pyperclip.paste().split('/')[-1]
    pyautogui.hotkey('alt', 'tab')
    time.sleep(pause*3)
    pyautogui.press('left')
    pyautogui.press('left')
    pyautogui.press('left')
    pyautogui.write(va_ticker)
    pyautogui.press('right')


def search_company():
    # Copy company
    sequence = [['right'], ['right'], ["ctrl", "c"]]
    for keys in sequence:
        pyautogui.hotkey(*keys)
        # time.sleep(pause)

    # Paste company and click
    pyautogui.hotkey('alt', 'tab')
    time.sleep(pause)
    pyautogui.hotkey('ctrl', 'tab')
    time.sleep(pause)
    pyautogui.moveTo(1100, 400)
    pyautogui.click()
    pyautogui.press('/')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press(' ')
    pyautogui.moveTo(1110, 290)
    time.sleep(pause*10)
    pyautogui.click()
    time.sleep(pause)


    # def pasty():
    # extract ticker id
    sequence = [
        ["ctrl", "l"],
        ["ctrl", "c"],
    ]
    for keys in sequence:
        pyautogui.hotkey(*keys)
        time.sleep(pause)
    tickerid = pyperclip.paste().split('/')[-1].split('?')[0]
    print(tickerid)

    # paste tickerid
    pyautogui.hotkey("alt", 'tab')
    time.sleep(pause*3)
    for i in range(9):
        pyautogui.press('left')
    pyautogui.write(tickerid)
    pyautogui.press('right')


def on_press(key):
    if key == keyboard.Key.caps_lock:
        vafunc()
    elif key == keyboard.Key.num_lock:
        search_company()
    # elif key == keyboard.Key.f9:
    #     pasty()
    elif key == keyboard.Key.f3:
        exit()


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
