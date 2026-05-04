# Complete Attack Simulation & Data Analysis Workflow

**Project:** Applying Firewalls and IDS/IPS Systems to Enhance Network Security on a Personal Desktop

---

## 🎯 Overview

This document provides a complete end-to-end workflow for:
1. Executing attack simulations (Malware, Brute-Force, Port Scanning)
2. Collecting detection data from Snort IDS/IPS
3. Analyzing effectiveness metrics
4. Generating comprehensive reports

---

## 📋 Pre-Test Checklist

### System Setup
- [ ] Target system: Ubuntu/Windows with SSH/RDP enabled
- [ ] Snort installed and configured
- [ ] Npcap installed for packet capture
- [ ] Python 3.6+ installed
- [ ] Paramiko library installed (`pip3 install paramiko`)
- [ ] Network connectivity verified (`ping` target system)

### Configuration Files
- [ ] `snort_custom_rules.conf` loaded into Snort
- [ ] Firewall rules configured
- [ ] Logging directories created: `/var/log/snort/`
- [ ] Output directory created: `test_results/`

### Documentation
- [ ] Print or open `ATTACK_SIMULATION_RESULTS.md` template
- [ ] Prepare `passwords.txt` wordlist
- [ ] Have test scripts ready: `bruteforce_*.py`, `port_scanner.py`

---

## 🚀 Execution Workflow

### Phase 1: Preparation (15 minutes)

**Terminal 1 - System Baseline**
```bash
# Monitor system before tests
watch -n 1 'free -h && echo "---" && top -b -n 1 | head -20'
```

**Terminal 2 - Snort Setup**
```bash
# Start Snort IDS in logging mode
sudo snort -A full -l /var/log/snort -c snort_custom_rules.conf -i eth0

# Or on Windows
snort -A full -l C:\Snort\log -c C:\Snort\etc\snort.conf
```

**Terminal 3 - Packet Capture**
```bash
# Start packet capture with Npcap
# Alternatively use tcpdump:
sudo tcpdump -i eth0 -w attack_capture.pcap

# Or dumpcap:
sudo dumpcap -i eth0 -w attack_capture.pcapng
```

**Terminal 4 - Verify Setup**
```bash
# Check Snort is running
ps aux | grep snort

# Check network connectivity
ping 192.168.1.100

# List available interfaces
ip addr show
```

---

### Phase 2: Execute Attack Tests (45 minutes)

#### Test 1: Malware C2 Simulation (Flightsim)

```bash
# Terminal 5 - Start Flightsim (example with safe behavior)
# This would require Flightsim tool installed
# ./flightsim c2

# Record in ATTACK_SIMULATION_RESULTS.md:
# - Start time
# - Number of C2 beacons
# - Ports used
# - Durations
```

**Expected Snort Alerts:**
```
[1:1000001] MALWARE-CNC Suspicious HTTPS C2 Activity
[1:1000002] MALWARE-DNS Suspicious DNS Beaconing
```

#### Test 2: SSH Brute-Force (Standard)

```bash
# Terminal 5 - Run SSH attack
python3 bruteforce_ssh_attack.py \
  --host 192.168.1.100 \
  --port 22 \
  --user admin \
  --wordlist passwords.txt \
  --delay 1 2>&1 | tee ssh_bruteforce_standard.log

# Record: Timestamp when started and any alerts received
```

#### Test 3: SSH Brute-Force (Rapid)

```bash
# Wait 30 seconds after Test 2
sleep 30

# Run rapid SSH attack
python3 bruteforce_ssh_attack.py \
  --host 192.168.1.100 \
  --port 22 \
  --user admin \
  --rapid \
  --attempts 10 2>&1 | tee ssh_bruteforce_rapid.log
```

#### Test 4: RDP Brute-Force (Standard)

```bash
# Wait 30 seconds
sleep 30

# Run RDP attack (standard)
python3 bruteforce_rdp_attack.py \
  --host 192.168.1.100 \
  --port 3389 \
  --user admin \
  --wordlist passwords.txt \
  --delay 0.5 2>&1 | tee rdp_bruteforce_standard.log
```

#### Test 5: RDP Brute-Force (Rapid)

```bash
# Wait 30 seconds
sleep 30

# Run RDP attack (rapid)
python3 bruteforce_rdp_attack.py \
  --host 192.168.1.100 \
  --port 3389 \
  --user admin \
  --rapid \
  --attempts 50 2>&1 | tee rdp_bruteforce_rapid.log
```

#### Test 6: Port Scan (Common Ports)

```bash
# Wait 30 seconds
sleep 30

# Scan common ports
python3 port_scanner.py \
  --host 192.168.1.100 \
  --common 2>&1 | tee port_scan_common.log
```

#### Test 7: Port Scan (Range 1-100)

```bash
# Wait 15 seconds
sleep 15

# Scan port range
python3 port_scanner.py \
  --host 192.168.1.100 \
  --range 1 100 2>&1 | tee port_scan_range.log
```

#### Test 8: Port Scan (Rapid 1-1000)

```bash
# Wait 15 seconds
sleep 15

# Rapid port scan
python3 port_scanner.py \
  --host 192.168.1.100 \
  --ports 1-1000 \
  --rapid 2>&1 | tee port_scan_rapid.log
```

---

### Phase 3: Data Collection (30 minutes)

#### Step 1: Export Snort Alerts

```bash
# Copy Snort alert log
cp /var/log/snort/alert test_results/snort_alerts_raw.log

# Parse with data collector (we'll create a parser)
python3 data_collector.py --parse-snort test_results/snort_alerts_raw.log
```

#### Step 2: Extract Attack Logs

```bash
# Consolidate all attack logs
cat ssh_bruteforce_standard.log >> test_results/attack_logs.txt
cat ssh_bruteforce_rapid.log >> test_results/attack_logs.txt
cat rdp_bruteforce_standard.log >> test_results/attack_logs.txt
cat rdp_bruteforce_rapid.log >> test_results/attack_logs.txt
cat port_scan_common.log >> test_results/attack_logs.txt
cat port_scan_range.log >> test_results/attack_logs.txt
cat port_scan_rapid.log >> test_results/attack_logs.txt
```

#### Step 3: Collect System Metrics

```bash
# Export network statistics
netstat -i > test_results/netstat_final.txt

# Export process information
ps aux > test_results/processes_final.txt

# Export system information
uname -a > test_results/system_info.txt
```

#### Step 4: Package Packet Captures

```bash
# Stop tcpdump/dumpcap (Ctrl+C in Terminal 3)
# Move pcap files
mv attack_capture.pcap* test_results/

# Optional: Convert to readable format
wireshark -r test_results/attack_capture.pcap -w test_results/attacks.csv
```

---

### Phase 4: Data Analysis (60 minutes)

#### Step 1: Parse Snort Alerts

```bash
# Run data collector to parse all alerts
python3 data_collector.py \
  --snort-log test_results/snort_alerts_raw.log \
  --output test_results/snort_alerts.csv
```

#### Step 2: Generate Report

```bash
# Generate comprehensive HTML report
python3 data_collector.py \
  --results test_results/test_results.csv \
  --alerts test_results/snort_alerts.csv \
  --report test_results/analysis_report.html
```

#### Step 3: Calculate Metrics

```bash
# Analyze effectiveness
python3 << 'EOF'
import csv
import json
from collections import defaultdict

# Read test results
tests = []
with open('test_results/test_results.csv', 'r') as f:
    reader = csv.DictReader(f)
    tests = list(reader)

# Read Snort alerts
alerts = []
with open('test_results/snort_alerts.csv', 'r') as f:
    reader = csv.DictReader(f)
    alerts = list(reader)

# Calculate metrics
total_alerts = len(alerts)
alerts_by_priority = defaultdict(int)
alerts_by_type = defaultdict(int)

for alert in alerts:
    alerts_by_priority[alert['priority']] += 1
    alerts_by_type[alert['message'][:30]] += 1  # First 30 chars of message

print("\n" + "="*70)
print("METRICS SUMMARY")
print("="*70)
print(f"Total Tests: {len(tests)}")
print(f"Total Alerts: {total_alerts}")
print(f"Average Alerts per Test: {total_alerts/max(len(tests),1):.1f}")
print("\nAlerts by Priority:")
for p, count in sorted(alerts_by_priority.items()):
    priority_name = {1: "HIGH", 2: "MEDIUM", 3: "LOW"}
    print(f"  {priority_name.get(int(p), 'UNKNOWN')}: {count}")
print("\nTop Attack Types:")
for attack_type, count in sorted(alerts_by_type.items(), key=lambda x: x[1], reverse=True)[:5]:
    print(f"  {attack_type}: {count}")
print("="*70 + "\n")
EOF
```

#### Step 4: Fill Results Template

```bash
# Open and fill the template
# ATTACK_SIMULATION_RESULTS.md
nano ATTACK_SIMULATION_RESULTS.md

# Key sections to populate:
# - Test execution details
# - Detection timelines
# - Alert counts
# - False positive analysis
# - Effectiveness metrics
# - System impact
```

---

## 📊 Data Analysis Questions to Answer

### Detection Effectiveness
1. ✅ Did Snort detect all attack types?
2. ✅ What was the average detection time?
3. ✅ Which attacks had fastest detection?
4. ✅ Detection rate for each attack type?

### False Positives/Negatives
1. ✅ How many false positives occurred?
2. ✅ Were there any missed attacks?
3. ✅ Which rules need tuning?
4. ✅ Need additional whitelisting?

### Rule Performance
1. ✅ Which SIDs triggered most often?
2. ✅ Which priorities were most relevant?
3. ✅ Any redundant rules?
4. ✅ Coverage gaps?

### System Impact
1. ✅ CPU usage during tests?
2. ✅ Memory consumption?
3. ✅ Network impact?
4. ✅ System responsiveness?

### Firewall + IDS/IPS Coordination
1. ✅ Did firewall block before IDS alert?
2. ✅ Complementary effect?
3. ✅ Any conflicts?
4. ✅ Resource trade-offs?

---

## 📁 Expected Output Files

After all phases:

```
test_results/
├── snort_alerts_raw.log          # Raw Snort log
├── snort_alerts.csv              # Parsed alerts
├── test_results.csv              # Test execution data
├── attack_logs.txt               # Combined attack logs
├── attack_capture.pcap           # Network traffic capture
├── analysis_report.html          # Visual HTML report
├── analysis_report.json          # Structured data
│
├── attack_metrics.txt            # Calculated metrics
├── effectiveness_analysis.txt    # Detailed analysis
├── findings_summary.txt          # Key findings
└── recommendations.txt           # Recommendations
```

---

## 📈 Sample Data Analysis Report

```
═══════════════════════════════════════════════════════════
  ATTACK SIMULATION DATA ANALYSIS REPORT
═══════════════════════════════════════════════════════════

Test Date: May 4, 2026
Total Tests Executed: 8
Total Attacks Simulated: ~1200+ individual attempts

DETECTION EFFECTIVENESS:
  ├─ Malware C2: 8/10 alerts (80%)
  ├─ SSH Brute-Force: 25/30 alerts (83%)
  ├─ RDP Brute-Force: 30/50 alerts (60%)
  └─ Port Scanning: 8/8 alerts (100%)
  
  OVERALL DETECTION RATE: 82%

ALERT ANALYSIS:
  ├─ Priority 1 (High): 45 alerts (40%)
  ├─ Priority 2 (Medium): 52 alerts (46%)
  └─ Priority 3 (Low): 16 alerts (14%)

PERFORMANCE METRICS:
  ├─ Average Detection Time: 1.2 seconds
  ├─ Fastest Detection: 0.3 seconds (Port Scan)
  ├─ Slowest Detection: 3.1 seconds (Malware C2)
  └─ False Positive Rate: 2.1%

FIREWALL vs. IDS/IPS:
  ├─ Firewall Detection Only: 35% (SSH/RDP)
  ├─ IDS/IPS Detection Only: 85% (All types)
  └─ Combined Detection: 95%+

KEY FINDINGS:
  ✓ Layered security significantly improves detection
  ✓ IDS/IPS catches encrypted threats firewall misses
  ✓ SSH rapid attacks detected nearly instantly
  ✓ Port scanning easily detected with current rules
  ✓ False positive rate acceptable (2.1%)

RECOMMENDATIONS:
  1. Increase SSH rule sensitivity slightly
  2. Review RDP rule for missed detections
  3. Fine-tune malware C2 detection rules
  4. Consider ML-based anomaly detection
  5. Implement automatic IP blocking after threshold

═══════════════════════════════════════════════════════════
```

---

## 🔧 Troubleshooting Common Issues

### Snort Not Logging Alerts
```bash
# Check Snort is running
ps aux | grep snort

# Verify log directory exists
ls -la /var/log/snort/

# Check file permissions
sudo chmod 777 /var/log/snort/

# Restart Snort with verbose output
sudo snort -A full -l /var/log/snort -c snort_custom_rules.conf -i eth0 -v
```

### Attack Scripts Fail to Connect
```bash
# Verify target is reachable
ping 192.168.1.100

# Check service is running
ssh -v 192.168.1.100

# Check firewall rules
sudo iptables -L -n

# Verify ports are listening
ss -tlnp | grep LISTEN
```

### Alerts Not Parsing
```bash
# Check alert format
head -20 /var/log/snort/alert

# Verify data_collector.py can parse
python3 data_collector.py --parse-snort test_results/snort_alerts_raw.log --verbose
```

---

## ✅ Completion Checklist

### Test Execution
- [ ] All 8 attack scenarios completed
- [ ] Each test logged to file
- [ ] System monitored throughout
- [ ] No critical errors

### Data Collection
- [ ] Snort alerts exported
- [ ] Attack logs collected
- [ ] System metrics captured
- [ ] Packet captures saved

### Data Analysis
- [ ] Alerts parsed into CSV
- [ ] Metrics calculated
- [ ] HTML report generated
- [ ] Results template filled

### Reporting
- [ ] Results documented
- [ ] Findings summarized
- [ ] Recommendations provided
- [ ] Report approved

---

## 📞 Next Steps

1. **Data Review Meeting** - Team discusses findings
2. **Rule Tuning** - Optimize Snort rules based on results
3. **Production Testing** - Run on actual systems with care
4. **Security Policy** - Update security guidelines
5. **User Training** - Educate staff on findings

---

**Prepared by:** [Team Members]  
**Date:** May 4, 2026  
**Status:** Ready for Execution ✅

---

**Report Version:** 1.0  
**Next Update:** Upon test completion
