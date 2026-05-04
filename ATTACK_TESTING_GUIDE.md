# Attack Simulation & Testing Guide

## Quick Start: Run Brute-Force Attack Tests

This guide explains how to use the attack simulation scripts to test your IDS/IPS system.

---

## 📋 What's Included

| File | Purpose |
|------|---------|
| `bruteforce_ssh_attack.py` | SSH brute-force attack simulator |
| `bruteforce_rdp_attack.py` | RDP brute-force attack simulator |
| `port_scanner.py` | Port scanning/reconnaissance simulator |
| `run_all_tests.py` | Master test runner orchestrating all attacks |
| `passwords.txt` | Password wordlist for brute-force tests |
| `snort_custom_rules.conf` | Custom Snort IDS rules for detection |

---

## 🚀 Quick Setup

### 1. Install Dependencies

```bash
# For SSH brute-force testing
pip install paramiko

# Verify installation
python3 -c "import paramiko; print('Paramiko installed')"
```

### 2. Prepare Target System

Make sure your target desktop has:
- ✅ SSH enabled on port 22 (or custom port)
- ✅ RDP enabled on port 3389 (or custom port)
- ✅ Snort running in IDS mode
- ✅ Npcap capturing packets

---

## 🔴 SSH Brute-Force Attack

### Test 1: Standard SSH Brute-Force (Detectable)

```bash
# With 1-second delays between attempts
python3 bruteforce_ssh_attack.py \
  --host 192.168.1.100 \
  --port 22 \
  --user admin \
  --wordlist passwords.txt \
  --delay 1
```

**What to expect:**
- Multiple failed SSH authentication attempts
- Snort alerts on repeated failed logins
- System blocks attacker IP after threshold

**Alert Output:**
```
[12:34:56] Attempting: admin:password
[FAILED] Invalid credentials: admin:password
[12:34:57] Attempting: admin:123456
[FAILED] Invalid credentials: admin:123456
...
[SUCCESS] Found credentials: admin:password123
```

---

### Test 2: Rapid SSH Brute-Force (Easy to Detect)

```bash
# 10 attempts per second - very obvious attack
python3 bruteforce_ssh_attack.py \
  --host 192.168.1.100 \
  --port 22 \
  --user admin \
  --rapid \
  --attempts 10
```

**What to expect:**
- Very rapid connection attempts
- Multiple alerts per second
- Immediate detection by IDS

---

## 🔴 RDP Brute-Force Attack

### Test 3: Standard RDP Brute-Force

```bash
# With 0.5-second delays between attempts
python3 bruteforce_rdp_attack.py \
  --host 192.168.1.100 \
  --port 3389 \
  --user admin \
  --wordlist passwords.txt \
  --delay 0.5
```

**What to expect:**
- Multiple RDP connection attempts
- Failed authentication attempts
- Snort detects pattern of failed logins

---

### Test 4: Rapid RDP Brute-Force

```bash
# 50 rapid connection attempts
python3 bruteforce_rdp_attack.py \
  --host 192.168.1.100 \
  --port 3389 \
  --user admin \
  --rapid \
  --attempts 50
```

---

## 🔴 Port Scanning / Reconnaissance

### Test 5: Scan Common Ports

```bash
# Scan well-known service ports
python3 port_scanner.py \
  --host 192.168.1.100 \
  --common
```

**Ports scanned:** 21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3306, 3389, 5432, 5900, 8080, 8443

---

### Test 6: Scan Port Range

```bash
# Scan ports 1-1000
python3 port_scanner.py \
  --host 192.168.1.100 \
  --range 1 1000
```

---

### Test 7: Rapid Port Scan (Obvious)

```bash
# Very rapid scanning - easy to detect
python3 port_scanner.py \
  --host 192.168.1.100 \
  --ports 1-1000 \
  --rapid
```

---

## 🎮 Interactive Test Suite

Run all tests with a menu interface:

```bash
# Start interactive menu
python3 run_all_tests.py --host 192.168.1.100 --interactive

# With monitoring (pauses before each test for Snort setup)
python3 run_all_tests.py --host 192.168.1.100 --monitor --interactive
```

**Menu Options:**
```
1. SSH Brute-Force (Standard)
2. SSH Brute-Force (Rapid)
3. RDP Brute-Force (Standard)
4. RDP Brute-Force (Rapid)
5. Port Scan (Common Ports)
6. Port Scan (Range 20-100)
7. Port Scan (Rapid 1-1000)
8. Run All Tests
9. Exit
```

---

## ⚙️ Advanced Options

### SSH Attack - Custom Port

```bash
python3 bruteforce_ssh_attack.py \
  --host 192.168.1.100 \
  --port 2222 \
  --user root \
  --wordlist passwords.txt \
  --delay 2
```

### SSH Attack - Different User

```bash
python3 bruteforce_ssh_attack.py \
  --host 192.168.1.100 \
  --user admin \
  --wordlist passwords.txt
```

### RDP Attack - Custom Timeout

```bash
python3 bruteforce_rdp_attack.py \
  --host 192.168.1.100 \
  --port 3389 \
  --delay 1
```

### Port Scan - Specific Ports

```bash
# Scan only SSH, HTTP, HTTPS, RDP
python3 port_scanner.py \
  --host 192.168.1.100 \
  --ports 22,80,443,3389
```

---

## 📊 Monitoring & Logs

### Snort Log Locations

**Linux:**
```bash
# View alerts
tail -f /var/log/snort/alert

# Check full logs
tail -f /var/log/snort/snort.log.1234567890

# Search for specific attacks
grep "SSH" /var/log/snort/alert
grep "RECONNAISSANCE" /var/log/snort/alert
```

**Windows:**
```
C:\Snort\log\alert
C:\Snort\log\snort.log
```

---

### Start Snort Before Testing

```bash
# Linux - IDS Mode (Monitor only)
sudo snort -A full -l /var/log/snort -c /etc/snort/snort.conf -i eth0

# Windows - IDS Mode
snort -A full -l C:\Snort\log -c C:\Snort\etc\snort.conf

# With custom rules file
snort -A full -l /var/log/snort -c snort_custom_rules.conf -i eth0
```

---

### View Results While Testing

**Terminal 1: Run Test**
```bash
python3 bruteforce_ssh_attack.py --host 192.168.1.100 --user admin --wordlist passwords.txt
```

**Terminal 2: Monitor Snort Alerts**
```bash
# Linux
tail -f /var/log/snort/alert

# Or in real-time
snort -r /var/log/snort/snort.log.1234567890 -A console
```

---

## 📈 Expected Snort Alerts

### SSH Brute-Force Alert

```
[**] [1:3000002:1] SSH BRUTE-FORCE Possible Brute Force Attack Detected [**]
[Classification: Attempted User Privilege Gain] [Priority: 1]
05/04-14:32:15.234567 192.168.1.100:54321 -> 192.168.1.1:22
TCP TTL:64 TOS:0x0 ID:1234 IpLen:20 DgmLen:60
```

### Port Scanning Alert

```
[**] [1:3000012:1] RECONNAISSANCE Port Scanning Activity Detected [**]
[Classification: Attempted Information Leak] [Priority: 2]
05/04-14:33:45.123456 192.168.1.100:60000 -> 192.168.1.1:[various ports]
TCP TTL:64 TOS:0x0 ID:5678 IpLen:20 DgmLen:60
```

---

## 🔧 Troubleshooting

### Script Requires Python 3.6+

```bash
# Check Python version
python3 --version

# If not installed, install Python 3
# Ubuntu/Debian:
sudo apt install python3 python3-pip

# macOS:
brew install python3

# Windows:
# Download from python.org
```

### Paramiko Not Found

```bash
# Install paramiko
pip3 install paramiko

# Verify
python3 -c "import paramiko; print(paramiko.__version__)"
```

### Connection Refused

- Verify target SSH/RDP service is running
- Check firewall rules (Windows Defender, iptables)
- Verify port numbers are correct
- Check network connectivity: `ping <target-ip>`

### Snort Not Detecting

- Make sure Snort is running: `ps aux | grep snort`
- Verify Snort config includes custom rules
- Check Snort has proper interface: `-i eth0` (verify with `ifconfig`)
- Review Snort logs for errors: `/var/log/snort/snort.log.*`

---

## 📋 Test Checklist

Before running tests:

- [ ] Target system accessible via network
- [ ] SSH/RDP services running (if testing those)
- [ ] Snort daemon running
- [ ] Npcap capturing packets
- [ ] Custom rules loaded in Snort
- [ ] Firewall not blocking attack traffic
- [ ] Sufficient disk space for logs
- [ ] Proper permissions to run scripts

---

## ✅ Success Indicators

### Successful SSH Brute-Force Detection

- [ ] Snort generates alerts for repeated failed logins
- [ ] Alerts show source IP of attacker
- [ ] Alerts include timestamp and port number
- [ ] Alert shows "SSH" or "BRUTE-FORCE" in message

### Successful Port Scan Detection

- [ ] Snort alerts on multiple connections within time window
- [ ] Alerts show "RECONNAISSANCE" or "portscan"
- [ ] Alerts track by source IP
- [ ] Pattern shows multiple different ports being probed

---

## 🔐 Security Notes

⚠️ **WARNING:**
- Only test on systems you own or have written permission to test
- Do not run these scripts on production systems
- Ensure your lab environment is isolated from the internet
- Do not publish IP addresses from real attacks
- Document all testing with timestamps and results

---

## 📝 Data Collection for Analysis

Recommended data to collect during each test:

```
Test Date & Time: [YYYY-MM-DD HH:MM:SS]
Test Type: [SSH/RDP/Port Scan]
Target: [IP:PORT]
Attack Duration: [seconds]
Total Attempts: [number]
Attacks Detected: [number]
Detection Time: [seconds to first alert]
Alerts Generated: [count]
False Positives: [count]
System Impact: [CPU%, Memory%]
```

---

**Last Updated:** May 4, 2026  
**Status:** Ready for Testing ✅
