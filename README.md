# 🛡️ LogSphere v2.0 – User Session Tracker

![Build Status](https://img.shields.io/badge/Status-Active-green?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-2.0-blue?style=for-the-badge)

LogSphere is a **modular Linux user session tracking and auditing tool**, designed to provide structured, machine-readable logs of login and logout events.  
It is built with **Python** and integrates seamlessly with **systemd** for reliable background execution.

---

## 🚀 What's New in v2.0
- ✅ **Session-based tracking** with unique `session_ids`
- 👤 **User identification** – supports multi-user Linux systems
- 🖥️ **TTY tracking** (preparing for multi-terminal monitoring)
- 📜 **Structured JSONL logs** stored in `logs/user_sessions.jsonl`
- 🧹 **Cleaner and more maintainable codebase** (`tracker.py`)

---

## 📂 Directory Structure
```bash
LogSphere/                       # Root project directory
│
├── legacy/                      # Archived versions
│   └── v1.0/                    # Phase 1 (basic login/logout tracker)
│       ├── scripts/             # Old Python scripts
│       ├── services/            # Old systemd service unit files
│       └── README.md            # Deprecated phase documentation
│
├── logs/                        # Runtime logs (not tracked by Git)
│   └── user_sessions.jsonl      # Session log file
│
├── scripts/                     # Active Python scripts
│   └── tracker.py               # Main v2.0 session tracker
│
├── services/                    # Active systemd service files
│   ├── LogSphere-login.service
│   └── LogSphere-logout.service
│
├── .gitignore                   # Git ignore file (excludes logs)
├── LICENSE
└── README.md                    # This file
```

## ⚙️ Prerequisites
- Linux system with **systemd** support
- **Python 3.x** installed
- Basic knowledge of **terminal commands** 

## 📥 Installation & Setup
### Clone the Repository
```bash
git clone https://github.com/saaswatt/LogSphere-suite.git
cd LogSphere
```

## 📂 File Setup
- Ensure tracker.py is in the scripts/ directory (or move it there).
- Copy the LogSphere-login.service and LogSphere-logout.service files to:
```bash
/etc/systemd/system #For System-wide coverage
```

## 🔧 Enable and Start Services
### Login & Logout Services
```bash
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable LogSphere-login.service
sudo systemctl enable LogSphere-logout.service
sudo systemctl start LogSphere-login.service
sudo systemctl start LogSphere-logout.service
```
- Check the `user_sessions.jsonl` in your `logs` directory for the logs.

## 🧪 Testing
- After setup, try logging out and logging back in.
- Your events should now appear in:
```bash
logs/user_sessions.jsonl
```

### Each entry will include:
- `session_id` (UUID)
- `user` (logged-in username)
- `tty` (if available)
- `login_time` & `logout_time`

## 📬 Contact
 If you encounter any issues with setup or have suggestions for improvements, feel free to reach out:
 - LinkedIn: [Saswat Kumar Pandey](https://www.linkedin.com/in/saswatkumarpandey)  