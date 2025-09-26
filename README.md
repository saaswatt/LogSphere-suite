# 🛡️ LogSphere v2.1 – User Session Tracker

![Build Status](https://img.shields.io/badge/Status-Active-green?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-2.1-blue?style=for-the-badge)

LogSphere is a **modular Linux user session tracking and auditing tool**, designed to provide structured, machine-readable logs of login and logout events.  
It is built with **Python** and integrates seamlessly with **systemd** for reliable background execution.

---

## ✨ Features
- 🖊 **Login/Logout Tracking**  
  Logs every user login and logout event with `session_id`, `tty`, timestamps, and user details.

- 📧 **Automated Daily Email Alerts**  
  Sends the session logs as an attachment to a configured email address at **12:00 AM daily**, using a **systemd timer**.

---

## 🚀 What's New in v2.1
- ✅ **Session-based tracking** with unique `session_ids`
- 👤 **User identification** – supports multi-user Linux systems
- 🖥️ **TTY tracking** (preparing for multi-terminal monitoring)
- 📜 **Structured JSONL logs** stored in `logs/user_sessions.jsonl`
- 📧 **New Email Alert Service** (Beta) – Daily log summary emailed automatically
- 🧹 **Cleaner and more maintainable codebase** (`tracker.py`)

---

## 📂 Directory Structure
```bash
LogSphere/                       # Root project directory
│
├── credentials/                 # SMTP password and mail config
│   └── smtp_passwd.txt          # Plaintext app password/token (secure this file)
│
├── logs/                        # Runtime logs (not tracked by Git)
│   ├── user_sessions.jsonl      # Session log file
│   └── email_tracker.jsonl      # Email send status history
│
├── scripts/                     # Active Python scripts
│   ├── tracker.py               # Main v2.0 session tracker
│   └── dailyMail.py             # Email automation script
│
├── services/                    # Active systemd service files
│   ├── LogSphere-login.service
│   ├── LogSphere-logout.service
│   ├── LogSphere-email.service
│   └── LogSphere-email.timer
│
├── legacy/                      # Archived versions
│   └── v1.0/                    # Phase 1 (basic login/logout tracker)
│
├── .gitignore                   # Git ignore file (excludes logs)
├── LICENSE
└── README.md                    # This file
```

## ⚙️ Prerequisites

- Linux system with systemd support
- Python 3.x
- A Gmail account with App Passwords enabled
- (Store the app password securely in credentials/smtp_passwd.txt)

## 📥 Installation & Setup
### Clone the Repository
```bash
git clone https://github.com/saaswatt/LogSphere-suite.git
cd LogSphere
```

### Setup Login & Logout Services
- Ensure tracker.py is in the scripts/ directory.
- Copy services to systemd:
```bash
sudo cp services/LogSphere-login.service /etc/systemd/system/
sudo cp services/LogSphere-logout.service /etc/systemd/system/
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable LogSphere-login.service
sudo systemctl enable LogSphere-logout.service
sudo systemctl start LogSphere-login.service
sudo systemctl start LogSphere-logout.service
```

- Logs will now be written to:
```bash
logs/user_sessions.jsonl
```

### Setup Email Alert Feature
- Move Service & Timer Files
```bash
sudo cp services/LogSphere-email.service /etc/systemd/system/
sudo cp services/LogSphere-email.timer /etc/systemd/system/
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
```

- Enable the Timer
```bash
sudo systemctl enable LogSphere-email.timer
sudo systemctl start LogSphere-email.timer
```

- Verify Timer
```bash
systemctl list-timers --all | grep LogSphere-email
```

## 📬 Contact

- If you encounter any issues with setup or have suggestions for improvements, feel free to reach out:

- LinkedIn: [Saswat Kumar Pandey](https://www.linkedin.com/in/saswatkumarpandey)