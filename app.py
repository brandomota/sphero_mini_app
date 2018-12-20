from sphero_mini import sphero_mini
import time, random

MAC_ADDRESS = "F9:26:CC:DE:AD:41"

 
cli = sphero_mini(MAC_ADDRESS)

for i in range(50):
    cli.setLEDColor(red=random.randint(0,255), 
                    green=random.randint(0,255), 
                    blue=random.randint(0,255))

    time.sleep(0.05)

cli.roll(50,90)

