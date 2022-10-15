import pyautogui
import time

# the code will be executed after a gap of 5 seconds
time.sleep(5)

#n is the number of times you want to send messege
n=5


for i in range(n):
    pyautogui.typewrite("Hey Buddy") # here is the text you may want to send
    pyautogui.press("enter")   # pressing the enter button to send the text

   