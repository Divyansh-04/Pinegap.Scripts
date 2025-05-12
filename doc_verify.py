import pyautogui
import time
from pynput import keyboard
import pyperclip

counter = 0
pause = 0.5
ticker = ''

def pinegapDoc():
    global counter
    counter += 1
    print(counter)
    url = "https://web.pinegap.ai/"
    for i in range(6):
        pyautogui.press('left')
    pyautogui.press('down')
    pyautogui.hotkey('ctrl', 'c')
    url += pyperclip.paste() + "/documents?id="

    pyautogui.press('right')
    pyautogui.hotkey('ctrl', 'c')
    url += pyperclip.paste() + "&view=Document"
    pyperclip.copy(url)
    for i in range(5):
        pyautogui.press('right')
    pyautogui.hotkey('alt', 'tab')
    time.sleep(pause)
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    pyautogui.hotkey('alt', 'tab')


def vaFast():
    url = "https://insights.visiblealpha.com/company/"
    pyautogui.press('down')
    pyautogui.hotkey('ctrl', 'c')
    url += pyperclip.paste()
    pyautogui.hotkey('alt', 'tab')
    pyperclip.copy(url)
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    pyautogui.hotkey('alt', 'tab')

def qrtrFast():
    url = "https://web.quartr.com/companies/"
    # https://web.quartr.com/companies/18158?companyId=18158&documentType=overview&eventId=339555
    pyautogui.press('down')
    pyautogui.hotkey('ctrl', 'c')
    url += pyperclip.paste() + '?companyId=' + pyperclip.paste() + '&documentType=overview&eventId='
    for i in range(3):
        pyautogui.press('right')
    pyautogui.hotkey('ctrl', 'c')
    url += pyperclip.paste()
    pyautogui.hotkey('alt', 'tab')
    pyperclip.copy(url)
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    pyautogui.hotkey('alt', 'tab')
    pyautogui.press('right')
    pyautogui.press('right')


def extractEventId():
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.hotkey('ctrl', 'c')
    # pyautogui.hotkey('ctrl', 'tab')
    pyautogui.hotkey('alt', 'tab')

    eid = pyperclip.paste().split('eventId=')[-1].split('&')[0]
    pyperclip.copy(eid)

    # pyautogui.press('right')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('down')


def on_press(key):
    if key == keyboard.Key.num_lock:
        # pinegapDoc()
        vaFast()
        # qrtrFast()
    elif key == keyboard.Key.f9:
        extractEventId()
    elif key == keyboard.Key.f3:
        exit()


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()


