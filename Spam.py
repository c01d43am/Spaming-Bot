import pyautogui, time
time.sleep(10)
print("Thanks For Using My Code! Make sure to give it a Star on Github!")
print("You have 10 seconds to switch to the tab and select the chat where you want to spam the message")
file = open("send.txt", 'r')
for word in file:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
