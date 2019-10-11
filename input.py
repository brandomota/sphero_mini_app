from inputs import devices, get_gamepad
from input_constants import *

gamepad = get_gamepad() #InputDevice("/dev/input/event0")

for event in gamepad.read_loop():
   if event.type == ecodes.EV_KEY:

     if event.value == 1:

       if event.code == X_BTN:
         print("botão x")
       
       if event.code == CIRCLE_BTN:
         print("botão bola")