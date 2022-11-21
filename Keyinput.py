import keyboard
import mouse
import time
import atexit
import os

def logout():
    return os.system('shutdown -l')

def exit_handler():
    print("프로그램이 강제종료됩니다!")
    #logout()
atexit.register(exit_handler)
k=0
while True:
    print(k)
    k+=1
    time.sleep(0.01)
    if keyboard.is_pressed('space'):
        k=0
        print('키보드 입력 감지')
        time.sleep(0.1)
    elif keyboard.is_pressed('backspace'):
        k=0
        print('키보드 입력 감지')
        time.sleep(0.1)
    elif keyboard.is_pressed('enter'):
        k=0
        print('키보드 입력 감지')
        time.sleep(0.1)
    elif mouse.is_pressed('left'):
        k=0
        print('마우스 입력 감지')
        time.sleep(0.1)
    elif mouse.is_pressed('right'):
        k=0
        print('마우스 입력 감지')
        time.sleep(0.1)
    elif k==300:
        break


    


