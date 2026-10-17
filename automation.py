# =========== Modules & Imports ===========
import pyautogui
import pyperclip
import time


# =========== Functions ===========

def open_chrome():
    try:
        chrome_icon = pyautogui.locateCenterOnScreen("assets/chrome_icon.jpg", confidence=0.7)
        pyautogui.click(chrome_icon)
        time.sleep(0.5)
    except Exception as error:
        print("Opening chrome Error : ", error)


# ===================================

def check_isdraging(x, y):
    copy_text = ""
    pyautogui.hotkey("ctrl", "c")
    copy_text += pyperclip.paste()

    if copy_text == "":
        x, y = 707, 348
        pyautogui.click(x, y)
        pyautogui.moveTo(x, y)
        pyautogui.mouseDown(button='left')

    return x, y


# ===================================

def chat_text_drag(x, y, chat_text):
    while y < 918 and x < 1886:
        x += 24.24
        y += 12.9
        pyautogui.moveTo(x, y)

        if x == 803.96 and y == 358.5999999999999:
            x, y = check_isdraging(x, y)

    pyautogui.hotkey("ctrl", "c")
    paste_text = pyperclip.paste()

    if (paste_text not in chat_text) and (not(paste_text.startswith("WhatsApp"))):
        chat_text += paste_text

    pyautogui.click(706, 307)
    pyautogui.click(706, 330)

    return chat_text


# ===================================

def download_voice_note(x, y, start, voice_note_button, chat_text, list1, list2):
    pyautogui.hotkey("ctrl", "c")
    paste_text = pyperclip.paste()

    if (paste_text not in chat_text) and (not(paste_text.startswith("WhatsApp"))):
        chat_text += paste_text

    pyautogui.click(706, 307)
    pyautogui.click(706, 330)
    time.sleep(0.5)

    pyautogui.click(voice_note_button, button="right")

    time.sleep(1)
    try:
        download_icon = pyautogui.locateCenterOnScreen("assets/download_icon.jpg", confidence=0.8)
        pyautogui.click(download_icon)
    except Exception:
        pyautogui.click(706, 307)
        pyautogui.click(706, 330)

        pyautogui.moveTo(x, y)
        pyautogui.mouseDown(button='left')
        time.sleep(0.5)
        return start, chat_text, list1, list2

    time.sleep(2.5)

    pyautogui.click(618, 854)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("ctrl", "c")
    voice_note_name = pyperclip.paste()

    count = voice_note_name.find("M")
    voice_note_name = voice_note_name[0:count+1]
    list2.append(voice_note_name)
    print("NOTE : ", voice_note_name)

    if voice_note_name not in list1:
        list1.append(voice_note_name)
        pyautogui.press("enter")
        time.sleep(1.5)
        pyautogui.click(706, 307)
        pyautogui.click(706, 330)
    else:
        pyautogui.click(pyautogui.locateCenterOnScreen("assets/cancel_icon.jpg"))
        time.sleep(1)
        pyautogui.click(706, 307)
        pyautogui.click(706, 330)

    index = start
    chat_text += "\n"
    chat_text += f"Voice note {index}"
    chat_text += "\n"
    start += 1
    pyautogui.moveTo(x, y)
    pyautogui.mouseDown(button='left')

    return start, chat_text, list1, list2


# ===================================

def whole_chat_drag(list1):
    x = 707
    y = 307
    list2 = []
    chat_text = ""
    start = 0

    pyautogui.moveTo(x, y)
    pyautogui.mouseDown(button='left')
    time.sleep(0.5)

    while True:
        try:
            all_voice_note_buttons = list(pyautogui.locateAllOnScreen("assets/voice_note_icon.jpg", confidence=0.999))
            len1 = len(all_voice_note_buttons)
        except Exception:
            chat_text = chat_text_drag(x, y, chat_text)
            break

        if start >= len1:
            chat_text = chat_text_drag(x, y, chat_text)
            break
        elif start < len1:
            voice_note_button = all_voice_note_buttons[start]

        x += 24.24
        y += 12.9

        pyautogui.moveTo(x, y)

        if x == 803.96 and y == 358.5999999999999:
            x, y = check_isdraging(x, y)

        if y >= voice_note_button.top + 35:
            start, chat_text, list1, list2 = download_voice_note(x, y, start, voice_note_button, chat_text, list1, list2)

    return list1, list2, chat_text


# ===================================

def check_reply():
    pyautogui.click(1752, 869, button="right")
    is_reply = True
    time.sleep(1)

    try:
        pyautogui.locateCenterOnScreen("assets/copy_icon.jpg", confidence=0.9)
        pyautogui.click(706, 307)
        pyautogui.click(706, 330)
        is_reply = False
    except Exception:
        pyautogui.click(706, 307)
        pyautogui.click(706, 330)

    time.sleep(0.5)
    return is_reply