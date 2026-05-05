#!/usr/bin/env python3
"""
Safe terminal demo for brute-force Blue Force screenshots.

This script does not perform any network attack and does not run Snort.
It only prints simulated terminal output so the workflow can be shown in
presentations or drafts. Do not submit this output as real evidence.
"""

import argparse
import sys
import time
from datetime import datetime


def slow_print(line="", delay=0.05):
    print(line, flush=True)
    if delay:
        time.sleep(delay)


def header(title):
    slow_print("=" * 78, 0)
    slow_print(title, 0)
    slow_print("=" * 78, 0)


def subheader(title):
    slow_print("")
    slow_print("-" * 78, 0)
    slow_print(title, 0)
    slow_print("-" * 78, 0)


def snort_setup(show_header=True):
    if show_header:
        header("SCREENSHOT 1 - BLUE FORCE SNORT INTERFACE SETUP")
        slow_print("Purpose: identify the correct Npcap interface and start Snort IDS mode.")
        slow_print("")

    slow_print("Microsoft Windows [Version 10.0.22631.3593]")
    slow_print("(c) Microsoft Corporation. All rights reserved.")
    slow_print("")
    subheader("Step 1. List Snort/Npcap interfaces")
    slow_print(r"C:\Windows\System32>cd C:\Snort\bin")
    slow_print(r"C:\Snort\bin>snort -W")
    slow_print("")
    slow_print("   ,,_     -*> Snort! <*-")
    slow_print("  o\"  )~   Version 2.9.20-WIN64 GRE (Build 82)")
    slow_print("   ''''    By Martin Roesch & The Snort Team")
    slow_print("")
    slow_print("Index   Physical Address    IP Address       Device Name                    Description")
    slow_print("-----   ----------------    ----------       -----------                    -----------")
    slow_print("1       00:00:00:00:00:00   disabled         \\Device\\NPF_{75FBB4DD...}     WAN Miniport")
    slow_print("2       00:00:00:00:00:00   disabled         \\Device\\NPF_{5ACE0ECA...}     WAN Miniport (IPv6)")
    slow_print("3       00:00:00:00:00:00   disabled         \\Device\\NPF_{79CC0AAC...}     WAN Miniport (IP)")
    slow_print("4       B0:68:E6:CB:B7:E5   192.168.51.109   \\Device\\NPF_{8FC304A4...}     Realtek 8822BE Wireless LAN 802.11ac PCI-E NIC")
    slow_print("5       F2:68:E6:CB:B7:E5   169.254.111.230  \\Device\\NPF_{D29EC5A1...}     Microsoft Wi-Fi Direct Virtual Adapter")
    slow_print("")
    subheader("Step 2. Start Snort on interface 4 in IDS console mode")
    slow_print(r"C:\Snort\bin>snort -i 4 -c C:\Snort\etc\demo.conf -A console -N")
    slow_print("")
    slow_print("[*] Snort IDS console mode started on interface 4")
    slow_print("[*] Waiting for SSH/RDP brute-force traffic...")
    slow_print("")
    slow_print("NOTE: SIMULATED DEMO OUTPUT - not real Snort evidence")


def snort_alerts(show_header=True):
    if show_header:
        header("SCREENSHOT 3 - BLUE FORCE SNORT BRUTE-FORCE ALERTS")
        slow_print("Purpose: show expected IDS alerts for SSH/RDP brute-force behavior.")
        slow_print("")

    slow_print("WARNING: No preprocessors configured for policy 0.")
    slow_print("WARNING: No preprocessors configured for policy 0.")
    slow_print("NOTE: SIMULATED DEMO OUTPUT - not real Snort evidence")
    slow_print("")

    alerts = [
        (
            "05/04-09:32:19.102001",
            "1:3000002:1",
            "SSH BRUTE-FORCE Possible Brute Force Attack Detected",
            "192.168.51.109:51422",
            "192.168.1.100:22",
        ),
        (
            "05/04-09:32:20.331820",
            "1:3000003:1",
            "SSH Failed Login Attempt",
            "192.168.51.109:51426",
            "192.168.1.100:22",
        ),
        (
            "05/04-09:32:22.884501",
            "1:3000004:1",
            "SSH RAPID Multiple Connections from Same Source",
            "192.168.51.109:51440",
            "192.168.1.100:22",
        ),
        (
            "05/04-09:32:36.774300",
            "1:3000006:1",
            "RDP BRUTE-FORCE Multiple Connections Detected",
            "192.168.51.109:51512",
            "192.168.1.100:3389",
        ),
        (
            "05/04-09:32:38.990241",
            "1:3000007:1",
            "RDP BRUTE-FORCE Rapid Connection Attempts",
            "192.168.51.109:51530",
            "192.168.1.100:3389",
        ),
    ]

    for ts, sid, msg, src, dst in alerts:
        if "3000002" in sid:
            subheader("SSH standard brute-force detection")
        elif "3000004" in sid:
            subheader("SSH rapid brute-force detection")
        elif "3000006" in sid:
            subheader("RDP repeated connection detection")
        elif "3000007" in sid:
            subheader("RDP rapid connection detection")
        slow_print(f"{ts} [**] [{sid}] {msg} [**] [Priority: 1]")
        slow_print(f"{{TCP}} {src} -> {dst}")
        slow_print("")
        time.sleep(0.8)

    slow_print("[*] Alert Summary")
    slow_print("    SSH brute-force alerts: 3")
    slow_print("    RDP brute-force alerts: 2")
    slow_print("    Total brute-force alerts: 5")
    slow_print("    Detection mode: IDS alerting")
    slow_print("    Blocking status: response path prepared, not proven in this demo")


def attack_output(show_header=True):
    if show_header:
        header("SCREENSHOT 2 - ATTACK-SIDE BRUTE-FORCE EXECUTION")
        slow_print("Purpose: show generated SSH/RDP attempts and measured success rate.")
        slow_print("")

    slow_print("Windows PowerShell")
    slow_print("Copyright (C) Microsoft Corporation. All rights reserved.")
    slow_print("")
    subheader("Test 1. SSH standard brute-force")
    slow_print(r"PS C:\Users\admin\Desktop\Security> python3 bruteforce_ssh_attack.py --host 192.168.1.100 --port 22 --user admin --wordlist passwords.txt --delay 1")
    slow_print("")
    slow_print("[*] Target: 192.168.1.100:22")
    slow_print("[*] Username: admin")
    slow_print("[*] Mode: SSH standard brute-force")
    slow_print("[*] NOTE: SIMULATED DEMO OUTPUT - no network attack is performed")
    slow_print("")
    for i in range(1, 11):
        slow_print(f"[09:32:{17+i:02d}] admin:password{i:03d}", 0.08)
    slow_print("[*] Progress: 100/100")
    slow_print("")
    slow_print("Attempts: 100")
    slow_print("Successful: 0")
    slow_print("Duration: 45.20s")
    slow_print("Rate: 2.21/s")
    slow_print("")

    subheader("Test 2. SSH rapid brute-force")
    slow_print(r"PS C:\Users\admin\Desktop\Security> python3 bruteforce_ssh_attack.py --host 192.168.1.100 --port 22 --user admin --rapid --attempts 10")
    slow_print("")
    slow_print("[*] Target: 192.168.1.100:22")
    slow_print("[*] Mode: SSH rapid brute-force")
    slow_print("[*] Attempts per second: 10")
    slow_print("")
    for i in range(1, 11):
        slow_print(f"[09:32:{28+i:02d}] admin:password{i}", 0.04)
    slow_print("[*] Progress: 100/100")
    slow_print("")
    slow_print("Attempts: 100")
    slow_print("Successful: 0")
    slow_print("Duration: 10.10s")
    slow_print("Rate: 9.90/s")
    slow_print("")

    subheader("Test 3. RDP standard brute-force")
    slow_print(r"PS C:\Users\admin\Desktop\Security> python3 bruteforce_rdp_attack.py --host 192.168.1.100 --port 3389 --user admin --wordlist passwords.txt --delay 0.5")
    slow_print("")
    slow_print("[*] Starting RDP Brute-Force Test")
    slow_print("[*] Target: 192.168.1.100:3389")
    slow_print("[*] Username: admin")
    slow_print("")
    for i in range(1, 6):
        slow_print(f"[09:32:{39+i:02d}] RDP Connection attempt: admin:Password{i}", 0.08)
    slow_print("[*] Progress: 50/50 attempts")
    slow_print("")
    slow_print("RDP ATTACK SUMMARY")
    slow_print("Total Attempts:       50")
    slow_print("Successful:           0")
    slow_print("Duration:             25.50 seconds")
    slow_print("Attack Rate:          1.96 attempts/second")
    slow_print("")
    subheader("Final brute-force result summary")
    slow_print("BRUTE-FORCE TEST SUMMARY")
    slow_print("Total SSH Attempts:   200")
    slow_print("Total RDP Attempts:   50")
    slow_print("Total Attempts:       250")
    slow_print("Successful Attempts:  0")
    slow_print("Success Rate:         0%")


def firewall_output(show_header=True):
    if show_header:
        header("SCREENSHOT 4 - FIREWALL BLOCK RESPONSE DESIGN")
        slow_print("Purpose: show the command used to block a confirmed brute-force source IP.")
        slow_print("")

    slow_print("Windows PowerShell")
    slow_print("")
    subheader("Step 1. Add inbound block rule for the suspicious source")
    slow_print(r"PS C:\Windows\system32> New-NetFirewallRule `")
    slow_print('>>   -DisplayName "Block brute-force source" `')
    slow_print(">>   -Direction Inbound `")
    slow_print(">>   -RemoteAddress 192.168.51.109 `")
    slow_print(">>   -Action Block")
    slow_print("")
    slow_print("Name                  : {8f0f4c5a-demo-rule}")
    slow_print("DisplayName           : Block brute-force source")
    slow_print("Enabled               : True")
    slow_print("Direction             : Inbound")
    slow_print("Action                : Block")
    slow_print("Status                : The rule was parsed successfully from the store.")
    slow_print("")
    subheader("Step 2. Verify the blocked source IP")
    slow_print(r"PS C:\Windows\system32> Get-NetFirewallRule -DisplayName ""Block brute-force source"" | Get-NetFirewallAddressFilter")
    slow_print("")
    slow_print("LocalAddress          : Any")
    slow_print("RemoteAddress         : 192.168.51.109")
    slow_print("")
    slow_print("NOTE: SIMULATED DEMO OUTPUT - use real firewall logs for final proof")


def combined():
    header("LEFT TERMINAL: ATTACK SIMULATION")
    attack_output(show_header=False)
    slow_print("")
    header("RIGHT TERMINAL: SNORT IDS ALERTS")
    snort_alerts(show_header=False)


def main():
    parser = argparse.ArgumentParser(description="Safe brute-force Blue Force terminal demo")
    parser.add_argument(
        "--view",
        choices=["snort-setup", "snort-alerts", "attack", "firewall", "combined"],
        default="combined",
        help="Demo output to print",
    )
    args = parser.parse_args()

    if args.view == "snort-setup":
        snort_setup()
    elif args.view == "snort-alerts":
        snort_alerts()
    elif args.view == "attack":
        attack_output()
    elif args.view == "firewall":
        firewall_output()
    elif args.view == "combined":
        combined()
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
