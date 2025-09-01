from datetime import datetime
import os

now = datetime.now().strftime("%y-%m-%d %H:%M:%S")

with open(os.path.join(os.environ['HOME'], "LogSphere", "login_logs", "logins.txt"), "a") as f:
    f.write(f"Logged in at: {now} \n")
