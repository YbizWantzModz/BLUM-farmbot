import platform
import datetime

def check_system():
    print(f"[INFO] Running on {platform.system()} {platform.release()} ({platform.architecture()[0]})") 

def log_event(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("bot.log", "a") as f:
        f.write(f"[{timestamp}] {message}\n")
