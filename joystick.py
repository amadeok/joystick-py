
#from pyjoystick.sdl2 import Key, Joystick, run_event_loop
import pygame, pyautogui
import time, threading
import pygetwindow as gw
from pygame.locals import *
from pynput.mouse import Listener
#from pynput.keyboard import Key, Controller

import time,random
pygame.display.init()
pygame.joystick.init()
#pygame.joystick.Joystick(0).init()


OFF = (0, "OFF")
RESIZE = (1, "RESIZE")
MOVE = (2, "MOVE")
SCROLL = (3, "SCROLL")
modes = [OFF, RESIZE, MOVE]

mode = RESIZE
mode_counter = RESIZE[0]
middle_mouse_clicked = False
pyautogui.PAUSE = 0.01
#keyboard = Controller()
whitelist = ["ldplayer"]
def loop2(js):
    while 1:
        event = pygame.event.wait()

        if event.type == pygame.JOYDEVICEREMOVED:
            js.quit()
            break

        elif event.type == pygame.JOYDEVICEADDED:
            js.init()


def loop_3():
    js = pygame.joystick.Joystick(0)
    btn_s = 0
    btn_t_a = [1,0]
    double = False
    global j_button_pressed
    while True:
        try:
            event = pygame.event.wait()# pygame.event.get()
            #for event in events:
            if event.type == pygame.JOYBUTTONDOWN:
                if js.get_button(0):
                    j_button_pressed = 1
                    btn_t_a[btn_s] = time.time()    
                    btn_s = 1 - btn_s
                d = btn_t_a[0] - btn_t_a[1]
                if abs(d) < 0.5:
                    j_button_pressed = 2
                    print("double ", btn_t_a, d)

            elif event.type == pygame.JOYBUTTONUP:
                print("button released")
                j_button_pressed =  0
            elif event.type == pygame.JOYDEVICEREMOVED:
                js.quit()
                break

            elif event.type == pygame.JOYDEVICEADDED:
                js.init()

            time.sleep(0.001)
        except Exception as e:
            print(e)
            time.sleep(1)

def on_move(x, y):
    print(x, y)

def on_click(x, y, button, pressed):
    global middle_mouse_clicked; global mode
    if button.name == "middle":
            # if pressed:
            #     mode = SCROLL
            middle_mouse_clicked = pressed
    print(x, y, button, pressed)


def on_scroll(x, y, dx, dy):
    print(x, y, dx, dy)

def mouse_loop():
    with Listener(on_click=on_click) as listener:
        listener.join()


def move_win(xaxis, yaxis):
    global j_button_pressed
    n= 0; n2 = 0; w = None
    if xaxis > 0.5:
        n = round((xaxis-0.5)*10)
    elif xaxis < -0.5:
        n = round((xaxis +0.5)*10)

    if yaxis > 0.5:
        n2 = round((yaxis-0.5)*10)
    elif yaxis < -0.5:
        n2 = round((yaxis +0.5)*10)

    if abs(xaxis) > 0.95:
        n *= 2

    if abs(yaxis) > 0.95:
        n2 *= 2

    try:
        w = gw.getActiveWindow()
        for elem in whitelist:
            if  elem in  w.title.lower():
                w = None
                break

        if w and n or w and n2:
            
            if j_button_pressed == 1:
                w.move(n, n2)
            elif j_button_pressed== 2:#middle_mouse_clicked:
                #for x in range(abs(n)):
                pyautogui.press("right" if n > 0 else "left")
            #for x in range(abs(n2)):
                pyautogui.press("up" if n2 < 0 else "down")
            else:
                w.resize(n, n2)

            print(w.title, n, xaxis, n2, yaxis)
    except Exception as e :
        print(w.title if w else "" , e)

t2 = threading.Thread(target=mouse_loop, args=() )
t2.start()
t2 = threading.Thread(target=loop_3, args=() )
t2.start()

def main_loop():
    print("new loop")
    slp = 0.01
    js = pygame.joystick.Joystick(0)
    
    #t = threading.Thread(target=loop2, args=(js,) )
    #t.start()
    global j_button_pressed
    j_button_pressed = 0
    while 1:
        global mode
        global mode_counter
        
        if slp > 4:
            print(slp)
        time.sleep(slp)

        pygame.event.pump() ### moved to game loop
        timer = time.time() ### add this to show time it takes
        en = js.get_init()
        if not en:
            time.sleep(0.5)
            break
        try:
            xaxis = js.get_axis(0)
            yaxis = js.get_axis(1)
            #j_button_pressed = js.get_button(0)

        except Exception as e:
            print(e)
            time.sleep(0.5)
            #js.init()
            continue
        # if button and mode != MOVE:
        #     mode = MOVE
        #     # mode_counter+=1
        #     # if mode_counter > 2:
        #     #     mode_counter = 0
        #     # mode = modes[mode_counter]
        #     # print("current mode: ", mode[1])
        #     time.sleep(0.1)

        #print("row 38 takes: {0} seconds".format( time.time() - timer ))
        #print("xaxis is: {0} {1}".format(xaxis, yaxis))

        ax = abs(xaxis)
        ay = abs(yaxis)
        m = max(ax, ay)
        if min(ay, ax) <= 0.10:
            slp=0.10
        if m > 0.10:
            slp=round(1/(100*m), 2)


        move_win(xaxis, yaxis)
        #print(xaxis)

    # while True:
    #         #pygame.event.pump()
    #         val1 =pygame.joystick.Joystick(0).get_axis(0)
    #         val2 = pygame.joystick.Joystick(0).get_axis(1)
    #         print(val1, " ", val2)






while True:
    while pygame.joystick.get_count() == 0:
        pygame.display.init()
        pygame.joystick.quit()
        pygame.joystick.init()
        
        time.sleep(1)
        print("no joysticks..")
    t = threading.Thread(target=main_loop, )
    t.start()
    t.join()
    








pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
j =joysticks[0]
print(j.get_init())
j.init()
print(j.get_init())
while 1:
    pygame.event.pump()

    n = j.get_numaxes()
    for x in range(n):
        val = j.get_axis(x)
        if val:
            print(val)
    time.sleep(0.5)
    #print(ax)

ret = Joystick.get_joysticks()
j = None
for jj in ret:
    if len(jj.axis):
        j = jj
        print(j)

while True:
    print(j.axis)
    for elem in j.axis:
        v = vars(elem)
        print(v)
def print_add(joy):
    print('Added', joy)

def print_remove(joy):
    print('Removed', joy)

def key_received(key):
    print('received', key)
    if key.value == Key.HAT_UP:
        pass
    elif key.value == Key.HAT_DOWN:
        pass
    elif key.value == Key.HAT_LEFT:
        pass
    elif key.value == Key.HAT_UPLEFT:
        pass
    elif key.value == Key.HAT_DOWNLEFT:
        pass
    elif key.value == Key.HAT_RIGHT:
        pass
    elif key.value == Key.HAT_UPRIGHT:
        pass
    elif key.value == Key.HAT_DOWNRIGHT:
        pass

run_event_loop(print_add, print_remove, key_received)