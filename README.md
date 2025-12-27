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

# syncdata

Reliable data synchronization from WSL to a remote Linux (VPN) server.

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


---

## Features

- Runs continuously as a daemon
- Automatically detects monthly folders (YYYY-MM)
- Waits for network and SSH availability
- Uses rsync for efficient incremental transfers
- Deletes source files only after successful transfer
- Never deletes the monthly root folder
- Handles missing or empty folders safely
- Auto-starts on boot using systemd
- Log rotation using logrotate
- Suitable for production environments

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


### SSH Setup (Mandatory)

## Passwordless SSH is required.

ssh-keygen -t ed25519
ssh-copy-id admin@192.168.1.148

# Verify:

ssh -o BatchMode=yes hr306@192.168.1.146 echo ok

