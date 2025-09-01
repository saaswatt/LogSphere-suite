# 🛡️ LogSphere

A **command-line tool (CLI)** to automatically log user **Login and Logout Time and Dates** on Linux systems.

## 🚀 Features
- Logs **login time and date** for each user.
- Logs **logout time and date** for each user.
- Works seamlessly with **systemd** for automatic tracking.

## 📂 Project Structure
```bash
LogSphere                         # Root project directory
│
├── scripts/                      # Python scripts
│   ├── login_logger.py           # Logs login time and date
│   └── logout_logger.py          # Logs logout time and date
│
├── services/                     # Systemd service unit files
│   ├── logger-login.service      # Login tracking service
│   └── logger-logout.service     # Logout tracking service
│
├── LICENSE
├── README.md                     # Documentation
└── requirements.txt              # Dependencies (if any in future)

   ```

## ⚙️ Prerequisites
- Linux system with **systemd** support
- Python 3.x installed
- Basic knowledge of **terminal commands**

## 📥 Installation
**Clone the repository:**
```bash
git clone https://github.com/<your-username>/logger-tool.git
cd scripts
```

### (Optional) Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```


## 🔧 Configuration

**Copy the service files to the systemd directory:**
```bash
sudo cp scripts/services/logger-login.service /etc/systemd/system/
sudo cp scripts/services/logger-logout.service /etc/systemd/system/
```

Reload systemd and enable the services:
```bash
sudo systemctl daemon-reload
sudo systemctl enable logger-login.service
sudo systemctl enable logger-logout.service
sudo systemctl start logger-login.service
sudo systemctl start logger-logout.service
```

## 📊 Usage

- Logs are stored in the folder defined by the script (recommended: **dynamic path inside user’s home directory**).

- **Check service status:**
```bash
systemctl status logger-login.service
systemctl status logger-logout.service
```

## 🧩 Example Log Output
Logged in at: 25-08-18 17:28:00 <br>
Logged out at: 25-08-18 19:23:41 

---

## 📬 Contact

If you encounter any issues with setup or have suggestions for improvements, feel free to reach out:

- LinkedIn: [Saswat Kumar Pandey](https://www.linkedin.com/in/saswatkumarpandey)  

I’ll be happy to connect and help out.