import random

from sphero_mini import sphero_mini
from input_constants import ARROW_UP_DOWN_KEY, ARROW_LEFT_RIGHT_KEY

class BallActions:

    def __init__(self,mac_address):
        self.ball = sphero_mini(mac_address)

    def get_destiny(self, code,value):
        destiny = 0

        if code == ARROW_UP_DOWN_KEY:
            if value == 1:
                destiny = 180
            else:
                destiny = 0
        elif code == ARROW_LEFT_RIGHT_KEY:
            if value == 1:
                destiny = 90
            else:
                destiny = 270

        return destiny


    def move_ball(self, code, value, is_analogic=False):
        if is_analogic:
            destiny = value
        else:
            destiny = self.get_destiny(code,value)

        self.ball.roll(255,destiny)

    def wake_up_ball(self):
        self.ball.wake()

    def set_random_color(self):
        self.ball.setLEDColor(red=random.randint(0, 255),
                        green=random.randint(0, 255),
                        blue=random.randint(0, 255))


