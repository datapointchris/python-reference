import time

import keyboard

MINUTES_TO_WAIT = 5
start = time.time()

while True:
    time.sleep(MINUTES_TO_WAIT * 60)
    keyboard.press_and_release('shift')
    minutes, seconds = divmod(time.time() - start, 60)
    print(f'Running {minutes:.0f} minutes, {seconds:.0f} seconds')
