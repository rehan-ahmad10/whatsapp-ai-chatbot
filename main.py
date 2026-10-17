# =========== Modules & Imports ===========
import pyautogui
import time

from automation import (
    open_chrome,
    check_reply,
    whole_chat_drag,
)
from transcribe import transcribe_voice_notes
from ai_process import response


# =========== Main ===========

if __name__ == "__main__":
    try:
        open_chrome()
        stop = 0
        list1 = []

        while True:
            stop += 1
            if stop % 2 == 0:
                option = pyautogui.confirm("Is you want to stop the program?")
                if option == "OK":
                    break

            is_reply = check_reply()

            list1, list2, chat_text = whole_chat_drag(list1)

            chat_text = transcribe_voice_notes(list2, chat_text)

            if is_reply:
                reply_text = response(chat_text)
                pyautogui.write(reply_text)
                pyautogui.press("enter")

            time.sleep(3)

    except Exception as error:
        print("Error in whatsapp chatbot : ", error)