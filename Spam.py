import pyautogui, time
time.sleep(1)
file = open("send.txt", 'r')
for word in file:
    pyautogui.typewrite(word)