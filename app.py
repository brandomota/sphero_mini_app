
from ball_actions import BallActions
from time import sleep


MAC_ADDRESS = "F9:26:CC:DE:AD:41"

def main():
    service = BallActions(MAC_ADDRESS)
    service.wake_up_ball()

    while(True):
        service.ball.roll(speed=150,heading=90)
        sleep(3)
        service.ball.roll(speed=150,heading=180)
        sleep(3)
        service.ball.roll(speed=150,heading=270)
        sleep(3)
        service.ball.roll(speed=150,heading=360)
        sleep(3)

    #controll = 

main()

