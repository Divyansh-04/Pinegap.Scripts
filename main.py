import pyautogui
import time
from pynput import keyboard
import pyperclip

counter = 0
pause = 0.2


def vafunc():
    global counter
    counter += 1
    print("Count ", counter)
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    for i in range(2):
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
                # ['ctrl', 'tab'],
                ['g'], ['ctrl', 'v']]
    s2 = [['enter'], ['ctrl', 'l'], ['ctrl', 'c']]
    for keys in sequence:
        pyautogui.hotkey(*keys)
        time.sleep(pause)
    time.sleep(pause*7)
    for keys in s2:
        pyautogui.hotkey(*keys)
        time.sleep(pause)


    pyautogui.moveTo(1700, 1050)
    pyautogui.click()
    va_ticker = pyperclip.paste().split('/')[-1]
    pyautogui.hotkey('alt', 'tab')
    time.sleep(pause)
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

def va_from_ticker():
    sequence = [['ctrl', 'tab'], ['up'], ['ctrl', 'c'], ['ctrl', 'tab'], ['alt', 'tab'], ['ctrl', 'l']]
    for keys in sequence:
        pyautogui.hotkey(*keys)
        time.sleep(pause)
    pyautogui.write('https://insights.visiblealpha.com/company/')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')


def quartrNameFunc():
    for i in range(6):
        pyautogui.press('right')

    sequence = [['up'], ['ctrl', 'c'], ['alt', 'tab'], ['/'], ['ctrl', 'v']]
    for keys in sequence:
        pyautogui.hotkey(*keys)
        time.sleep(pause)


    pyautogui.moveTo(1110, 290)
    time.sleep(pause*8)
    pyautogui.click()
    time.sleep(pause*2)
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
    for i in range(8):
        pyautogui.press('left')
    pyautogui.write(tickerid)
    pyautogui.press('right')

def quartrIdFunc():
    for i in range(2):
        pyautogui.press('left')
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.hotkey('alt', 'tab')
    time.sleep(pause)
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.write("https://web.quartr.com/companies/")
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')



def on_press(key):
    if key == keyboard.Key.num_lock:
        quartrIdFunc()
    # elif key == keyboard.Key.caps_lock:
    #     search_company()
    # elif key == keyboard.Key.f9:
    #     pasty()
    elif key == keyboard.Key.f3:
        exit()




with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
