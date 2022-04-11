import sys
import os
import pyautogui
import time

pyautogui.FAILSAFE = True
letters = 'ylihefc'
require = 'i'

found = []
with open(sys.path[0] +  "/list.txt", "r") as f:
    words = f.readlines()
    for word in words:
        word = word.strip().lower()
        if require not in word:
            continue
        counter = 0
        good = True
        for letter in word:
            if letter not in letters:
                good = False
                break
            counter += 1
        if good and counter >= 4:
            found.append(word)

found = sorted(found, key=len)
found.reverse()

time.sleep(4)
for i in found:
    pyautogui.moveTo(447,750)
    pyautogui.click()
    time.sleep(.1)
    pyautogui.write(i)
    time.sleep(.15)
    pyautogui.press('return')
    time.sleep(.1)
    pyautogui.press('backspace')
    time.sleep(.1)
    

