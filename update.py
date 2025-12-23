import time
import random
from datetime import datetime

# random delay between 0 to 40 minutes (in seconds)
delay = random.randint(0, 40 * 60)

print(f"Waiting for {delay//60} minutes before commit...")
time.sleep(delay)

with open("log.txt", "a") as f:
    f.write(f"Auto commit at {datetime.now()}\n")

print("Commit file updated")
