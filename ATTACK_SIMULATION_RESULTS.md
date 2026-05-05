# Attack Simulation Results & Analysis Report

**Project:** Applying Firewalls and IDS/IPS Systems to Enhance Network Security on a Personal Desktop  
**Date:** May 4, 2026  
**Test Environment:** Personal Desktop Lab

---

## 📋 Executive Summary

This document consolidates data from attack simulation scenarios including:

- ✅ Malware simulation (Flightsim C2)
- ✅ Brute-force attacks (SSH & RDP)
- ✅ Port scanning & reconnaissance
- ✅ Malicious traffic injection

---

## 🎯 Test Scenarios Overview

| #   | Scenario                 | Tool                     | Type              | Status  |
| --- | ------------------------ | ------------------------ | ----------------- | ------- |
| 1   | Malware C2 Beaconing     | Flightsim + Snort        | Malware           | Executed - Detected |
| 2   | SSH Brute-Force (Slow)   | bruteforce_ssh_attack.py | Credential Attack | Data Collected |
| 3   | SSH Brute-Force (Fast)   | bruteforce_ssh_attack.py | Credential Attack | Data Collected |
| 4   | RDP Brute-Force (Slow)   | bruteforce_rdp_attack.py | Credential Attack | Data Collected |
| 5   | RDP Brute-Force (Fast)   | bruteforce_rdp_attack.py | Credential Attack | Planned |
| 6   | Port Scan (Common)       | port_scanner.py          | Reconnaissance    | Data Collected |
| 7   | Port Scan (Range)        | port_scanner.py          | Reconnaissance    | Planned |
| 8   | Port Scan (Rapid 1-1000) | port_scanner.py          | Reconnaissance    | Planned |

---

## 🛡️ Blue Force Results Summary

This section focuses on the defensive results from the Blue Force side. The lab used Windows Defender Firewall as the first filtering layer, Npcap as the packet capture engine, and Snort as the IDS analysis engine. The main evidence is based on the screenshots showing Flightsim C2 traffic and Snort console alerts.

### Blue Force Lab Configuration

| Component | Observed Configuration |
| --------- | ---------------------- |
| Defensive host | Windows personal desktop lab |
| Firewall layer | Windows Defender Firewall |
| Packet capture engine | Npcap |
| IDS/IPS engine | Snort 2.9.20-WIN64 GRE Build 82 |
| Snort mode in this lab | IDS mode - console alerting, not inline blocking |
| Monitored interface | Index 4 - Realtek 8822BE Wireless LAN 802.11ac PCI-E NIC |
| Defensive host/source IP | 192.168.51.109 |
| Snort command | `snort -i 4 -c C:\Snort\etc\demo.conf -A console -N` |

### Malware C2 Detection Result

| Assessment Item | Blue Force Result |
| --------------- | ----------------- |
| Attack simulation tool | AlphaSOC Flightsim 2.5.1, `run c2` module |
| Simulated behavior | DNS lookups to C2-like domains and outbound connections to suspicious C2 IP:port pairs |
| Firewall result | No blocking was observed in the screenshots because the traffic used legitimate outbound paths such as HTTPS/443 and there was no matching blacklist rule shown |
| Npcap result | Captured outbound traffic from the monitored interface `192.168.51.109` |
| Snort result | Generated clear Malware C2 HTTPS alerts using a custom rule |
| Observed alert | `[1:1000001:1] [DU AN] Phat hien ket noi Malware C2 (HTTPS)` |
| English meaning of alert | Project rule: detected Malware C2 HTTPS connection |
| Detected traffic examples | `192.168.51.109:53413 -> 51.11.192.48:443` and `192.168.51.109:59427 -> 172.64.151.4:443` |
| Visible alert count | At least 6 Malware C2 HTTPS alerts visible on the Snort console screenshot |
| Defensive conclusion | Blue Force successfully detected Malware C2 traffic that passed through the basic firewall layer |

### Flightsim C2 Evidence from Screenshots

The Flightsim screenshot shows the infected-host simulation generating C2-style outbound activity. The defensive Snort screenshot shows that this activity was detected by the IDS.

| Evidence Type | Observed Value |
| ------------- | -------------- |
| Flightsim module | `flightsim.exe run c2` |
| Flightsim version | AlphaSOC Network Flight Simulator 2.5.1 |
| Source IP shown by Flightsim | 192.168.51.109 |
| C2 domains observed | `permission-resident-lots-ebooks.trycloudflare.com`, `malware.keonhacai.cam`, `sobig.admits.io`, `v3.earthpledge.org`, `malware.xoilaczzzzze.tv` |
| C2 IP:port pairs observed | `91.218.183.177:4444`, `62.109.26.208:443`, `123.30.48.175:8080`, `43.143.242.10:5555`, `13.232.39.48:11300` |
| Attack execution time shown | 09-Apr-2026, approximately 20:56:58 to 20:57:10 |
| Snort alert time shown | 09-Apr-2026, approximately 21:02:25 |

Because the attack terminal and IDS console were not exported into one synchronized log file, the exact Time to Detect (TTD) should not be claimed as a precise number. However, the screenshots are sufficient to show that Snort generated real-time console alerts for Malware C2 HTTPS traffic.

### Brute-Force and Reconnaissance Defensive Result

The exported test data in `test_results/` shows that the brute-force simulations did not achieve any successful login. The Snort/firewall alert logs for these specific tests still need to be exported before final detection-rate or blocking-rate claims can be made.

| Scenario | Attack Traffic Recorded | Defensive Result |
| -------- | ----------------------- | ---------------- |
| SSH brute-force slow | 100 attempts, 45.20 seconds, 2.21 attempts/sec | 0 successful logins; suitable for threshold-based SSH brute-force detection |
| SSH brute-force fast | 100 attempts, 10.10 seconds, 9.90 attempts/sec | 0 successful logins; stronger rapid-connection pattern for Snort rules |
| RDP brute-force | 50 attempts, 25.50 seconds, 1.96 attempts/sec | 0 successful logins; suitable for RDP multiple-connection detection |
| Common port scan | 6 ports scanned, open ports: 22, 80, 443 | Blue Force identified exposed services that should be hardened or restricted |

### Blue Force Key Findings

1. Windows Defender Firewall worked as the first filtering layer, but it was not sufficient to identify Malware C2 traffic using legitimate outbound ports such as HTTPS/443.
2. Npcap and Snort added deeper network visibility by inspecting captured packets and generating security alerts.
3. The custom rule `[1:1000001:1]` successfully detected Malware C2 HTTPS traffic and produced alerts containing timestamp, source IP, destination IP, protocol, port and rule ID.
4. In this Windows lab, Snort was running in IDS mode, so the confirmed result is detection and alerting. Blocking should only be claimed after Snort is tested in inline/IPS mode.
5. The brute-force and port-scan tests already have attack-side data, but synchronized Snort/firewall logs are still required to calculate final Detection Rate, Prevention Rate, Time to Detect and Time to Respond.

### Blue Force Submission Paragraph

From the Blue Force perspective, the experiment shows that a layered defense model is more effective than relying on the firewall alone. Windows Defender Firewall provided the first layer of traffic control, while Npcap captured outbound packets and Snort analyzed them in real time. During the Flightsim C2 simulation, the suspicious traffic was able to use normal outbound paths such as HTTPS/443, so no firewall block was observed. However, Snort successfully detected the Malware C2 behavior and generated repeated alerts with the rule `[1:1000001:1] [DU AN] Phat hien ket noi Malware C2 (HTTPS)`. The alert output included the source IP `192.168.51.109`, destination IPs, ports and timestamps, proving that the IDS layer detected malicious C2-like communication that the basic firewall layer did not identify.

For brute-force and reconnaissance testing, the collected results show that SSH and RDP brute-force attempts produced no successful logins, and the common port scan identified exposed services on ports 22, 80 and 443. These results support the Blue Force hardening strategy: restrict unnecessary open ports, tune Snort rules for repeated login attempts and rapid connections, and use firewall rules or IPS mode to block confirmed malicious sources. Overall, the combined firewall + IDS/IPS approach improves visibility, reduces attack exposure and provides actionable alerts for incident response.

---

## 📊 Scenario 1: Malware C2 Beaconing (Flightsim)

### Description

Simulates malware command-and-control (C2) communication using Flightsim tool.

### Attack Characteristics

- **Tool**: Flightsim malware simulator
- **Behavior**:
  - Encrypted HTTPS connections to external servers
  - Periodic "beaconing" (heartbeat) to C2 server
  - Unusual DNS queries
  - Data exfiltration patterns
  - High entropy traffic

### Expected Detection Points

#### Firewall Detection

- ❌ Likely to miss (uses legitimate HTTPS port 443)
- May detect if external IP is blacklisted
- Cannot inspect encrypted payload

#### IDS/IPS Detection (Snort)

- ✅ Detects suspicious HTTPS patterns
- ✅ Identifies beaconing behavior (periodic connections)
- ✅ Alerts on unusual DNS queries
- ✅ Recognizes C2 traffic signatures

### Expected Snort Alerts

```
[SID:1000001] MALWARE-CNC Suspicious HTTPS C2 Activity / Phat hien ket noi Malware C2 (HTTPS)
[SID:1000002] MALWARE-DNS Suspicious DNS Beaconing
[SID:1000003] MALWARE-TRAFFIC Unusual Outbound Traffic
```

### Observed Snort Alert Evidence

```
04/09-21:02:25.x [**] [1:1000001:1] [DU AN] Phat hien ket noi Malware C2 (HTTPS) [**]
[TCP] 192.168.51.109:53413 -> 51.11.192.48:443

04/09-21:02:25.x [**] [1:1000001:1] [DU AN] Phat hien ket noi Malware C2 (HTTPS) [**]
[TCP] 192.168.51.109:59427 -> 172.64.151.4:443
```

### Test Data to Collect

| Metric                  | Expected Value | Actual Value |
| ----------------------- | -------------- | ------------ |
| Total HTTPS Connections | 10-50          | 2 HTTPS C2 destinations visible in Snort alert; 10 IP:port pairs visible across two Flightsim runs |
| Detection Time (sec)    | <2             | Not calculated exactly; console alert confirmed after traffic capture |
| Snort Alerts            | 5-15           | At least 6 malware C2 HTTPS alerts visible on console |
| DNS Anomaly Alerts      | 3-8            | Not confirmed in screenshot |
| False Positives         | <2             | 0 observed during controlled Flightsim test |
| False Negatives         | 0              | Not fully measurable without exported full log/pcap |
| CPU Impact (%)          | <5             | Not recorded |
| Memory Impact (MB)      | <50            | Not recorded |

### Analysis Questions

1. Was beaconing pattern detected immediately?  
   - Snort alert was confirmed on the console, but exact TTD requires synchronized log export.
2. How many connection attempts before alert?  
   - At least two HTTPS C2 destinations were shown in Snort alerts; exact attempt count requires full alert log.
3. Were DNS anomalies caught?  
   - Flightsim generated suspicious DNS queries, but DNS-specific Snort alerts were not visible in the supplied screenshot.
4. Any false positives from legitimate HTTPS traffic?  
   - None observed during the controlled test window.
5. Did firewall supplement IDS/IPS detection?  
   - Firewall reduced exposure at the port/IP layer, but the key detection came from Snort IDS because C2 traffic used legitimate outbound network paths.

---

## 📊 Scenario 2-5: Brute-Force Blue Force Results

This section focuses on the Blue Force result for SSH and RDP brute-force activity. The objective is to verify whether repeated login attempts or sudden connection spikes can be detected by IDS/IPS rules, and how the firewall or IPS layer can be used to block the attacking source after a defined threshold.

### Defensive Objective

| Requirement | Blue Force Interpretation |
| ----------- | ------------------------- |
| Detect repeated failed logins | Snort rules monitor repeated SSH/RDP attempts from the same source within a short time window |
| Detect sudden request spikes | Rapid SSH/RDP attempts trigger threshold-based rules using `track by_src` |
| Block the attacking source after 5-10 failures | Blocking is a follow-up defensive action through firewall rules or Snort inline/IPS mode |
| Reduce brute-force success | The current test data shows 0 successful logins across SSH and RDP attempts |

### Commands Used for Brute-Force Simulation

Start Snort in IDS console mode on the monitored Windows interface:

```powershell
cd C:\Snort\bin
snort -i 4 -c C:\Snort\etc\demo.conf -A console -N
```

Run the SSH standard brute-force test:

```bash
python3 bruteforce_ssh_attack.py \
  --host 192.168.1.100 \
  --port 22 \
  --user admin \
  --wordlist passwords.txt \
  --delay 1
```

Run the SSH rapid brute-force test. In this script, `--attempts 10` means 10 attempts per second and generates 100 password attempts:

```bash
python3 bruteforce_ssh_attack.py \
  --host 192.168.1.100 \
  --port 22 \
  --user admin \
  --rapid \
  --attempts 10
```

Run the RDP brute-force test:

```bash
python3 bruteforce_rdp_attack.py \
  --host 192.168.1.100 \
  --port 3389 \
  --user admin \
  --wordlist passwords.txt \
  --delay 0.5
```

Optional RDP rapid test command for the remaining test case:

```bash
python3 bruteforce_rdp_attack.py \
  --host 192.168.1.100 \
  --port 3389 \
  --user admin \
  --rapid \
  --attempts 50
```

### Observed Attack-Side Results

The exported result file shows that the brute-force simulations did not obtain valid credentials or successful login sessions.

| Test Case | Target | Attempts | Duration | Rate | Successful Logins |
| --------- | ------ | -------- | -------- | ---- | ----------------- |
| SSH brute-force standard | `192.168.1.100:22` | 100 | 45.20 sec | 2.21/sec | 0 |
| SSH brute-force rapid | `192.168.1.100:22` | 100 | 10.10 sec | 9.90/sec | 0 |
| RDP brute-force standard | `192.168.1.100:3389` | 50 | 25.50 sec | 1.96/sec | 0 |
| **Total** | SSH + RDP | **250** | - | - | **0** |

### Extracted Results for Submission

The following values are taken from `test_results/brute_force_results.txt` and `test_results/brute_force_results.csv`.

| Field | Value to Submit |
| ----- | --------------- |
| Test timestamp | 2026-05-04T09:32:31.110942 |
| Target host | `192.168.1.100` |
| Tested services | SSH/22 and RDP/3389 |
| Tested username | `admin` |
| SSH test count | 2 |
| SSH total attempts | 200 |
| SSH successful logins | 0 |
| SSH average duration | 27.65 seconds |
| RDP test count | 1 |
| RDP total attempts | 50 |
| RDP successful attempts | 0 |
| RDP average duration | 25.50 seconds |
| Total brute-force attempts | 250 |
| Total successful attempts | 0 |
| Measured brute-force success rate | 0% |

Evidence statement for the report:

```text
The brute-force test generated 250 total attempts against SSH and RDP services on 192.168.1.100. The exported results show 200 SSH attempts and 50 RDP attempts, with 0 successful attempts recorded. This indicates that no credential compromise or successful brute-force access was achieved during the test window.
```

Blue Force evidence status:

| Evidence Type | Current Status | How to Use in Report |
| ------------- | -------------- | -------------------- |
| Attack execution data | Available | Use the exported totals, rate and success values |
| Snort brute-force alert log | Not included in current evidence | State expected detection based on configured Snort rules |
| Firewall/IPS block log | Not included in current evidence | State blocking as the designed response path, not a proven result |
| Final blocking claim | Pending | Only claim confirmed blocking after collecting firewall or IPS logs |

### Blue Force Detection Logic

The defensive rules are threshold-based. Instead of reacting to a single login attempt, Snort looks for repeated activity from the same source address. This makes the detection more useful because normal users may mistype a password once or twice, while brute-force tools create a repeated pattern.

| Rule ID | Detection Purpose | Trigger Threshold | Expected Blue Force Action |
| ------- | ----------------- | ----------------- | -------------------------- |
| `3000002` | SSH brute-force behavior | 5 matching events within 60 seconds | Raise high-priority SSH brute-force alert |
| `3000003` | SSH password attempt pattern | 3 matching events within 30 seconds | Raise failed-login pattern alert |
| `3000004` | Rapid SSH connections | 10 new SSH connections within 60 seconds | Raise rapid-source alert |
| `3000006` | RDP brute-force behavior | 10 new RDP connections within 60 seconds | Raise high-priority RDP brute-force alert |
| `3000007` | Rapid RDP reconnection | 20 new RDP connections within 30 seconds | Raise rapid RDP alert |

Expected Snort alert messages:

```text
[SID:3000002] SSH BRUTE-FORCE Possible Brute Force Attack Detected
[SID:3000003] SSH Failed Login Attempt
[SID:3000004] SSH RAPID Multiple Connections from Same Source
[SID:3000006] RDP BRUTE-FORCE Multiple Connections Detected
[SID:3000007] RDP BRUTE-FORCE Rapid Connection Attempts
```

### Blocking Strategy

The current lab evidence supports IDS detection planning and attack-side success measurement. It should not be written as "automatic blocking was proven" unless synchronized Snort/firewall logs are exported. The correct defensive design is:

1. Snort detects repeated login attempts or rapid connection bursts.
2. The source IP is classified as suspicious after the threshold is reached.
3. Windows Firewall or Snort IPS mode blocks the source.
4. Future SSH/RDP attempts from that source are denied before authentication can continue.

Manual Windows Firewall block command after confirming the attack source:

```powershell
New-NetFirewallRule `
  -DisplayName "Block brute-force source" `
  -Direction Inbound `
  -RemoteAddress <ATTACKER_IP> `
  -Action Block
```

Example Snort IPS rule style. This requires Snort to run in inline/IPS mode; changing `alert` to `drop` alone is not enough if Snort is still running in passive IDS mode:

```text
drop tcp any any -> any 22 (
  msg:"SSH BRUTE-FORCE Block Source After Threshold";
  flow:to_server,new;
  flags:S;
  threshold:type both, track by_src, count 10, seconds 60;
  sid:3000104; rev:1; priority:1;
)

drop tcp any any -> any 3389 (
  msg:"RDP BRUTE-FORCE Block Source After Threshold";
  flow:to_server,new;
  flags:S;
  threshold:type both, track by_src, count 10, seconds 60;
  sid:3000106; rev:1; priority:1;
)
```

### Result Interpretation

The brute-force tests produced 250 total SSH/RDP attempts and 0 successful logins, giving a measured success rate of 0% in the collected test data. From the Blue Force perspective, this result supports the defensive goal of reducing successful brute-force outcomes. The IDS/IPS rules are designed to identify the attack pattern after repeated attempts, especially when the rate increases suddenly.

For final reporting, the strongest accurate conclusion is: the brute-force traffic was generated successfully, no credentials were compromised, and the configured Snort rules provide a clear detection path based on failed-login repetition and connection-rate thresholds. The remaining validation step is to export Snort and firewall logs during the same test window to prove alert count, Time to Detect, Time to Respond and the number of blocked attempts.

### Submission-Ready Summary

In the brute-force experiment, the Blue Force focused on detecting repeated authentication attempts and rapid connection bursts against SSH and RDP services. The test generated 200 SSH attempts and 50 RDP attempts against `192.168.1.100`, with 0 successful logins recorded. Snort rules were prepared to detect brute-force behavior using source-based thresholds, such as 5 SSH-related events within 60 seconds or 10 rapid connections from the same source. This approach is more reliable than simple port filtering because it identifies the behavior pattern of brute-force activity rather than only checking whether port 22 or 3389 is open.

The defensive workflow is to let Snort identify the suspicious source, then block that source through Windows Firewall or Snort inline IPS mode. In the current lab, Snort was used mainly for IDS alerting, so the report should state that blocking is the planned response path, not a fully proven result. Overall, the collected data supports the conclusion that the layered firewall + IDS/IPS model reduces brute-force risk by detecting abnormal login behavior early and providing a clear mechanism to block the attacking IP after the threshold is reached.

---

## 📊 Scenario 6, 7, 8: Port Scanning / Reconnaissance

### Test 6: Port Scan (Common Ports)

**Command:**

```bash
python3 port_scanner.py \
  --host 192.168.1.100 \
  --common
```

**Ports Scanned:** 21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3306, 3389, 5432, 5900, 8080, 8443 (16 ports)

### Test 7: Port Scan (Range 1-100)

**Command:**

```bash
python3 port_scanner.py \
  --host 192.168.1.100 \
  --range 1 100
```

**Ports Scanned:** 1-100 (100 ports)

### Test 8: Port Scan (Rapid 1-1000)

**Command:**

```bash
python3 port_scanner.py \
  --host 192.168.1.100 \
  --ports 1-1000 \
  --rapid
```

**Ports Scanned:** 1-1000 (1000 ports) at rapid rate

### Expected Detection Metrics

| Test     | Ports | Scan Time | Detection Time | Alerts |
| -------- | ----- | --------- | -------------- | ------ |
| Common   | 16    | ~2 sec    | 1-2 sec        | 1-2    |
| Range    | 100   | ~10 sec   | 2-3 sec        | 2-3    |
| Rapid 1K | 1000  | ~10 sec   | <1 sec         | 3-5    |

### Expected Snort Alerts

```
[SID:3000008] RECONNAISSANCE Possible Nmap SYN Scan
[SID:3000012] RECONNAISSANCE Port Scanning Activity Detected
[SID:3000013] RECONNAISSANCE Sequential Port Scan Pattern
```

### Test Data Template

```
Test: Port Scan (Rapid 1-1000)
Date/Time: _______________
Duration: _____ seconds
Total Ports Scanned: _____
Open Ports Found: _____

Detection Timeline:
- First probe: _____ ms
- First alert: _____ seconds
- Last alert: _____ seconds
- Total alerts: _____

Alert Details:
- RECONNAISSANCE alerts: _____
- SYN scan alerts: _____
- Pattern detection: Yes / No

Firewall Response:
- Blocked: _____ attempts
- Allowed: _____ attempts
- Source IP: _______________
- Block time: _____ seconds

System Impact:
- CPU Peak: _____%
- Memory Peak: _____ MB
- Network Activity: _____ Mbps
```

---

## 📊 Combined Attack Analysis

### Data Collection Summary Form - Blue Force Focus

```
═══════════════════════════════════════════════════════════
  ATTACK SIMULATION SUMMARY FORM
═══════════════════════════════════════════════════════════

Test Session Date:
  - Malware C2 evidence: 09-Apr-2026
  - Brute-force/scan exported data: 04-May-2026
Tester Name: Project team
Target System:
  - Malware C2 lab host/source IP: 192.168.51.109
  - Brute-force/scan target: 192.168.1.100
Network: Personal desktop lab network

FIREWALL CONFIGURATION:
  ☑ Windows Defender Firewall
  ☐ UFW (Linux)
  ☐ IPTables
  ☐ Other: _______________

IDS/IPS CONFIGURATION:
  ☑ Snort (IDS mode)
  ☐ Snort (IPS mode)
  ☐ Suricata
  ☑ Other: Npcap packet capture

TEST RESULTS:
  ✓ All 8 tests executed: No - 5 evidence-backed/data-backed runs available
  ✓ Data collected: Yes - Malware C2, SSH x2, RDP x1, common port scan
  ✓ Logs saved: Partial - screenshots + CSV/JSON; full Snort log/pcap pending

TOTAL STATISTICS:
  - Total Tests Executed: 5 current runs
  - Total Attacks Simulated: 1 malware C2 scenario + 4 script-based attack runs
  - Total Alerts Generated: At least 6 visible Malware C2 HTTPS alerts
  - Detection Rate (%): Malware C2 confirmed; overall rate not final without full IDS logs
  - False Positive Rate (%): 0 observed in controlled malware C2 window
  - Average Detection Time (sec): Not final; timestamp synchronization/export required
  - System Resource Impact: Not recorded

KEY FINDINGS:
  1. Flightsim C2 bypassed basic firewall filtering but was detected by Snort.
  2. Custom Malware C2 HTTPS rule [1:1000001:1] fired repeatedly.
  3. SSH/RDP brute-force attempts had 0 successful logins in exported test data.

RECOMMENDATIONS:
  1. Export Snort alerts to file and correlate with attack timestamps.
  2. Test Snort inline/IPS mode before claiming prevention/blocking metrics.
  3. Add firewall deny rules or dynamic blocklists for confirmed malicious IPs/domains.

═══════════════════════════════════════════════════════════
```

---

## 📈 Comparative Analysis Table

### Effectiveness Comparison: Firewall Only vs. IDS/IPS Only vs. Combined

| Attack Type         | Firewall Only | IDS/IPS Only | Combined |
| ------------------- | ------------- | ------------ | -------- |
| **SSH Brute-Force** |               |              |          |
| Detection Rate      | 40-60%        | 80-95%       | 95%+     |
| Time to Detect      | 5+ sec        | 1-2 sec      | <1 sec   |
|                     |               |              |          |
| **RDP Brute-Force** |               |              |          |
| Detection Rate      | 50-70%        | 85-95%       | 95%+     |
| Time to Detect      | 3-4 sec       | 1-2 sec      | <1 sec   |
|                     |               |              |          |
| **Port Scanning**   |               |              |          |
| Detection Rate      | 30-50%        | 70-90%       | 90%+     |
| Time to Detect      | 2-3 sec       | 1-2 sec      | <1 sec   |
|                     |               |              |          |
| **Malware C2**      |               |              |          |
| Detection Rate      | 0-20%         | 70-90%       | 80%+     |
| Time to Detect      | N/A           | 1-3 sec      | 1-2 sec  |
|                     |               |              |          |
| **Overall**         |               |              |          |
| False Positive Rate | Low           | Medium       | Low      |
| Resource Impact     | Low           | Medium       | Medium   |
| User Experience     | Good          | Fair         | Good     |

---

## 🔍 Detailed Analysis Sections

### Performance Bottlenecks

- Exact Time to Detect is not final because attack timestamps and Snort alert timestamps were not exported into one synchronized log source.
- Snort console displayed repeated `No preprocessors configured for policy 0` warnings. This should be reviewed because missing preprocessors can reduce DNS/HTTP protocol-aware detection.
- CPU and memory impact were not recorded during the screenshot-based malware C2 test, so resource impact remains pending.
- DNS anomaly detection was not confirmed in the visible alert output even though Flightsim generated suspicious C2 domain queries.

### False Positive Analysis

- False positives observed during the controlled malware C2 window: 0.
- This value is preliminary because the test window was narrow and centered on Flightsim traffic.
- Rule tuning should compare alerts against normal browsing, update checks, cloud sync and DNS traffic before final deployment.
- Whitelisting should be used carefully so common cloud/CDN traffic does not hide real C2 behavior.

### Rule Effectiveness

- Confirmed triggered rule: `[1:1000001:1] [DU AN] Phat hien ket noi Malware C2 (HTTPS)`.
- DNS-specific malware rules were expected but not confirmed in the screenshot.
- SSH/RDP/recon rules exist in `snort_custom_rules.conf`, but corresponding Snort alert logs were not captured yet.
- For IPS deployment, changing `alert` to `drop` is only sufficient when Snort is also running in inline/IPS mode; otherwise the rule will not actually block packets.

### Improvement Recommendations

- Enable persistent Snort logging, for example `fast` or unified output, then correlate alerts with Flightsim/brute-force/scan timestamps.
- Add DNS and HTTP/TLS-oriented Snort rules for C2 domains, suspicious SNI/Host values and repeated outbound beaconing.
- Test IPS mode separately with `drop` rules in an isolated lab before enabling it on the main network path.
- Harden open ports found by port scanning: restrict SSH/22, HTTP/80 and HTTPS/443 to required sources only.
- Record CPU, memory and network throughput during attacks to quantify Blue Force overhead.
- Build a clean baseline of normal outbound traffic to reduce false positives before final rule tuning.

---

## 📝 Notes Section

Use this space to document:

- Unexpected behaviors
- System anomalies
- Configuration issues
- Interesting findings
- Questions for team

```
OBSERVATIONS & NOTES:
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________
```

---

## ✅ Completion Checklist

- [ ] All 8 test scenarios executed
- [x] Snort malware C2 alerts captured from console screenshot
- [ ] System metrics recorded
- [x] Attack timeline documented for malware C2
- [ ] Detection rates calculated
- [x] Preliminary false positives counted for controlled malware C2 window
- [ ] Firewall logs reviewed
- [x] Network traffic analyzed for observed C2 HTTPS alerts
- [ ] Performance metrics recorded
- [ ] HTML report generated
- [x] CSV data exported for SSH/RDP/port scan tests
- [x] Analysis summary completed for Blue Force focus
- [x] Findings documented
- [x] Recommendations provided
- [ ] Report approved by team

---

**Report Status:** Blue Force results added - partial evidence complete  
**Next Steps:** Export full Snort/firewall logs, run remaining RDP rapid/range scan/rapid 1-1000 scan tests, then calculate final detection and prevention metrics  
**Follow-up:** Schedule analysis meeting upon completion

---

**Last Updated:** May 5, 2026  
**Version:** 1.1 (Blue Force Results Draft)
