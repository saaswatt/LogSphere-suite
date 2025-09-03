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
### 🧬 Clone the Repository
```bash
git clone https://github.com/saaswatt/LogSphere-suite.git
cd LogSphere
```
- Copy the **logouts.py** file in 
```bash
/usr/local/bin
```
- Copy the **logger-login serivce** in
```bash
~/.config/systemd/user
```
- Copy the **logger-logout service** in
```bash
/etc/systemd/system
```

## 🔧 Configuration
### Follow these steps to set up **LogSphere** correctly on your system:

- For **logger-login service**, type the following activation commands:
```bash
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl --user enable logger-login.service
sudo systemctl --user start logger-login.service
sudo systemctl --user status logger-login.service
```
- For **logger-logout service**, type the following activation commands:
``` bash
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable logger-logout.service
sudo systemctl start logger-logout.service
sudo systemctl user status logger-logout.service
```

## 📬 Contact

If you encounter any issues with setup or have suggestions for improvements, feel free to reach out:

- LinkedIn: [Saswat Kumar Pandey](https://www.linkedin.com/in/saswatkumarpandey)  

I’ll be happy to connect and help out.