import esp
esp.osdebug(None)
import network
import utime
from wifi_info import ssid, password
import gc
gc.collect()

# Connect to network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

for _ in range(10):
    if wlan.isconnected() == False:
        utime.sleep(1)

if wlan.isconnected():
    print('connected')
    print(wlan.ifconfig())
else:
    print('failed to connect')