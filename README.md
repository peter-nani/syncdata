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

## 🧱 Architecture Overview

Windows (ShareX Screenshots)
↓
WSL Ubuntu (Python Service)
↓
rsync over SSH
↓
Remote Linux Server (Archive Storage)


---

## 📂 Directory Structure

/home/admin_user/
├── cronjobs/
│ └── sync_forever.py
├── persistent_rsync.log


---

## ⚙️ Requirements

### Source Machine (WSL / Linux)

- Python **3.8+**
- `rsync`
- `ssh`
- `systemd` (for service mode)

```bash
sudo apt update
sudo apt install -y rsync openssh-client

Destination Server

SSH server running

Target directory exists

SSH key-based login enabled

🔐 SSH Setup (MANDATORY)

Passwordless SSH is required.

ssh-keygen -t ed25519
ssh-copy-id hr306@192.168.1.146
