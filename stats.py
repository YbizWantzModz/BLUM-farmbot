import json
import os

STATS_FILE = "farm_stats.json"

class FarmStats:
    def __init__(self):
        self.clicks = 0
        self.load_stats()

    def increment_clicks(self):
        self.clicks += 1
        self.save_stats()

    def get_clicks(self):
        return self.clicks

    def save_stats(self):
        with open(STATS_FILE, "w") as f:
            json.dump({"clicks": self.clicks}, f)

    def load_stats(self):
        if os.path.exists(STATS_FILE):
            with open(STATS_FILE, "r") as f:
                data = json.load(f)
                self.clicks = data.get("clicks", 0)

if __name__ == "__main__":
    stats = FarmStats()
    stats.increment_clicks()
    print(f"Total Clicks: {stats.get_clicks()}")
