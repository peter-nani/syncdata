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

## Architecture

Windows (ShareX Screenshots)
|
v
WSL Ubuntu (Python Service)
|
v
rsync over SSH
|
v
Remote Linux Server (Archive Storage)