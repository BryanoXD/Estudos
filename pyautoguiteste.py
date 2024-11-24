import pyautogui
import time

#pequeno teste para abrir programas

#safe pauses entre ações
pyautogui.PAUSE = 0.5
pyautogui.press('winleft')
pyautogui.write('power point')
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('enter')