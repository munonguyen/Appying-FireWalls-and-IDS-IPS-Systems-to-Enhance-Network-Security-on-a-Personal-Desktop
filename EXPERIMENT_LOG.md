# Experiment Log & Results

## Current Testing Status

### Phase: Malware Detection Testing ✅ IN PROGRESS

**Date Started:** May 4, 2026  
**Responsible:** Nguyễn Thanh Bình, Lê Thị Hải Yến

---

## Test 1: Malware Detection with Flightsim

### Setup

- **Attacker Tool:** Flightsim (malware behavior simulator)
- **Capture Tool:** Npcap
- **Detection Engine:** Snort with custom rules
- **Firewall:** Windows Defender Firewall

### Scenario

Flightsim simulates an infected PC sending malicious traffic to external C2 (Command & Control) servers:

- Beacon-like outbound connections
- High entropy data transmission
- Unusual port usage
- Suspicious DNS queries

### Expected Observations

✅ **Firewall Bypass:** Flightsim bypasses the basic firewall (using legitimate HTTPS port 443)  
✅ **Snort Detection:** IDS immediately catches the malicious traffic with continuous alerts  
✅ **Rule Triggering:** Custom Snort rules generate alerts for:

- Suspicious outbound traffic
- Possible C2 activity
- Abnormal traffic patterns

### Key Metrics

| Metric              | Target  | Status     |
| ------------------- | ------- | ---------- |
| Detection Rate      | >90%    | 🔄 Testing |
| Firewall Block Rate | 70-100% | 🔄 Testing |
| IDS/IPS Alert Time  | <1 sec  | 🔄 Testing |
| False Positives     | Low     | 🔄 Testing |

### Alert Example

```
[**] [1:1000001:1] MALWARE-CNC Suspicious C2 Beaconing Activity [**]
[Classification: Misc activity] [Priority: 2] {TCP}
05/04-14:32:15.234567 192.168.1.100:54321 -> 203.0.113.45:443
Timestamp: 2026-05-04 14:32:15 UTC
Source IP: 192.168.1.100 (Local Host)
Destination IP: 203.0.113.45 (External C2 Server)
Protocol: TCP
Port: 443 (HTTPS)
Rule: CUSTOM-MALWARE-DETECT
Severity: Medium
Action: Alert
```

---

## Test 2: Brute-Force Attack Detection

### Status: NOT YET TESTED ⏳

### Setup

- **Attack Method:** Multiple failed SSH/RDP login attempts
- **Source:** Single or multiple attacker IPs
- **Target:** Local SSH/RDP services

### Expected Results

- IDS detects consecutive failed authentication attempts
- Automatic blocking after 5-10 failed attempts
- Alert generation with attacker IP and attempt count
- Significant reduction in attack success rate

### Metrics to Measure

| Metric            | Expected    |
| ----------------- | ----------- |
| Detection Latency | <5 seconds  |
| Blocking Latency  | <10 seconds |
| Blocked Attempts  | >95%        |
| False Positives   | <1%         |

---

## Test 3: Port Scanning Detection

### Status: NOT YET TESTED ⏳

### Setup

- **Scanning Tool:** Nmap or similar
- **Target:** Personal desktop with custom ports
- **Detection Method:** Snort rules for scanning patterns

### Expected Observations

- Detect rapid sequential port probes
- Alert on suspicious scanning patterns
- Block attacker IP after threshold

---

## General Observations

### Firewall Limitations

- ✅ Blocks basic unauthorized connections
- ❌ Fails to detect malware using legitimate ports (e.g., HTTPS)
- ❌ Cannot inspect encrypted payload content
- ❌ Reactive only to known blacklisted IPs

### IDS/IPS Advantages

- ✅ Deep packet inspection of payloads
- ✅ Behavioral analysis of traffic patterns
- ✅ Real-time threat detection and alerting
- ✅ Custom rule flexibility for organization-specific threats

### Combined System Benefits

- ✅ Multiple layers catch evasion attempts
- ✅ Firewall reduces load on IDS/IPS
- ✅ IDS/IPS catches sophisticated attacks
- ✅ Comprehensive logging and audit trail

---

## Snort Rules (Custom Configuration)

### Example Rule Structure

```
alert tcp any any -> any 443 (msg:"MALWARE-CNC Suspicious HTTPS Activity"; \
  content:"GET"; http_method; \
  content:"User-Agent|3a|"; http_header; \
  classtype:trojan-activity; sid:1000001; rev:1; priority:2;)

alert tcp any any -> any 22 (msg:"IDS-SSH Multiple Failed Login Attempts"; \
  flow:to_server,established; \
  content:"Invalid user"; msg:"SSH Brute Force Attempt"; \
  threshold: type both, track by_src, count 5, seconds 60; \
  classtype:attempted-user; sid:1000002; rev:1; priority:1;)
```

---

## Next Steps

1. ⏳ Complete Malware (Flightsim) testing
2. ⏳ Conduct Brute-Force attack testing
3. ⏳ Execute Port Scanning detection tests
4. ⏳ Compile comprehensive results
5. ⏳ Generate final analysis report
6. ⏳ Document team findings and recommendations

---

**Last Updated:** May 4, 2026  
**Next Review:** Upon test completion
