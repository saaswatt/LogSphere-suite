import json
from datetime import datetime
import os

log_entry = {
    "time stamp" : datetime.now().astimezone().isoformat(),
    "Event" : "login"
}

base_dir = os.path.dirname(os.path.abspath(__file__))

logs_dir = os.path.join(base_dir, "..", "logs")
os.makedirs(logs_dir, exist_ok=True)

log_file = os.path.join(logs_dir, "login_logs.jsonl")

with open(log_file, "a") as f:
    f.write(json.dumps(log_entry)+"\n")