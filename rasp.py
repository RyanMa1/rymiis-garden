import time, requests
from board import SCL, SDA
import busio
from adafruit_seesaw.seesaw import Seesaw 
ss = Seesaw(busio.I2C(SCL, SDA), addr=0x36)

heroku = "" #Enter your heroku app URL here
while True:
    requests.post(heroku, data={"temp": ss.get_temp(), "moisture": ss.moisture_read()})
    time.sleep(1)
