import pyautogui
import time
from pynput import keyboard
import pyperclip

# Pause between actions
pause = 0.4

def open_quartr_url():
    # Step 1: Copy quartr_company_id
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(pause)
    quartr_company_id = pyperclip.paste().strip()
    # print("Company ID:", quartr_company_id)

    # Step 2: Move right 3 times and copy quartr_event_id
    for _ in range(3):
        pyautogui.press('right')
        time.sleep(pause / 2)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(pause)
    quartr_event_id = pyperclip.paste().strip()
    # print("Event ID:", quartr_event_id)

    # Step 3: Build the URL
    url = f"https://web.quartr.com/companies/{quartr_company_id}?companyId={quartr_company_id}&documentType=overview&eventId={quartr_event_id}"
    # print("Generated URL:", url)

    # Step 4: Click into browser (right side of split-screen)
    pyautogui.moveTo(1600, 500)  # Adjust if needed based on screen
    pyautogui.click()
    time.sleep(pause)

    # Step 5: Open URL in address bar
    pyautogui.hotkey('ctrl', 'l')
    time.sleep(pause / 2)
    pyautogui.write(url)
    pyautogui.press('enter')

def on_press(key):
    if key == keyboard.Key.num_lock:
        open_quartr_url()
    elif key == keyboard.Key.f3:
        print("Exiting...")
        exit()

# Start listening
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
