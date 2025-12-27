# syncdata

Sync data from WSL to a VPN / remote Linux server.

## 📦 Persistent Rsync Screenshot Sync Service

A **production-grade, self-healing Python service** that continuously syncs screenshots from a Windows machine (via WSL) to a remote Linux server using `rsync`, deletes source files **only after successful transfer**, survives network failures, and **auto-starts on boot using systemd**.

---

## 🚀 Features

- ✅ Runs forever (daemon-style)
- ✅ Auto-detects current month folders (`YYYY-MM`)
- ✅ Waits for network & SSH availability
- ✅ Uses `rsync` for efficient incremental sync
- ✅ Deletes source files only after successful transfer
- ✅ Never deletes the month folder
- ✅ Handles empty / missing folders safely
- ✅ Auto-starts on boot via `systemd`
- ✅ Log rotation via `logrotate`
- ✅ Safe for production use

---

## Overview

**Persistent Rsync Screenshot Sync Service** is a production-grade Python daemon that continuously syncs screenshots from a Windows machine (via WSL) to a remote Linux server using `rsync` over SSH.

The service:
- Moves files safely (copy → verify → delete)
- Survives network failures
- Runs continuously
- Starts automatically on system boot
- Maintains bounded log size

---

## Requirements

### Source Machine (WSL / Linux)

- Python 3.8 or higher
- rsync
- ssh
- systemd

Install dependencies:

```bash
sudo apt update
sudo apt install -y rsync openssh-client
```

### SSH Setup (Mandatory)

**Passwordless SSH is required.**

```bash
ssh-keygen -t ed25519
ssh-copy-id admin@192.168.1.148

# Verify:
ssh -o BatchMode=yes admin@192.168.1.148 echo ok
```

## Running as a systemd Service (Recommended)

Create the service file:

```bash
sudo nano /etc/systemd/system/persistent-rsync.service
```

```ini
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
```

## Enable and start

```bash
sudo systemctl daemon-reload
sudo systemctl enable persistent-rsync
sudo systemctl start persistent-rsync
```

## Check live status

```bash
systemctl status persistent-rsync
```

## View service logs

```bash
journalctl -u persistent-rsync -f
```

## Log Rotation

To prevent unbounded log growth:

```bash
sudo nano /etc/logrotate.d/persistent-rsync
```

```bash
/home/admin_user/persistent_rsync.log {
    daily
    rotate 14
    compress
    delaycompress
    missingok
    notifempty
    copytruncate
}
```

## Test configuration:

```bash
sudo logrotate -d /etc/logrotate.d/persistent-rsync
```

## Common Commands

### Restart service:

```bash
sudo systemctl restart persistent-rsync
```

### Stop service:

```bash
sudo systemctl stop persistent-rsync
```

### Disable auto-start:

```bash
sudo systemctl disable persistent-rsync
```

### Future Improvements

- Skip files newer than a configurable threshold
- Organize destination by day
- Failure notifications (mail / Telegram)
- Resource limits via systemd
- Restrict SSH key to rsync-only usage
