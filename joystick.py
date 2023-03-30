
#from pyjoystick.sdl2 import Key, Joystick, run_event_loop
import pygame
import time


import pygame
#import serial ### I do not have "serial" so I remove this
import time
pygame.display.init()
pygame.joystick.init()
pygame.joystick.Joystick(0).init()

slp = 0.01
js = pygame.joystick.Joystick(0)

while 1:
    time.sleep(slp)

    pygame.event.pump() ### moved to game loop
    timer = time.time() ### add this to show time it takes

    xaxis = js.get_axis(0)
    yaxis = js.get_axis(1)

    #print("row 38 takes: {0} seconds".format( time.time() - timer ))
    print("xaxis is: {0} {1}".format(xaxis, yaxis))

    ax = abs(xaxis)
    ay = abs(yaxis)
    m = max(ax, ay)
    if min(ay, ax) <= 0.10:
        slp=0.10
    if m > 0.10:
        slp=round(1/(100*m), 2)
    #print(xaxis)

# while True:
#         #pygame.event.pump()
#         val1 =pygame.joystick.Joystick(0).get_axis(0)
#         val2 = pygame.joystick.Joystick(0).get_axis(1)
#         print(val1, " ", val2)









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