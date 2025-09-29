#!/usr/bin/env python3
import json
import os
import sys
import datetime
import uuid
import subprocess

# --- CONFIG ---
LOGDIR = "/home/saswat/LogSphere/logs/"
os.makedirs(LOGDIR, exist_ok=True)
LOGFILE = os.path.join(LOGDIR, "user_sessions.jsonl")

# --- Get Active User & TTY via loginctl ---
def get_active_user_and_tty():
    """
    Returns Active Users and TTY
    """
    try:
        # List active sessions (no headers)
        session_result = subprocess.run(["loginctl", "list-sessions", "--no-legend"],
                                        capture_output=True, text=True, check=True)
        sessions = session_result.stdout.strip().splitlines()
        if not sessions:
            return "unknown", "unknown"

        # Take the first active session (usually seat0 for graphical login)
        first_session = sessions[0].split()[0]

        # Get user and TTY for that session
        user_result = subprocess.run(["loginctl", "show-session", first_session,
                                      "-p", "Name", "-p", "TTY"],
                                     capture_output=True, text=True, check=True)
        user_info = dict(line.split("=", 1) for line in user_result.stdout.strip().splitlines())
        return user_info.get("Name", "unknown"), user_info.get("TTY", "unknown")
    except Exception: #pylint: disable=broad-exception-caught
        return "unknown", "unknown"

USER, TTY = get_active_user_and_tty()

# --- Session ID file ---
SESSION_ID_FILE = f"/run/logsphere_session_{USER}_{TTY.replace('/', '_')}.id"

# --- Get Action ---
ACTION = sys.argv[1] if len(sys.argv) > 1 else None
if ACTION not in ["login", "logout"]:
    sys.exit("Invalid action. Use 'login' or 'logout'.")

# --- Helper: Write JSONL entry ---
def log_entry(entry):
    """
    Log Entry format
    """
    with open(LOGFILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")

if ACTION == "login":
    session_id = str(uuid.uuid4())
    login_time = datetime.datetime.now().astimezone().isoformat()

    os.makedirs("/run/logsphere", exist_ok=True)
    with open(SESSION_ID_FILE, "w", encoding="utf-8") as sid_file:
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
        with open(SESSION_ID_FILE, "r", encoding="utf-8") as sid_file:
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

    if os.path.exists(SESSION_ID_FILE):
        os.remove(SESSION_ID_FILE)
