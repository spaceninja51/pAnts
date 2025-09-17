from datetime import datetime, timedelta
from textual.app import App
import time

game_state = {
    "start_tick": 0,
    "crumbs": 0,
    "last_tick": 0
}

class Clock:
    def __init__():
        TICKS_PER_SECOND = 1
        # YYYY-MM-DD HH:MM:SS.sssss
        instance_start =  datetime.now() - timedelta(minutes=5)
        # print(f"Session started at: {instance_start}")
        TICK_RATE = 1/TICKS_PER_SECOND
    def upTime():
        upTime = datetime.now() - instance_start
        print(upTime)
        return upTime
    def timePassed():
        global lastTick
        # If there is not a previous tick, set the startup time as the previous one
        try:
            pauseTime = datetime.now() - lastTick
            lastTick = datetime.now()
        except (UnboundLocalError, NameError):
            print(f"no previous tick found, using instance start time: ({instance_start})")

            lastTick = instance_start
            pauseTime = datetime.now() - lastTick
            lastTick = datetime.now()
        
        ticks = (pauseTime.total_seconds()/TICK_RATE)
        return ticks

toggle = True
timer = Clock
while toggle == True:
    print(timer.timePassed())
    toggle = input()