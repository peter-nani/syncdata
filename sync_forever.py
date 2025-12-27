#!/usr/bin/env python3

import subprocess
import time
import os
from datetime import datetime


def get_src():
    month = datetime.now().strftime("%Y-%m")
    return f"/mnt/c/Users/hr306/Downloads/ShareX-18.0.1-portable/ShareX/Screenshots/{month}/"


# ================== CONFIG ==================
DEST = "hr306@192.168.1.146:/home/hr306/git_repos/screenshots/"
SSH_HOST = "hr306@192.168.1.146"
CHECK_INTERVAL = 30      # seconds between retries
SYNC_INTERVAL = 60       # seconds between sync attempts
LOG_FILE = os.path.expanduser("~/persistent_rsync.log")
# ============================================


def log(msg):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {msg}\n")
    print(msg)


def check_ssh_connection():
    """Check SSH connectivity without hanging"""
    try:
        result = subprocess.run(
            ["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=5", SSH_HOST, "echo ok"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return result.returncode == 0
    except Exception:
        return False


def run_rsync():
    #os.makedirs(src, exist_ok=True)
    src = get_src()
    os.makedirs(src, exist_ok=True)
    if not os.path.exists(src):
        log(f"Source directory not found: {src}")
        return False

    cmd = [
        "rsync",
        "-avz",
        "--remove-source-files",
        src,
        DEST
    ]

    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    log(result.stdout)
    if result.returncode != 0:
        log(f"ERROR: rsync failed\n{result.stderr}")
        return False

    subprocess.run(
        ["find", src, "-mindepth", "1", "-type", "d", "-empty", "-delete"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    log("Sync completed successfully")
    return True



def main():
    log("Persistent rsync service started")

    while True:
        if not check_ssh_connection():
            log("Destination unreachable. Waiting for connection...")
            time.sleep(CHECK_INTERVAL)
            continue

        log("Connection established. Starting sync...")
        run_rsync()

        time.sleep(SYNC_INTERVAL)


if __name__ == "__main__":
    main()

