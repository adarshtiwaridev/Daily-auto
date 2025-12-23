from datetime import datetime

with open("log.txt", "a") as f:
    f.write(f"update at {datetime.now()}\n")

print("Updated successfully")
