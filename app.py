
from ball_actions import BallActions
from time import sleep


MAC_ADDRESS = "F9:26:CC:DE:AD:41"

def main():
    service = BallActions(MAC_ADDRESS)
    service.wake_up_ball()

    while(True):
        service.ball.roll(speed=50,heading=90)
        sleep(100);

    #controll = 

main()

