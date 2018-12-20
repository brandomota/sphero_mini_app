from sphero_mini import sphero_mini
import time

MAC_ADDRESS = "F9:26:CC:DE:AD:41"

 
cli = sphero_mini(MAC_ADDRESS)

while True:
    cli.setLEDColor(red=255, green=255, blue=0)

    time.sleep(5)

    cli.setLEDColor(red=33,green=33,blue=33)


