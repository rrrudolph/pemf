import socket
import urandom
from html import html
from timer import Time
from pemf import PEMF
from lights import Light

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

def set_alarm(m):
    alarm = Time()
    alarm.day_of_year += 1
    alarm.hour = int(m[0])
    alarm.minute = int(m[1:])

    return alarm

def random_decimal():
    x = urandom.getrandbits(7)
    while x > 1:
        x /= 10
    
    return x

alarm = None
while True:
    conn, addr = s.accept()
    #print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    try:
        message = str(request).split('?message=')[1].split(' ')[0]
        print(message)
        print('')
        alarm = set_alarm(message)

    except:  
        response = html
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()

    if alarm:
        break

print(alarm)
pemf_phase_one = alarm.copy(minute_delta=-1)
pemf_phase_two = alarm.copy(minute_delta=-.5)
lights_phase = alarm.copy(minute_delta=-.25)

sleep_frequency = 2 + random_decimal()
wakeup_frequency = 15 + random_decimal()

while True:
    if Time() > pemf_phase_one:
        PEMF.on(sleep_frequency, minutes=0.15)
        break

while True:
    if Time() > pemf_phase_two:
        PEMF.on(wakeup_frequency, minutes=0.15)
        break

while True:
    if Time() > lights_phase:
        Light.on()
        break
        
while True:
    if Time() > alarm:
        PEMF.off()
        Light.off()
        break

# pemf_phase_one = alarm.copy(hour_delta=-4)
# pemf_phase_two = alarm.copy(minute_delta=-30)
# lights_phase = alarm.copy(minute_delta=-3)

# sleep_frequency = 2 + random_decimal()
# wakeup_frequency = 15 + random_decimal()

# while True:
#     if Time() > pemf_phase_one:
#         PEMF.on(sleep_frequency, hours=3.5)
#         break

# while True:
#     if Time() > pemf_phase_two:
#         PEMF.on(wakeup_frequency, minutes=30)
#         break

# while True:
#     if Time() > lights_phase:
#         Light.on()
#         PEMF.on(wakeup_frequency, minutes=3)
#         break
        
# while True:
#     if Time() > alarm:
#         PEMF.off()
#         Light.off()
#         break

