import pyautogui
import time
from pynput import keyboard, mouse
import pyperclip

counter = 0
pause = 0.1


def vafunc():
    global counter
    counter += 1
    print("Count ", counter)
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    sequence = [
        ['ctrl', 'tab'],
        ['down'],
        ['ctrl', 'c'],
        ['alt', 'tab'],
        ]
    for keys in sequence:
        pyautogui.hotkey(*keys)

    time.sleep(pause)
    pyperclip.copy('https://insights.visiblealpha.com/company/' + pyperclip.paste())


    s2 = [['ctrl', 'l'], ['ctrl', 'v'], ['enter']]
    for keys in s2:
        pyautogui.hotkey(*keys)

    pyautogui.hotkey('alt', 'tab')
    pyautogui.press('right')

def vafunc2():
    pyautogui.hotkey('left')
    pyautogui.hotkey('ctrl', 'c')

    pyautogui.hotkey('alt', 'tab')
    ticker = pyperclip.paste()
    pyperclip.copy('https://insights.visiblealpha.com/mex/' + ticker + '/SCH/KV')
    seq = [['ctrl', 'l'], ['ctrl', 'v'], ['enter'], ['alt', 'tab'], ['ctrl', 'tab']]
    for keys in seq:
        pyautogui.hotkey(*keys)
    time.sleep(pause)
    pyautogui.write(ticker)



def searchQrtrCompany():
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

def vaTicker():
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
    pyautogui.press('down')
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.hotkey('alt', 'tab')
    time.sleep(pause)
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.write("https://web.quartr.com/companies/")
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')


def on_press(key):
    if key == keyboard.Key.num_lock:
        vafunc()
    elif key == keyboard.Key.f9:
        vafunc2()
    elif key == keyboard.Key.f3:
        exit()


def on_click(x, y, button, pressed):
    if button == mouse.Button.x1:
        vafunc()
    elif button == mouse.Button.x2:
        vafunc2()
    elif button == mouse.Button.middle:
        exit()


# with mouse.Listener(on_click = on_click) as listener:
#     listener.join()
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
