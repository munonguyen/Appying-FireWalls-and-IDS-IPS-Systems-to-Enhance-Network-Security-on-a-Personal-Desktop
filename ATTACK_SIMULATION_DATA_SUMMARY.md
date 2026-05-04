# 🎯 Attack Simulation & Data Collection - Complete Summary

**Project:** Applying Firewalls and IDS/IPS Systems to Enhance Network Security on a Personal Desktop

---

## 📦 What Was Created

### 1. Attack Simulation Scripts

| File | Purpose | Command |
|------|---------|---------|
| `bruteforce_ssh_attack.py` | SSH brute-force simulator | `python3 bruteforce_ssh_attack.py --host <ip> --user admin --wordlist passwords.txt` |
| `bruteforce_rdp_attack.py` | RDP brute-force simulator | `python3 bruteforce_rdp_attack.py --host <ip> --user admin --rapid --attempts 50` |
| `port_scanner.py` | Port reconnaissance scanner | `python3 port_scanner.py --host <ip> --common` |
| `run_all_tests.py` | Automated test orchestrator | `python3 run_all_tests.py --host <ip> --all` |

### 2. Detection Rules

| File | Purpose | Count |
|------|---------|-------|
| `snort_custom_rules.conf` | Custom Snort IDS rules | 15 detection rules |

### 3. Data Collection & Analysis

| File | Purpose | Output |
|------|---------|--------|
| `data_collector.py` | Parse & analyze attack data | CSV, JSON, HTML reports |

### 4. Supporting Data Files

| File | Purpose |
|------|---------|
| `passwords.txt` | Password wordlist for brute-force tests |

### 5. Documentation

| File | Purpose |
|------|---------|
| `BRUTEFORCE_QUICK_START.md` | Quick reference for running tests |
| `ATTACK_TESTING_GUIDE.md` | Detailed testing procedures |
| `DATA_COLLECTION_GUIDE.md` | Data collection methodology |
| `ATTACK_SIMULATION_RESULTS.md` | Results template & analysis framework |
| `EXECUTION_WORKFLOW.md` | Complete end-to-end workflow |
| `ATTACK_SIMULATION_DATA_SUMMARY.md` | This file |

---

## 🚀 Quick Start (5 minutes)

### Simplest Way to Run Tests

```bash
# Terminal 1: Start Snort
sudo snort -A full -l /var/log/snort -c snort_custom_rules.conf -i eth0

# Terminal 2: Run all tests with interactive menu
python3 run_all_tests.py --host 192.168.1.100 --interactive

# Terminal 3: Monitor alerts in real-time
tail -f /var/log/snort/alert
```

---

## 📊 Attack Scenarios Included

### Scenario 1: Malware C2 Simulation
- **Tool**: Flightsim
- **Detection**: HTTPS beaconing, DNS anomalies
- **Expected Alerts**: C2-related Snort alerts

### Scenario 2-3: SSH Brute-Force
- **Test 2**: Standard (1 attack/sec)
- **Test 3**: Rapid (10 attacks/sec)
- **Detection**: Failed login patterns, rapid connection spikes

### Scenario 4-5: RDP Brute-Force  
- **Test 4**: Standard (1 connection/0.5 sec)
- **Test 5**: Rapid (50 attempts rapid)
- **Detection**: Multiple connection attempts, authentication failures

### Scenario 6-8: Port Scanning
- **Test 6**: Common ports (16 ports)
- **Test 7**: Port range (1-100)
- **Test 8**: Rapid scan (1-1000 ports)
- **Detection**: Sequential probing patterns, reconnaissance activity

---

## 📈 Data Collection Architecture

```
Attack Simulation Scripts
    ↓ (generates attack traffic)
Network/Firewall
    ↓ (blocks/allows)
Npcap (captures packets)
    ↓ (feeds traffic to IDS)
Snort IDS/IPS (analyzes)
    ↓ (generates alerts)
Alert Log Files
    ↓ (parsed by)
data_collector.py
    ↓ (produces)
CSV, JSON, HTML Reports
```

---

## 🎯 Complete Testing Workflow

### Step 1: Preparation (10 min)
```bash
# Install dependencies
pip3 install paramiko

# Verify setup
./test_setup.sh  # (if available)
```

### Step 2: Start Monitoring (5 min)
```bash
# Terminal 1: Snort IDS
sudo snort -A full -l /var/log/snort -c snort_custom_rules.conf -i eth0

# Terminal 2: Packet capture  
sudo tcpdump -i eth0 -w capture.pcap

# Terminal 3: System monitoring
watch -n 1 'free -h && echo "---" && top -bn1 | head -20'
```

### Step 3: Run Attacks (40 min)
```bash
# Terminal 4: Execute all tests
python3 run_all_tests.py --host 192.168.1.100 --all
```

### Step 4: Collect Data (20 min)
```bash
# Export Snort alerts
cp /var/log/snort/alert test_results/snort_alerts_raw.log

# Run data collector
python3 data_collector.py
```

### Step 5: Analyze Results (30 min)
```bash
# Generate reports
python3 data_collector.py --generate-report test_results/

# View HTML report
open test_results/test_report.html

# Fill template with findings
nano ATTACK_SIMULATION_RESULTS.md
```

---

## 📋 Data Collected Per Attack

### From Attack Script Output
- Total attack attempts
- Attack rate (attempts/second)
- Attack duration
- Unique targets
- Attack success indicators

### From Snort IDS
- Alert timestamp
- Alert message/type
- Source IP & port
- Destination IP & port
- Protocol
- Alert priority (1=High, 2=Med, 3=Low)
- Signature ID (SID)

### From System Monitoring
- CPU usage during attacks
- Memory consumption
- Network throughput
- System responsiveness
- Process activity

### From Network Capture
- Packet count
- Traffic patterns
- Payload analysis (if needed)
- Unique flows

---

## 📊 Analysis Methods

### 1. Alert Correlation
```
Match attack attempts to Snort alerts
Calculate detection latency
Identify missed attacks
Count false positives
```

### 2. Pattern Analysis
```
Aggregate alerts by type
Track source IPs
Analyze port usage
Identify timing patterns
```

### 3. Effectiveness Metrics
```
Detection Rate = (Detected Attacks / Total Attacks) × 100
FP Rate = (False Alerts / Total Traffic) × 100
Average Detection Time
System Impact Score
```

### 4. Comparative Analysis
```
Firewall Only vs. IDS/IPS Only vs. Combined
Detection rate improvements
Response time comparisons
Resource usage trade-offs
```

---

## 📁 Output Structure

```
test_results/
├── test_results.csv          # All test execution data
├── snort_alerts.csv          # Parsed Snort alerts
├── snort_alerts_raw.log      # Raw Snort log
├── attack_capture.pcap       # Network traffic
├── test_report.html          # Visual report
├── test_results.json         # Structured data
├── analysis_summary.json     # Attack summary
└── attack_logs.txt           # Combined logs
```

---

## 🔍 Key Metrics to Track

### Detection Performance
| Metric | Acceptable | Good | Excellent |
|--------|-----------|------|-----------|
| Detection Rate | >70% | >85% | >95% |
| Detection Time | <5 sec | <2 sec | <1 sec |
| False Positive Rate | <5% | <2% | <1% |

### Attack Coverage
| Attack Type | Expected Detection |
|-------------|-------------------|
| SSH Brute-Force | 85-95% |
| RDP Brute-Force | 80-90% |
| Port Scanning | 90-100% |
| Malware C2 | 70-85% |

### System Impact
| Resource | Acceptable | Ideal |
|----------|-----------|-------|
| CPU Overhead | <10% | <5% |
| Memory Overhead | <100MB | <50MB |
| Network Impact | <5% | <2% |

---

## 💡 Usage Examples

### Run Single Test
```bash
python3 bruteforce_ssh_attack.py --host 192.168.1.100 --user admin --wordlist passwords.txt --delay 1
```

### Run Test with Custom Parameters
```bash
python3 port_scanner.py --host 192.168.1.100 --range 1 500 --timeout 3
```

### Run All Tests Automatically
```bash
python3 run_all_tests.py --host 192.168.1.100 --all
```

### Collect and Analyze Data
```bash
python3 data_collector.py --snort-log /var/log/snort/alert --output results/
```

---

## 🔐 Security Reminders

⚠️ **IMPORTANT:**
- Only test on systems you own or have written permission to test
- Do not use on production systems
- Ensure lab is isolated from the internet
- Document all activities with timestamps
- Remove/anonymize IPs before sharing reports
- Comply with all local laws and regulations

---

## 📚 Documentation Files & When to Use

| Document | When to Use |
|----------|------------|
| `BRUTEFORCE_QUICK_START.md` | Need to run tests immediately |
| `ATTACK_TESTING_GUIDE.md` | Detailed instructions for each test |
| `DATA_COLLECTION_GUIDE.md` | Understanding data collection methodology |
| `ATTACK_SIMULATION_RESULTS.md` | Recording and analyzing test results |
| `EXECUTION_WORKFLOW.md` | Complete step-by-step workflow |
| `README.md` | Project overview and quick reference |

---

## ✅ Success Indicators

After completing all tests, you should have:

✓ **8 attack scenarios executed** - All tests ran without critical errors
✓ **1000+ alerts captured** - Snort detected and logged attacks
✓ **Attack timelines established** - Timestamps show detection sequence
✓ **System metrics recorded** - CPU, memory, network data collected
✓ **False positives identified** - Known legitimate activities documented
✓ **Effectiveness verified** - Detection rates calculated
✓ **Reports generated** - HTML, CSV, JSON outputs created
✓ **Findings documented** - Key observations recorded
✓ **Recommendations provided** - Improvement suggestions made

---

## 🎓 Learning Outcomes

This project demonstrates:

1. **How firewalls work** - Traffic filtering and rule-based blocking
2. **How IDS/IPS works** - Pattern matching and anomaly detection
3. **Why layered security matters** - Multiple layers catch more attacks
4. **Detection methodology** - Signature vs. anomaly-based detection
5. **Data analysis** - Parsing logs and extracting metrics
6. **Security metrics** - Measuring effectiveness objectively

---

## 🔧 Technical Stack

- **Attack Simulation**: Python (paramiko, socket, threading)
- **IDS/IPS Engine**: Snort with custom rules
- **Packet Capture**: Npcap or libpcap/tcpdump
- **Data Analysis**: Python (csv, json, collections)
- **Reporting**: HTML, CSV, JSON formats
- **System Monitoring**: Linux tools (top, iostat, netstat)

---

## 📞 Support & Troubleshooting

### Common Issues

**Q: Snort not capturing alerts**  
A: Check Snort is running (`ps aux | grep snort`), verify permissions (`chmod 777 /var/log/snort/`), check configuration syntax

**Q: Attack scripts won't connect**  
A: Verify target reachable (`ping`), check service running (`ssh -v`), verify firewall rules allow traffic

**Q: Data collector fails to parse**  
A: Check alert log format (`head -20 /var/log/snort/alert`), run with verbose mode, verify file permissions

**Q: Low detection rate**  
A: Check custom rules loaded, verify Snort rule set up-to-date, check IDS in correct mode (IDS vs IPS)

---

## 🎯 Next Steps After Testing

1. **Review Findings** - Analyze detection rates and false positives
2. **Tune Rules** - Adjust Snort rules based on results
3. **Update Policy** - Document security procedures based on findings
4. **Train Users** - Educate on layered security importance
5. **Plan Deployment** - Roadmap for implementing on production systems
6. **Continuous Monitoring** - Set up ongoing IDS/IPS monitoring

---

## 📝 Quick Reference Card

```
ATTACK SIMULATION QUICK REFERENCE

Start Snort:
  sudo snort -A full -l /var/log/snort -c snort_custom_rules.conf -i eth0

SSH Brute-Force:
  python3 bruteforce_ssh_attack.py --host TARGET --user admin --wordlist passwords.txt

RDP Brute-Force:
  python3 bruteforce_rdp_attack.py --host TARGET --port 3389 --rapid

Port Scan:
  python3 port_scanner.py --host TARGET --common

Run All Tests:
  python3 run_all_tests.py --host TARGET --all

View Alerts:
  tail -f /var/log/snort/alert

Collect Data:
  python3 data_collector.py

Generate Report:
  python3 data_collector.py --generate-report test_results/
```

---

## 🏆 Project Completion Checklist

- [ ] All attack simulation scripts created and tested
- [ ] Snort custom rules configured (15 rules)
- [ ] Data collection tool implemented
- [ ] Documentation completed (6 major documents)
- [ ] Test workflow documented step-by-step
- [ ] Example data collection shown
- [ ] Output format specifications provided
- [ ] Analysis methodology explained
- [ ] Code committed to git repository
- [ ] Team ready to execute tests

---

**Status:** ✅ READY FOR ATTACK SIMULATION & DATA COLLECTION

**Created:** May 4, 2026  
**Version:** 1.0  
**Team:** Hanoi University - Network Security Course

---

For detailed information on each component, see the corresponding documentation file listed above.

**Ready to test!** 🚀
