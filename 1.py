import time

def focus_clock(minutes):
    seconds = minutes * 60
    while seconds > 0:
        print(f"Focus for {minutes} minutes. Time remaining: {seconds // 60} minutes {seconds % 60} seconds")
        time.sleep(1)
        seconds -= 1
    print("Time's up! Take a break.")

# 使用示例：专注25分钟
focus_clock(25)
