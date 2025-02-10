import time
import random
import keyboard
import pyautogui
import threading
from cloud import get_accounts
from stats import FarmStats
from utils import check_system, log_event

# Настройки
CLICK_INTERVAL = 3  # Интервал между кликами (в секундах)

# Инициализация статистики
stats = FarmStats()

def random_offset():
    return random.randint(-5, 5), random.randint(-5, 5)

def auto_farm():
    print("[INFO] Blum AutoFarm started. Press 'q' to stop.")
    log_event("Bot started")
    
    accounts = get_accounts()
    if not accounts:
        print("[ERROR] No accounts loaded from the cloud.")
        log_event("No accounts loaded")
        return
    
    while not keyboard.is_pressed('q'):
        x, y = pyautogui.position()
        x_offset, y_offset = random_offset()
        pyautogui.moveTo(x + x_offset, y + y_offset, duration=random.uniform(0.1, 0.3))
        pyautogui.click()
        stats.increment_clicks()
        log_event(f"Clicked at ({x + x_offset}, {y + y_offset}) - Total clicks: {stats.get_clicks()}")
        print(f"[INFO] Clicked at ({x + x_offset}, {y + y_offset}) - Total clicks: {stats.get_clicks()}")
        time.sleep(CLICK_INTERVAL + random.uniform(-0.5, 0.5))
    
    print("[INFO] Blum AutoFarm stopped.")
    log_event("Bot stopped")

if __name__ == "__main__":
    check_system()
    threading.Thread(target=auto_farm).start()
