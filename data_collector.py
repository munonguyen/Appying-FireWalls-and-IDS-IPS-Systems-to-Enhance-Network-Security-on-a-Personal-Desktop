#!/usr/bin/env python3
"""
Data Collection & Analysis Tool for Attack Simulation Tests
Purpose: Collect, parse, and analyze logs from Snort IDS/IPS and attack simulations
Outputs: CSV reports, JSON data, and analysis summaries
"""

import os
import json
import csv
import re
import sys
from datetime import datetime
from pathlib import Path
from collections import defaultdict, Counter

class AttackDataCollector:
    """Collect and parse attack simulation data"""
    
    def __init__(self, output_dir="test_results"):
        self.output_dir = output_dir
        self.test_results = []
        self.snort_alerts = []
        self.traffic_data = []
        
        # Create output directory
        Path(output_dir).mkdir(exist_ok=True)
        
    def parse_snort_alert_log(self, log_file):
        """Parse Snort alert log file"""
        alerts = []
        
        try:
            with open(log_file, 'r') as f:
                current_alert = {}
                for line in f:
                    line = line.strip()
                    
                    # Match alert header
                    if line.startswith('[**]'):
                        if current_alert:
                            alerts.append(current_alert)
                        
                        # Parse alert message: [**] [SID:REV:PRIORITY] MESSAGE [**]
                        match = re.search(r'\[(\d+):(\d+):(\d)\].*\]\s(.*?)\s\[', line)
                        if match:
                            current_alert = {
                                'sid': match.group(1),
                                'rev': match.group(2),
                                'priority': match.group(3),
                                'message': match.group(4),
                                'timestamp': None,
                                'source_ip': None,
                                'dest_ip': None,
                                'protocol': None
                            }
                    
                    # Parse timestamp
                    elif line.startswith('['):
                        ts_match = re.search(r'\[(\d{2}/\d{2}-\d{2}:\d{2}:\d{2}\.\d+)\]', line)
                        if ts_match and current_alert:
                            current_alert['timestamp'] = ts_match.group(1)
                    
                    # Parse IPs and ports
                    elif '->' in line:
                        # Format: 192.168.1.100:54321 -> 192.168.1.1:22
                        match = re.search(r'(\d+\.\d+\.\d+\.\d+):(\d+)\s->\s(\d+\.\d+\.\d+\.\d+):(\d+)', line)
                        if match and current_alert:
                            current_alert['source_ip'] = match.group(1)
                            current_alert['source_port'] = match.group(2)
                            current_alert['dest_ip'] = match.group(3)
                            current_alert['dest_port'] = match.group(4)
                    
                    # Parse protocol
                    elif line.startswith('TCP') or line.startswith('UDP'):
                        parts = line.split()
                        if parts and current_alert:
                            current_alert['protocol'] = parts[0]
                
                # Add last alert
                if current_alert:
                    alerts.append(current_alert)
        
        except FileNotFoundError:
            print(f"Warning: Log file not found: {log_file}")
        
        self.snort_alerts.extend(alerts)
        return alerts
    
    def add_test_result(self, test_name, test_type, target, status, 
                       total_attempts=None, detections=None, 
                       detection_time=None, false_positives=None,
                       cpu_usage=None, memory_usage=None):
        """Add a test result to the collection"""
        result = {
            'timestamp': datetime.now().isoformat(),
            'test_name': test_name,
            'test_type': test_type,
            'target': target,
            'status': status,
            'total_attempts': total_attempts,
            'detections': detections,
            'detection_time_seconds': detection_time,
            'false_positives': false_positives,
            'cpu_usage_percent': cpu_usage,
            'memory_usage_mb': memory_usage
        }
        self.test_results.append(result)
        return result
    
    def generate_attack_summary(self):
        """Generate summary of all attacks detected"""
        if not self.snort_alerts:
            return None
        
        summary = {
            'total_alerts': len(self.snort_alerts),
            'alerts_by_type': defaultdict(int),
            'alerts_by_priority': defaultdict(int),
            'alerts_by_source_ip': defaultdict(int),
            'attacks_detected': [],
            'timeline': []
        }
        
        for alert in self.snort_alerts:
            msg = alert.get('message', 'UNKNOWN')
            summary['alerts_by_type'][msg] += 1
            summary['alerts_by_priority'][alert.get('priority', '3')] += 1
            
            source = alert.get('source_ip', 'UNKNOWN')
            summary['alerts_by_source_ip'][source] += 1
            
            # Categorize attack type
            if 'SSH' in msg or 'BRUTE' in msg:
                summary['attacks_detected'].append({
                    'type': 'SSH_BRUTEFORCE',
                    'timestamp': alert.get('timestamp'),
                    'source_ip': source,
                    'dest_port': alert.get('dest_port')
                })
            elif 'RDP' in msg:
                summary['attacks_detected'].append({
                    'type': 'RDP_BRUTEFORCE',
                    'timestamp': alert.get('timestamp'),
                    'source_ip': source,
                    'dest_port': alert.get('dest_port')
                })
            elif 'RECONNAISSANCE' in msg or 'portscan' in msg.lower():
                summary['attacks_detected'].append({
                    'type': 'PORT_SCAN',
                    'timestamp': alert.get('timestamp'),
                    'source_ip': source
                })
            elif 'MALWARE' in msg or 'C2' in msg or 'CNC' in msg:
                summary['attacks_detected'].append({
                    'type': 'MALWARE_C2',
                    'timestamp': alert.get('timestamp'),
                    'source_ip': source,
                    'dest_ip': alert.get('dest_ip'),
                    'dest_port': alert.get('dest_port')
                })
        
        return summary
    
    def save_to_csv(self, filename="test_results.csv"):
        """Save test results to CSV"""
        filepath = os.path.join(self.output_dir, filename)
        
        if not self.test_results:
            print("No test results to save")
            return None
        
        try:
            with open(filepath, 'w', newline='') as csvfile:
                fieldnames = self.test_results[0].keys()
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                writer.writerows(self.test_results)
            
            print(f"✅ Results saved to: {filepath}")
            return filepath
        except Exception as e:
            print(f"❌ Error saving CSV: {str(e)}")
            return None
    
    def save_alerts_to_csv(self, filename="snort_alerts.csv"):
        """Save Snort alerts to CSV"""
        filepath = os.path.join(self.output_dir, filename)
        
        if not self.snort_alerts:
            print("No alerts to save")
            return None
        
        try:
            with open(filepath, 'w', newline='') as csvfile:
                fieldnames = self.snort_alerts[0].keys()
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                writer.writerows(self.snort_alerts)
            
            print(f"✅ Alerts saved to: {filepath}")
            return filepath
        except Exception as e:
            print(f"❌ Error saving alerts CSV: {str(e)}")
            return None
    
    def save_to_json(self, filename="test_results.json"):
        """Save all data to JSON"""
        filepath = os.path.join(self.output_dir, filename)
        
        try:
            data = {
                'timestamp': datetime.now().isoformat(),
                'test_results': self.test_results,
                'snort_alerts': self.snort_alerts,
                'summary': self.generate_attack_summary()
            }
            
            with open(filepath, 'w') as jsonfile:
                json.dump(data, jsonfile, indent=2)
            
            print(f"✅ Data saved to: {filepath}")
            return filepath
        except Exception as e:
            print(f"❌ Error saving JSON: {str(e)}")
            return None
    
    def generate_html_report(self, filename="test_report.html"):
        """Generate HTML report"""
        filepath = os.path.join(self.output_dir, filename)
        summary = self.generate_attack_summary()
        
        html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>IDS/IPS Attack Simulation Test Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; background-color: #f5f5f5; }}
        .container {{ max-width: 1200px; margin: 0 auto; background-color: white; padding: 20px; border-radius: 5px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }}
        h1 {{ color: #333; border-bottom: 3px solid #007bff; padding-bottom: 10px; }}
        h2 {{ color: #555; margin-top: 30px; }}
        table {{ width: 100%; border-collapse: collapse; margin: 15px 0; }}
        th {{ background-color: #007bff; color: white; padding: 12px; text-align: left; }}
        td {{ padding: 10px; border-bottom: 1px solid #ddd; }}
        tr:hover {{ background-color: #f9f9f9; }}
        .alert {{ background-color: #fff3cd; border-left: 4px solid #ffc107; padding: 10px; margin: 10px 0; }}
        .success {{ color: green; }}
        .failure {{ color: red; }}
        .metric {{ display: inline-block; margin: 10px 20px 10px 0; }}
        .metric-value {{ font-size: 24px; font-weight: bold; color: #007bff; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🔒 IDS/IPS Attack Simulation Test Report</h1>
        <p><strong>Generated:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        
        <h2>📊 Summary Statistics</h2>
        <div class="metric">
            <div>Total Tests</div>
            <div class="metric-value">{len(self.test_results)}</div>
        </div>
        <div class="metric">
            <div>Total Alerts</div>
            <div class="metric-value">{len(self.snort_alerts)}</div>
        </div>
"""
        
        if summary:
            html_content += f"""
        <div class="metric">
            <div>Attacks Detected</div>
            <div class="metric-value">{len(summary['attacks_detected'])}</div>
        </div>

        <h2>🎯 Attacks by Type</h2>
        <table>
            <tr><th>Attack Type</th><th>Count</th></tr>
"""
            for attack_type, alerts in summary['alerts_by_type'].items():
                html_content += f"<tr><td>{attack_type}</td><td>{alerts}</td></tr>\n"
            
            html_content += """
        </table>

        <h2>⚠️ Alert Priority Distribution</h2>
        <table>
            <tr><th>Priority</th><th>Count</th></tr>
"""
            for priority in sorted(summary['alerts_by_priority'].keys()):
                count = summary['alerts_by_priority'][priority]
                priority_name = {1: "High", 2: "Medium", 3: "Low"}.get(int(priority), "Unknown")
                html_content += f"<tr><td>{priority_name} ({priority})</td><td>{count}</td></tr>\n"
            
            html_content += """
        </table>

        <h2>🔍 Source IPs of Attacks</h2>
        <table>
            <tr><th>Source IP</th><th>Alert Count</th></tr>
"""
            for ip in sorted(summary['alerts_by_source_ip'].keys(), 
                            key=lambda x: summary['alerts_by_source_ip'][x], 
                            reverse=True):
                count = summary['alerts_by_source_ip'][ip]
                html_content += f"<tr><td>{ip}</td><td>{count}</td></tr>\n"
        
        html_content += """
        </table>

        <h2>📈 Test Results</h2>
        <table>
            <tr>
                <th>Test Name</th>
                <th>Type</th>
                <th>Target</th>
                <th>Status</th>
                <th>Attempts</th>
                <th>Detections</th>
                <th>Detection Time (sec)</th>
            </tr>
"""
        
        for result in self.test_results:
            status_class = "success" if result['status'] == 'SUCCESS' else "failure"
            html_content += f"""
            <tr>
                <td>{result['test_name']}</td>
                <td>{result['test_type']}</td>
                <td>{result['target']}</td>
                <td class="{status_class}">{result['status']}</td>
                <td>{result['total_attempts'] or 'N/A'}</td>
                <td>{result['detections'] or 'N/A'}</td>
                <td>{result['detection_time_seconds'] or 'N/A'}</td>
            </tr>
"""
        
        html_content += """
        </table>

        <h2>🚨 Detailed Alerts</h2>
        <table>
            <tr>
                <th>Timestamp</th>
                <th>Message</th>
                <th>Source IP</th>
                <th>Dest IP</th>
                <th>Priority</th>
            </tr>
"""
        
        for alert in self.snort_alerts[:100]:  # Limit to first 100 for readability
            html_content += f"""
            <tr>
                <td>{alert.get('timestamp', 'N/A')}</td>
                <td>{alert.get('message', 'N/A')}</td>
                <td>{alert.get('source_ip', 'N/A')}</td>
                <td>{alert.get('dest_ip', 'N/A')}</td>
                <td>{alert.get('priority', 'N/A')}</td>
            </tr>
"""
        
        html_content += """
        </table>

        <hr>
        <p style="color: #999; font-size: 12px;">Report generated by IDS/IPS Test Data Collector</p>
    </div>
</body>
</html>
"""
        
        try:
            with open(filepath, 'w') as htmlfile:
                htmlfile.write(html_content)
            print(f"✅ HTML report saved to: {filepath}")
            return filepath
        except Exception as e:
            print(f"❌ Error saving HTML: {str(e)}")
            return None
    
    def print_summary(self):
        """Print summary to console"""
        print("\n" + "="*70)
        print("DATA COLLECTION SUMMARY")
        print("="*70)
        
        print(f"\n📊 Test Results Collected: {len(self.test_results)}")
        for result in self.test_results:
            print(f"  - {result['test_name']}: {result['status']}")
        
        print(f"\n🚨 Snort Alerts Parsed: {len(self.snort_alerts)}")
        
        summary = self.generate_attack_summary()
        if summary:
            print(f"\n📈 Attack Summary:")
            print(f"  - SSH Brute-Force: {sum(1 for a in summary['attacks_detected'] if a['type'] == 'SSH_BRUTEFORCE')}")
            print(f"  - RDP Brute-Force: {sum(1 for a in summary['attacks_detected'] if a['type'] == 'RDP_BRUTEFORCE')}")
            print(f"  - Port Scans: {sum(1 for a in summary['attacks_detected'] if a['type'] == 'PORT_SCAN')}")
            print(f"  - Malware/C2: {sum(1 for a in summary['attacks_detected'] if a['type'] == 'MALWARE_C2')}")
        
        print("\n" + "="*70 + "\n")


def main():
    collector = AttackDataCollector(output_dir="test_results")
    
    print("🔍 Attack Data Collection & Analysis Tool")
    print("="*70)
    
    # Example: Add test results (in real usage, these would come from actual tests)
    collector.add_test_result(
        test_name="SSH Brute-Force (Standard)",
        test_type="SSH_BRUTEFORCE",
        target="192.168.1.100:22",
        status="SUCCESS",
        total_attempts=47,
        detections=8,
        detection_time=1.2,
        false_positives=0,
        cpu_usage=2.5,
        memory_usage=45
    )
    
    collector.add_test_result(
        test_name="RDP Brute-Force (Rapid)",
        test_type="RDP_BRUTEFORCE",
        target="192.168.1.100:3389",
        status="SUCCESS",
        total_attempts=50,
        detections=15,
        detection_time=0.8,
        false_positives=1,
        cpu_usage=3.1,
        memory_usage=52
    )
    
    collector.add_test_result(
        test_name="Port Scan (1-1000)",
        test_type="PORT_SCAN",
        target="192.168.1.100:various",
        status="SUCCESS",
        total_attempts=1000,
        detections=5,
        detection_time=2.3,
        false_positives=0,
        cpu_usage=1.8,
        memory_usage=40
    )
    
    # Parse Snort logs (example)
    # collector.parse_snort_alert_log('/var/log/snort/alert')
    
    # Generate outputs
    collector.save_to_csv()
    collector.save_to_json()
    collector.generate_html_report()
    collector.print_summary()
    
    print("✅ Data collection complete!")
    print(f"📁 Results saved to: {collector.output_dir}/")


if __name__ == '__main__':
    main()
