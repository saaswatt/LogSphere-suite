"""
This Python Script will send Daily Emails at sharp 12:00am.
Content:
Logs in jsonl format
"""

import os
import ssl
import json
import smtplib
from datetime import datetime
from email.message import EmailMessage

# _________CONFIGURATION_________
SENDER_MAIL = "logsphere.sender@gmail.com"
RECEIVER_MAIL = "logsphere.receiver@gmail.com"
SUBJECT = "LogSphere Daily Log Report"
BODY = "The attached file contains system logs collected in the last 24 hours."
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ATTACHMENT_FILE = os.path.join(BASE_DIR, "logs", "user_sessions.jsonl")
LOG_FILE = os.path.join(BASE_DIR, "logs", "email_tracker.jsonl")
CREDENTIALS_FILE = os.path.join(BASE_DIR, "credentials", "smtp_passwd.txt")

with open(CREDENTIALS_FILE, "r", encoding="utf-8") as f:
    SMTP_PASSWD = f.read().strip()

# _________CREATE THE MESSAGE_________
msg = EmailMessage()
msg["From"] = SENDER_MAIL
msg["To"] = RECEIVER_MAIL
msg["Subject"] = SUBJECT
msg.set_content(BODY)

# _________ATTACH FILE_________
try:
    with open(ATTACHMENT_FILE, "rb") as f:
        file_data = f.read()
        file_name = os.path.basename(ATTACHMENT_FILE)
    msg.add_attachment(
        file_data, maintype="application", subtype="json", filename=file_name
    )
except Exception as exc:
    EMAIL_STATUS = "FAILED: Could not attach file"
    now = datetime.now().isoformat()
    with open(LOG_FILE, "a", encoding="utf-8") as log_track:
        json.dump(
            {"timestamp": now, "event": "Daily Log Sent", "status": EMAIL_STATUS},
            log_track,
        )
        log_track.write("\n")
    raise SystemExit(EMAIL_STATUS) from exc

# _________SEND MAIL_________
try:
    s = smtplib.SMTP("smtp.gmail.com", 587)
    context = ssl.create_default_context()
    s.starttls(context=context)
    s.login(SENDER_MAIL, SMTP_PASSWD)
    s.send_message(msg)
    s.quit()
    EMAIL_STATUS = "SUCCESS!!!"
except smtplib.SMTPAuthenticationError:
    EMAIL_STATUS = "FAILED: Authentication Error"
except smtplib.SMTPConnectError:
    EMAIL_STATUS = "FAILED: Connection error"
except smtplib.SMTPSenderRefused:
    EMAIL_STATUS = "FAILED: Sender refused"
except smtplib.SMTPRecipientsRefused:
    EMAIL_STATUS = "FAILED: Recipient refused"
except smtplib.SMTPDataError:
    EMAIL_STATUS = "FAILED: Data error"
except smtplib.SMTPException:
    EMAIL_STATUS = "FAILED: Other SMTP error"
except Exception:  # pylint: disable=broad-exception-caught
    EMAIL_STATUS = "FAILED: Unexpected error"


now = datetime.now().isoformat()

log_entry = {"timestamp": now, "event": "Daily Log Sent", "status": EMAIL_STATUS}

with open(LOG_FILE, "a", encoding="utf-8") as log_track:
    json.dump(log_entry, log_track)
    log_track.write("\n")
