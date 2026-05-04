# Test Data Collection Template

## Log Collection Points

### 1. Snort Alert Logs Location
- **Linux**: `/var/log/snort/alert`
- **Windows**: `C:\Snort\log\alert`
- **Format**: Text-based alert log with structured format

### 2. Npcap Traffic Capture
- **File**: `capture.pcapng`
- **Location**: `./pcap_captures/`
- **Analysis**: Wireshark or tcpdump

### 3. System Metrics
- **CPU Usage**: Monitor via `top` or Task Manager
- **Memory Usage**: Monitor via `top` or Task Manager
- **Network Traffic**: Monitor via `nethogs` or Performance Monitor

---

## Data Collection Workflow

### Before Test
```
1. Start Snort IDS in logging mode
2. Start Npcap packet capture
3. Record system baseline (CPU, Memory)
4. Document target configuration
5. Synchronize timestamps across all systems
```

### During Test
```
1. Run attack simulation script
2. Monitor Snort alerts in real-time
3. Record start/end timestamps
4. Note any system anomalies
5. Keep terminal output for reference
```

### After Test
```
1. Stop Snort logging
2. Stop Npcap capture
3. Export Snort alerts to CSV/JSON
4. Parse pcap files
5. Collect final system metrics
6. Compile all data into report
```

---

## Data Fields to Collect

### Test Execution Data
- Test ID / Name
- Test Type (SSH/RDP/Port Scan)
- Date & Time Started
- Date & Time Ended
- Duration (seconds)
- Target IP:Port
- Attack Parameters

### Attack Metrics
- Total Attack Attempts
- Attack Rate (attempts/second)
- Unique Source IPs
- Unique Destination Ports
- Attack Success Rate (%)

### Detection Metrics
- Total Alerts Generated
- Alert Types (SSH, RDP, Recon, etc.)
- Time to First Alert (seconds)
- Time to Last Alert (seconds)
- Detection Rate (%)
- False Positive Count
- False Negative Count

### System Performance
- CPU Usage (%)
- Memory Usage (MB)
- Network Throughput (Mbps)
- Process Count
- File Descriptors Used

### Snort IDS Data
- Alert SID (Signature ID)
- Alert Priority (1=High, 2=Med, 3=Low)
- Alert Message
- Source IP & Port
- Destination IP & Port
- Protocol (TCP/UDP)
- Triggered Rules

---

## Data Analysis Tasks

### 1. Alert Correlation
```
For each attack, match:
- Attack attempt → Snort alert timestamp
- Calculate detection latency
- Identify missed attacks (false negatives)
- Identify spurious alerts (false positives)
```

### 2. Attack Pattern Analysis
```
Aggregate data by:
- Attack type (SSH/RDP/Scan)
- Source IP distribution
- Port distribution
- Time of day distribution
- Detect coordinated attacks
```

### 3. Effectiveness Metrics
```
Calculate:
- Detection rate = (detected / total) × 100
- False positive rate = (false alerts / total alerts) × 100
- Average detection time
- System impact
```

### 4. Rule Performance
```
For each Snort rule:
- Detection count
- False positive count
- Sensitivity (hit rate)
- Performance impact
```

---

## Expected Output Files

After running data collector:

```
test_results/
├── test_results.csv          # Tabular test data
├── test_results.json         # Structured test data
├── snort_alerts.csv          # All Snort alerts
├── test_report.html          # Visual HTML report
├── attack_summary.json       # Attack summary
└── analysis_report.txt       # Text analysis report
```

---

## Sample Data Records

### Test Result Record
```csv
timestamp,test_name,test_type,target,status,total_attempts,detections,detection_time_seconds,false_positives,cpu_usage_percent,memory_usage_mb
2026-05-04T14:32:15,SSH Brute-Force (Standard),SSH_BRUTEFORCE,192.168.1.100:22,SUCCESS,47,8,1.2,0,2.5,45
2026-05-04T14:35:20,RDP Brute-Force (Rapid),RDP_BRUTEFORCE,192.168.1.100:3389,SUCCESS,50,15,0.8,1,3.1,52
2026-05-04T14:38:45,Port Scan (1-1000),PORT_SCAN,192.168.1.100:various,SUCCESS,1000,5,2.3,0,1.8,40
```

### Snort Alert Record
```csv
sid,rev,priority,message,timestamp,source_ip,source_port,dest_ip,dest_port,protocol
3000002,1,1,SSH BRUTE-FORCE Possible Brute Force Attack Detected,05/04-14:32:15.234567,192.168.1.100,54321,192.168.1.1,22,TCP
3000006,1,1,RDP BRUTE-FORCE Multiple Connections Detected,05/04-14:35:20.123456,192.168.1.100,60000,192.168.1.1,3389,TCP
3000012,1,2,RECONNAISSANCE Port Scanning Activity Detected,05/04-14:38:45.456789,192.168.1.100,65432,192.168.1.1,443,TCP
```

---

## Data Collection Command References

### Generate Snort Alert CSV from Log File
```bash
python3 data_collector.py --parse-snort /var/log/snort/alert --output snort_alerts.csv
```

### Create Test Summary Report
```bash
python3 data_collector.py --generate-report test_results/ --format html
```

### Analyze Attack Patterns
```bash
python3 data_collector.py --analyze-attacks snort_alerts.csv --output analysis.json
```

### Generate Metrics Dashboard
```bash
python3 data_collector.py --metrics test_results.csv snort_alerts.csv --dashboard
```

---

## Important Notes

- **Timestamps**: Keep consistent timezone across all systems (UTC recommended)
- **Privacy**: Remove or anonymize real IP addresses before sharing data
- **Accuracy**: Manual review of automated parsing (especially Snort logs)
- **Retention**: Archive raw logs for audit trail (30 days minimum)
- **Backup**: Maintain multiple copies of collected data

---

**Last Updated**: May 4, 2026
