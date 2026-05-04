# Technical Setup & Implementation Guide

## Project: Applying Firewalls and IDS/IPS Systems to Enhance Network Security on a Personal Desktop

---

## System Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                    THREAT SOURCES                             │
│        (Port Scanners, Malware, Brute-Force, etc.)           │
└──────────────────────────────────┬──────────────────────────┘
                                   ↓
        ┌─────────────────────────────────────────────┐
        │   LAYER 1: FIREWALL (Traffic Control)       │
        │   Windows Defender Firewall                 │
        │   - Block unnecessary ports                 │
        │   - Restrict unknown IPs                    │
        │   - Protect SSH/RDP services                │
        │   - Limit login attempts                    │
        └─────────────────────────────────────────────┘
                          ↓
        ┌─────────────────────────────────────────────┐
        │   PACKET INTERCEPTION LAYER                 │
        │   Npcap (Packet Capture Driver)             │
        │   - Captures all network packets            │
        │   - Feeds data to IDS/IPS engine            │
        └─────────────────────────────────────────────┘
                          ↓
        ┌─────────────────────────────────────────────┐
        │   LAYER 2: IDS/IPS (Deep Analysis)          │
        │   Snort Engine with Custom Rules            │
        │   - Signature-based detection               │
        │   - Anomaly detection                       │
        │   - Real-time alerting                      │
        │   - Optional packet blocking (IPS mode)     │
        └─────────────────────────────────────────────┘
                          ↓
        ┌─────────────────────────────────────────────┐
        │   LOGGING & ANALYSIS LAYER                  │
        │   System Logs & Alert Database              │
        │   - Detection records                       │
        │   - Attack patterns                         │
        │   - Metrics & statistics                    │
        └─────────────────────────────────────────────┘
                          ↓
        ┌─────────────────────────────────────────────┐
        │   PROTECTED PERSONAL DESKTOP                │
        └─────────────────────────────────────────────┘
```

---

## Component Details

### 1. Windows Defender Firewall

**Purpose:** Initial network traffic filtering

**Configuration:**

```
✓ Enable Firewall on all networks
✓ Block all inbound connections by default
✓ Allow necessary outbound connections:
  - SSH (port 22) - restricted
  - RDP (port 3389) - restricted
  - HTTPS (port 443) - monitored
  - DNS (port 53) - monitored
✓ Block suspicious IPs after detected attacks
✓ Log all blocked connections
```

**Limitations Identified:**

- ❌ Cannot detect malware using legitimate ports (HTTPS 443)
- ❌ No deep packet inspection
- ❌ Signature-based only
- ❌ Misses encrypted threat content

---

### 2. Npcap - Packet Capture Driver

**Purpose:** Intercept and capture network packets

**Function:** Acts as a "stealth camera" for the IDS/IPS system

**Installation & Configuration:**

```bash
# Download Npcap from: https://npcap.org/
# Install with administrator privileges
# Verify installation: npcap-config --show-driver-version

# Basic packet capture syntax:
dumpcap -i [interface] -f [filter] -w [output-file]

# Example: Capture traffic on local network adapter
dumpcap -i Ethernet -f "tcp port 443" -w malware_traffic.pcapng
```

**Captured Data:**

- Source and destination IP addresses
- Protocol type (TCP, UDP, ICMP, etc.)
- Port numbers
- Packet payload (encrypted or plaintext)
- Timestamps of packet transmission

---

### 3. Snort - IDS/IPS Engine

**Purpose:** Real-time network traffic analysis and threat detection

**Operating Modes:**

#### Mode 1: IDS (Intrusion Detection System) - CURRENT

```bash
# Run as IDS - Monitor and Alert only
snort -A full -l /var/log/snort -c /etc/snort/snort.conf -i eth0

# Reads traffic from Npcap or pcap files
# Generates alerts without blocking
# Safe for lab testing environment
```

**Advantages:**

- ✅ Non-disruptive to network
- ✅ Real-time monitoring
- ✅ Comprehensive logging
- ✅ Low false positive impact

#### Mode 2: IPS (Intrusion Prevention System) - PRODUCTION READY

```bash
# Run as IPS - Inline blocking mode
# Requires configuration change in custom rules:
# Change: alert tcp any any -> any 443
# To: drop tcp any any -> any 443

snort -Q -i eth0 --daq-dir=/usr/local/lib/daq --daq nfq --daq-mode inline

# Now actively DROPS (blocks) matching packets
# Prevents malicious traffic at gateway
```

**Advantages:**

- ✅ Active threat mitigation
- ✅ Blocks malicious packets in real-time
- ✅ Prevents C2 communication
- ✅ Stops brute-force attempts

---

### 4. Snort Custom Rules

**Rule Format:**

```
[action] [protocol] [src_ip] [src_port] -> [dst_ip] [dst_port]
([options])

# Actions: alert, drop, reject, pass, log
# Protocols: tcp, udp, icmp, ip
```

#### Rule Set 1: Malware C2 Detection

```snort
# Detect suspicious HTTPS beaconing (Flightsim behavior)
alert tcp any any -> any 443 (
  msg:"MALWARE-CNC Suspicious HTTPS C2 Activity";
  flow:to_server,established;
  content:"GET"; http_method;
  content:"User-Agent|3a| "; http_header;
  classtype:trojan-activity;
  sid:1000001; rev:1; priority:2;
)

# Detect high-frequency outbound DNS queries
alert udp any any -> any 53 (
  msg:"MALWARE-DNS Suspicious DNS Beaconing";
  content:"|01 00|";
  offset:2; depth:2;
  threshold: type both, track by_src, count 10, seconds 60;
  classtype:suspicious-dns;
  sid:1000002; rev:1; priority:2;
)

# Detect unusual outbound traffic patterns
alert tcp any any -> any !80:445 (
  msg:"MALWARE-TRAFFIC Unusual Outbound Traffic";
  flow:to_server;
  byte_extract:1,0,byte_val,relative;
  classtype:suspicious-traffic;
  sid:1000003; rev:1; priority:3;
)
```

#### Rule Set 2: Brute-Force Detection

```snort
# SSH brute-force attempt detection
alert tcp any any -> any 22 (
  msg:"ATTACK-SSH Brute Force Attempt Detected";
  flow:to_server,established;
  content:"Invalid user"; msg:"SSH authentication failure";
  threshold: type both, track by_src, count 5, seconds 60;
  classtype:attempted-user;
  sid:2000001; rev:1; priority:1;
)

# RDP brute-force attempt detection
alert tcp any any -> any 3389 (
  msg:"ATTACK-RDP Brute Force Attempt Detected";
  flow:to_server,established;
  threshold: type both, track by_src, count 10, seconds 60;
  classtype:attempted-admin;
  sid:2000002; rev:1; priority:1;
)

# Multiple failed login attempts
alert tcp any any -> any 22 (
  msg:"ATTACK-SSH Multiple Failed Logins";
  flow:to_server,established;
  content:"Failed";
  threshold: type threshold, track by_src, count 3, seconds 10;
  classtype:attempted-user;
  sid:2000003; rev:1; priority:1;
)
```

#### Rule Set 3: Reconnaissance Detection

```snort
# Port scanning detection
alert tcp any any -> any any (
  msg:"RECONNAISSANCE Port Scan Detected";
  flow:to_server,new;
  flags:S;
  threshold: type both, track by_src, count 20, seconds 30;
  classtype:attempted-recon;
  sid:3000001; rev:1; priority:2;
)

# Nmap NULL flag scan
alert tcp any any -> any any (
  msg:"RECONNAISSANCE Nmap NULL Scan";
  flow:to_server,new;
  flags:0;
  classtype:attempted-recon;
  sid:3000002; rev:1; priority:2;
)
```

---

## Test Scenarios & Execution

### Test 1: Malware Detection (Flightsim)

**Setup:**

1. Start Npcap in capture mode
2. Start Snort in IDS mode
3. Run Flightsim malware simulator
4. Monitor Snort alerts in real-time

**Expected Flow:**

```
Flightsim generates malicious traffic
        ↓
Firewall (may pass legitimate-looking HTTPS traffic)
        ↓
Npcap captures the packets
        ↓
Snort analyzes with custom rules
        ↓
Snort detects C2 beaconing pattern
        ↓
Alert generated with details
        ↓
Log entry created for analysis
```

**Alert Output Example:**

```
[**] [1:1000001:1] MALWARE-CNC Suspicious HTTPS C2 Activity [**]
[Classification: Trojan activity] [Priority: 2]
05/04-14:32:15.234567 192.168.1.100:54321 -> 203.0.113.45:443
```

### Test 2: Brute-Force Attack Detection

**Setup:**

1. Simulate multiple failed SSH/RDP logins
2. Monitor firewall and Snort responses
3. Record blocking time and accuracy

**Expected Detection:**

- Alert after 5-10 failed attempts
- Automatic IP blocking (optional in IPS mode)
- Alert includes attacker IP and attempt count

### Test 3: Port Scanning Detection

**Setup:**

1. Run port scanner against desktop
2. Monitor Snort for scanning pattern detection
3. Record detection accuracy

**Expected Detection:**

- Detect rapid sequential port probes
- Alert on suspicious scanning patterns
- Block attacker IP after threshold

---

## Log File Locations

```
Windows Firewall Logs:
C:\Windows\System32\LogFiles\Firewall\

Snort Alert Logs:
/var/log/snort/alert  (Linux)
C:\Snort\log\  (Windows)

Npcap Capture Files:
[Output directory specified during capture]

System Event Logs:
Event Viewer → Windows Logs → Security
```

---

## Key Implementation Notes

✅ **Isolation:** Lab environment is isolated from production networks  
✅ **Customization:** Snort rules are organization-specific  
✅ **Flexibility:** Can switch from IDS to IPS by changing rule actions  
✅ **Scalability:** Model can be extended to enterprise environments  
✅ **Logging:** Comprehensive audit trail for analysis

---

## Configuration Files

### Snort Configuration (snort.conf)

```
# Set HOME_NET to local network
var HOME_NET 192.168.1.0/24
var EXTERNAL_NET !$HOME_NET

# Include custom rules
include /etc/snort/rules/custom_rules.conf

# Logging settings
output alert_full: stdout

# Performance monitoring
config profile_rules: print all

# Plugin configuration
preprocessor http_inspect: global \
    iis_unicode_map unicode.map 1252
```

---

**Last Updated:** May 4, 2026  
**Status:** Documentation Complete - Awaiting Full Deployment
