#!/usr/bin/env python3
import json 
import os
import sys
import datetime 
import uuid
import getpass
import subprocess

# --- CONFIG ---
LOGDIR = "/home/saswat/LogSphere/logs/"
os.makedirs(LOGDIR, exist_ok=True)
LOGFILE = os.path.join(LOGDIR, "user_sessions.jsonl")

# Detect current user & TTY (no PAM)
USER = getpass.getuser()
try:
    result = subprocess.run(["who", "am", "i"], capture_output=True, text=True)
    if result.returncode == 0 and result.stdout.strip():
        parts = result.stdout.split()
        TTY = parts[1] if len(parts) > 1 else "unknown"
    else:
        TTY = "unknown"
except Exception:
    TTY = "unknown"

SESSION_ID_FILE = f"/run/logsphere_session_{USER}_{TTY.replace('/', '_')}.id"

ACTION = sys.argv[1] if len(sys.argv) > 1 else None
if ACTION not in ["login", "logout"]:
    sys.exit("Invalid action. Use 'login' or 'logout'.")

def log_entry(entry):
    with open(LOGFILE, "a") as f:
        f.write(json.dumps(entry) + "\n")

if ACTION == "login":
    session_id = str(uuid.uuid4())
    login_time = datetime.datetime.now().astimezone().isoformat()

    # Save session ID for logout
    with open(SESSION_ID_FILE, "w") as sid_file:
        sid_file.write(session_id)

    log_entry({
        "session_id": session_id,
        "user": USER,
        "tty": TTY,
        "login_time": login_time,
        "logout_time": None
    })

elif ACTION == "logout":
    try:
        with open(SESSION_ID_FILE, "r") as sid_file:
            session_id = sid_file.read().strip()
    except FileNotFoundError:
        session_id = "unknown"

    logout_time = datetime.datetime.now().astimezone().isoformat()
    log_entry({
        "session_id": session_id,
        "user": USER,
        "tty": TTY,
        "login_time": None,
        "logout_time": logout_time
    })

    # Clean up session file
    if os.path.exists(SESSION_ID_FILE):
        os.remove(SESSION_ID_FILE)
