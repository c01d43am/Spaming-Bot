import pyautogui, time
time.sleep(5)
print("Thanks For Using My Code! Make sure to give it a Star ")
print("You have 5 seconds to switch to the tab and select the chat where you want to spam the message")
file = open("send.txt", 'r')
for word in file:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
