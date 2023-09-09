from machine import Pin
from utime import time, sleep_ms
import random

DUTY_CYCLE = 0.2   #  0.15 = 15%
LED = Pin(25, Pin.OUT)
SIGNAL = Pin(2, Pin.OUT)

def create_list_of_frequencies(first_frequency, last_frequency):
    """Return a list of frequencies with random decimals appended. Decimals
    will adhere to the order of the frequencies passed in"""
    
    if first_frequency < last_frequency:
        frequencies = [
            (
                freq + random.uniform(0, 0.33),
                freq + random.uniform(0.33, 0.66),
                freq + random.uniform(0.66, 0.99)
            ) for freq in range(first_frequency, last_frequency +1)
        ]
    else:
        frequencies = [
            (
                freq + random.uniform(0.66, 0.99),
                freq + random.uniform(0.33, 0.66),
                freq + random.uniform(0, 0.33)
            ) for freq in range(first_frequency, last_frequency -1, -1)
        ]
    
    return [frequency for tple in frequencies for frequency in tple]
    

def play_frequency(frequency, seconds):
    """This will actually output a pulse"""

    hz_freq = 1000 / frequency
    ms_on_time = int(DUTY_CYCLE * hz_freq)
    ms_off_time = int((1 - DUTY_CYCLE) * hz_freq)

    print(ms_on_time)
    print(ms_off_time)
    print('playing freq', frequency)

    end = time() + seconds
    while time() < end:
        LED(1), SIGNAL(1)
        sleep_ms(ms_on_time)
        LED(0), SIGNAL(0)
        sleep_ms(ms_off_time)
    
def run(*args, minutes):
    """Play a single frequency or step through a range"""
    
    first_frequency = args[0] 
    total_seconds = minutes * 60 

    if len(args) == 1:
        play_frequency(first_frequency, total_seconds)
    
    else:
        last_frequency = args[1]
        total_frequencies = abs(first_frequency - last_frequency)
        seconds_per_freq = total_seconds / total_frequencies / 3
        frequencies = create_list_of_frequencies(first_frequency, last_frequency)
        print(frequencies)

        for frequency in frequencies:
            play_frequency(frequency, seconds_per_freq)

r_dec = round(random.uniform(0, 0.99), 2)
freq = 1
# freq = 1 + r_dec
run(freq, minutes=90)
# run(40, minutes=10)
# run(25, 22, minutes=1)


