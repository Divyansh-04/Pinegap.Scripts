
import pyautogui
import time
from pynput import keyboard
import pyperclip

counter = 0
pause = 0.5

# def pinegapDoc():
#     global counter
#     counter += 1
#     print(counter)

#     url = "https://web.pinegap.ai/"
#     for i in range(3):
#         pyautogui.press('left')
#     pyautogui.press('down')
#     pyautogui.hotkey('ctrl', 'c')
#     url += pyperclip.paste() + "/documents?id="
#     pyautogui.press('left')
#     pyautogui.hotkey('ctrl', 'c')
#     url += pyperclip.paste() + "&view=Document"
#     pyperclip.copy(url)
#     pyautogui.hotkey('alt', 'tab')
#     time.sleep(pause)
#     pyautogui.hotkey('ctrl', 'l')
#     pyautogui.hotkey('ctrl', 'v')
#     pyautogui.press('enter')
#     pyautogui.hotkey('alt', 'tab')
#     for i in range(2):
#         pyautogui.press('right')
#     pyautogui.hotkey('ctrl', 'c')
#     for i in range(2):
#         pyautogui.press('right')

def pinegapDoc():
    global counter
    counter += 1
    print(counter)

    url = "https://web.pinegap.ai/"

    # Copy documentId from current cell
    pyautogui.hotkey('ctrl', 'c')
    doc_id = pyperclip.paste()

    # Move to ticker (right cell) and copy
    pyautogui.press('right')
    pyautogui.hotkey('ctrl', 'c')
    ticker = pyperclip.paste()

    # Construct final URL
    full_url = f"{url}{ticker}/documents?id={doc_id}&view=Document"

    # Open in browser
    pyautogui.hotkey('alt', 'tab')
    time.sleep(pause)
    pyperclip.copy(full_url)
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')

    # Switch back
    pyautogui.hotkey('alt', 'tab')
    pyautogui.press('down')
    pyautogui.press('left')  # Move to next row if needed



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
    pyautogui.press('down')
    pyautogui.hotkey('ctrl', 'c')
    url += pyperclip.paste()
    pyautogui.hotkey('alt', 'tab')
    pyperclip.copy(url)
    pyautogui.hotkey('ctrl', 'l')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    pyautogui.hotkey('alt', 'tab')



def on_press(key):
    if key == keyboard.Key.num_lock:
        pinegapDoc()
        # vaFast()
        # qrtrFast()
    elif key == keyboard.Key.f3:
        exit()


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
