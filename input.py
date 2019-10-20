import evdev
from ball_actions import *
from input_constants import *
from time import sleep


def conect_gamepad():
  MAC_ADDRESS = "F9:26:CC:DE:AD:41"
  service = BallActions(MAC_ADDRESS)
  service.wake_up_ball()
  try:

    device = [evdev.InputDevice(path) for path in evdev.list_devices()][0]
    print(device)
    last_second = None

    for event in device.read_loop():

      if event.type in [TYPE_EVENT_KEY_PRESS, TYPE_EVENT_KEY_ARROW_PRESS] and last_second != event.sec:
        last_second = event.sec

        if event.code == ARROW_LEFT_RIGHT_KEY or ARROW_UP_DOWN_KEY and event.value in [-1,1]:
          service.move_ball(event.code, event.value)

        elif event.code in [AXIS_LEFT_RIGHT_CODE, AXIS_UP_DOWN_CODE] and event.value != 0:
          service.move_ball(event.code,event.value,is_analogic=True)

        elif event.value == X_BTN:
          service.set_random_color()

        elif event.code == CIRCLE_BTN:
          print("botão bola")

  except:
    raise


while True:
  try:
    conect_gamepad()

  except Exception as e:
    print("Controle não conectado, aguardando conectar para tentar novamente....")
    sleep(5)

    conect_gamepad()


