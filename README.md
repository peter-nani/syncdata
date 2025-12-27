# syncdata
sync data from wsl to vpn server
📦 Persistent Rsync Screenshot Sync Service

A production-grade, self-healing Python service that continuously syncs screenshots from a Windows machine (via WSL) to a remote Linux server using rsync, deletes source files after successful transfer, survives network failures, and auto-starts on boot using systemd.

🚀 Features

✅ Runs forever (daemon-style)
✅ Auto-detects current month folders (YYYY-MM)
✅ Waits for network & SSH availability
✅ Uses rsync for efficient incremental sync
✅ Deletes source files only after successful transfer
✅ Never deletes the month folder
✅ Handles empty / missing folders safely
✅ Auto-starts on boot via systemd
✅ Log rotation via logrotate
✅ Safe for production use

🧱 Architecture Overview
Windows (ShareX Screenshots)
        ↓
WSL Ubuntu (Python Service)
        ↓
rsync over SSH
        ↓
Remote Linux Server (Archive Storage)

📂 Directory Structure
/home/admin_user/
├── cronjobs/
│   └── sync_forever.py
├── persistent_rsync.log

⚙️ Requirements
On Source Machine (WSL / Linux)
Python 3.8+
rsync
ssh
systemd (for service mode)
sudo apt update
sudo apt install -y rsync openssh-client


On Destination Server
SSH server running
Target directory exists
SSH key-based login enabled


🔐 SSH Setup (MANDATORY)
Passwordless SSH is required.
ssh-keygen -t ed25519
ssh-copy-id admin@192.168.1.148


Verify:
ssh -o BatchMode=yes hr306@192.168.1.146 echo ok

Expected output:
ok


🐍 Script Configuration
sync_forever.py (Key Concepts)
Auto-detect current month
def get_src():
    month = datetime.now().strftime("%Y-%m")
    return f"/mnt/c/Users/hr306/Downloads/ShareX-18.0.1-portable/ShareX/Screenshots/{month}/"

Safety guarantees
Month folder is auto-created if missing
Month folder is never deleted
Only files are removed after transfer
Empty subfolders are cleaned safely


▶️ Run Manually (Test Mode)
python3 /home/admin_user/cronjobs/sync_forever.py


Stop with:
Ctrl + C


Logs:

tail -f ~/persistent_rsync.log
🔄 Run as a systemd Service (Recommended)
1️⃣ Create service file
sudo nano /etc/systemd/system/persistent-rsync.service


[Unit]
Description=Persistent Rsync Screenshot Sync Service
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=admin_user
Group=admin_user
ExecStart=/usr/bin/python3 /home/admin_user/cronjobs/sync_forever.py
Restart=always
RestartSec=10
Environment=PYTHONUNBUFFERED=1
WorkingDirectory=/home/admin_user

[Install]
WantedBy=multi-user.target

2️⃣ Enable & start
sudo systemctl daemon-reload
sudo systemctl enable persistent-rsync
sudo systemctl start persistent-rsync

3️⃣ Check status
systemctl status persistent-rsync

4️⃣ View logs
journalctl -u persistent-rsync -f

🧾 Log Rotation (Prevent Unlimited Log Growth)
Create logrotate config
sudo nano /etc/logrotate.d/persistent-rsync

/home/admin_user/persistent_rsync.log {
    daily
    rotate 14
    compress
    delaycompress
    missingok
    notifempty
    copytruncate
}


Test:
sudo logrotate -d /etc/logrotate.d/persistent-rsync


🔒 Safety Guarantees
Scenario	Behavior
Network down	Waits, retries forever
SSH unavailable	No sync, no deletion
Source folder missing	Auto-created
Files in use	Not deleted until rsync success
Month folder empty	Never deleted
Service crash	Auto-restarted
🧠 Important Design Decisions

systemd over cron → survives reboots
rsync over SCP → efficient & resumable
--remove-source-files → safe move semantics
find -mindepth 1 → folder protection
Dynamic month detection → zero maintenance


🛠️ Common Commands
Restart service
sudo systemctl restart persistent-rsync

Stop service
sudo systemctl stop persistent-rsync

Disable auto-start
sudo systemctl disable persistent-rsync

🚧 Optional Enhancements (Future)
Skip files newer than X seconds
Per-day folders on destination
Failure alerts (mail / Telegram)
systemd CPU / memory limits
SSH key restriction to rsync only

✅ Final Status
This setup is:
✔ Production-ready
✔ Self-healing
✔ Safe against data loss
✔ Zero manual intervention

Author: Prasanna kumar vundaty
Purpose: Screenshot Archival & Cleanup
Stability: Production