#!/usr/bin/env python3
"""
Results Aggregator for Brute Force Tests
"""

import json
import csv
import os
from datetime import datetime
from pathlib import Path

class ResultsAggregator:
    def __init__(self, output_dir="test_results"):
        self.output_dir = output_dir
        self.results = {
            "timestamp": datetime.now().isoformat(),
            "ssh_tests": [],
            "rdp_tests": [],
            "port_scans": [],
            "summary": {}
        }
        Path(output_dir).mkdir(exist_ok=True)
    
    def add_ssh_result(self, target, port, username, total_attempts, 
                       successful, duration, rate):
        """Add SSH brute-force test result"""
        self.results["ssh_tests"].append({
            "target": target,
            "port": port,
            "username": username,
            "total_attempts": total_attempts,
            "successful": successful,
            "duration_seconds": duration,
            "attempts_per_second": rate,
            "timestamp": datetime.now().isoformat()
        })
    
    def add_rdp_result(self, target, port, username, total_attempts,
                       successful, duration, rate):
        """Add RDP brute-force test result"""
        self.results["rdp_tests"].append({
            "target": target,
            "port": port,
            "username": username,
            "total_attempts": total_attempts,
            "successful": successful,
            "duration_seconds": duration,
            "attempts_per_second": rate,
            "timestamp": datetime.now().isoformat()
        })
    
    def add_port_scan_result(self, target, scan_type, open_ports, 
                             closed_ports, duration, rate):
        """Add port scanning test result"""
        self.results["port_scans"].append({
            "target": target,
            "scan_type": scan_type,
            "open_ports": open_ports,
            "closed_ports": closed_ports,
            "total_scanned": len(open_ports) + len(closed_ports),
            "duration_seconds": duration,
            "scans_per_second": rate,
            "timestamp": datetime.now().isoformat()
        })
    
    def calculate_summary(self):
        """Calculate summary statistics"""
        summary = {
            "total_ssh_tests": len(self.results["ssh_tests"]),
            "total_rdp_tests": len(self.results["rdp_tests"]),
            "total_port_scans": len(self.results["port_scans"]),
            "test_date": self.results["timestamp"]
        }
        
        if self.results["ssh_tests"]:
            ssh_data = self.results["ssh_tests"]
            summary["ssh_avg_duration"] = sum(t["duration_seconds"] for t in ssh_data) / len(ssh_data)
            summary["ssh_total_attempts"] = sum(t["total_attempts"] for t in ssh_data)
            summary["ssh_successful"] = sum(t["successful"] for t in ssh_data)
        
        if self.results["rdp_tests"]:
            rdp_data = self.results["rdp_tests"]
            summary["rdp_avg_duration"] = sum(t["duration_seconds"] for t in rdp_data) / len(rdp_data)
            summary["rdp_total_attempts"] = sum(t["total_attempts"] for t in rdp_data)
            summary["rdp_successful"] = sum(t["successful"] for t in rdp_data)
        
        if self.results["port_scans"]:
            scan_data = self.results["port_scans"]
            summary["scan_avg_duration"] = sum(t["duration_seconds"] for t in scan_data) / len(scan_data)
            summary["total_ports_scanned"] = sum(t["total_scanned"] for t in scan_data)
        
        self.results["summary"] = summary
        return summary
    
    def save_json(self, filename="brute_force_results.json"):
        """Save results to JSON"""
        self.calculate_summary()
        filepath = os.path.join(self.output_dir, filename)
        with open(filepath, 'w') as f:
            json.dump(self.results, f, indent=2)
        return filepath
    
    def save_csv(self, filename="brute_force_results.csv"):
        """Save results to CSV"""
        filepath = os.path.join(self.output_dir, filename)
        
        # Save SSH tests
        if self.results["ssh_tests"]:
            ssh_file = os.path.join(self.output_dir, "ssh_results.csv")
            with open(ssh_file, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=self.results["ssh_tests"][0].keys())
                writer.writeheader()
                writer.writerows(self.results["ssh_tests"])
        
        # Save RDP tests
        if self.results["rdp_tests"]:
            rdp_file = os.path.join(self.output_dir, "rdp_results.csv")
            with open(rdp_file, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=self.results["rdp_tests"][0].keys())
                writer.writeheader()
                writer.writerows(self.results["rdp_tests"])
        
        # Save port scans
        if self.results["port_scans"]:
            port_file = os.path.join(self.output_dir, "port_scan_results.csv")
            with open(port_file, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=self.results["port_scans"][0].keys())
                writer.writeheader()
                writer.writerows(self.results["port_scans"])
        
        return filepath
    
    def save_text_report(self, filename="brute_force_results.txt"):
        """Save results to text report"""
        self.calculate_summary()
        filepath = os.path.join(self.output_dir, filename)
        
        with open(filepath, 'w') as f:
            f.write("="*70 + "\n")
            f.write("BRUTE FORCE TEST RESULTS SUMMARY\n")
            f.write("="*70 + "\n\n")
            f.write(f"Test Date: {self.results['timestamp']}\n\n")
            
            summary = self.results["summary"]
            f.write("SUMMARY STATISTICS\n")
            f.write("-"*70 + "\n")
            f.write(f"Total SSH Tests:      {summary.get('total_ssh_tests', 0)}\n")
            f.write(f"Total RDP Tests:      {summary.get('total_rdp_tests', 0)}\n")
            f.write(f"Total Port Scans:     {summary.get('total_port_scans', 0)}\n")
            
            if "ssh_total_attempts" in summary:
                f.write(f"\nSSH Attack Summary:\n")
                f.write(f"  Total Attempts:     {summary['ssh_total_attempts']}\n")
                f.write(f"  Successful:         {summary['ssh_successful']}\n")
                f.write(f"  Avg Duration:       {summary['ssh_avg_duration']:.2f}s\n")
            
            if "rdp_total_attempts" in summary:
                f.write(f"\nRDP Attack Summary:\n")
                f.write(f"  Total Attempts:     {summary['rdp_total_attempts']}\n")
                f.write(f"  Successful:         {summary['rdp_successful']}\n")
                f.write(f"  Avg Duration:       {summary['rdp_avg_duration']:.2f}s\n")
            
            if "total_ports_scanned" in summary:
                f.write(f"\nPort Scan Summary:\n")
                f.write(f"  Total Ports Scanned: {summary['total_ports_scanned']}\n")
                f.write(f"  Avg Duration:       {summary['scan_avg_duration']:.2f}s\n")
            
            f.write("\n" + "="*70 + "\n")
            f.write("DETAILED RESULTS\n")
            f.write("="*70 + "\n\n")
            
            if self.results["ssh_tests"]:
                f.write("SSH BRUTE FORCE TESTS:\n")
                f.write("-"*70 + "\n")
                for i, test in enumerate(self.results["ssh_tests"], 1):
                    f.write(f"\nTest #{i}:\n")
                    f.write(f"  Target:      {test['target']}:{test['port']}\n")
                    f.write(f"  User:        {test['username']}\n")
                    f.write(f"  Attempts:    {test['total_attempts']}\n")
                    f.write(f"  Successful:  {test['successful']}\n")
                    f.write(f"  Duration:    {test['duration_seconds']:.2f}s\n")
                    f.write(f"  Rate:        {test['attempts_per_second']:.2f}/s\n")
            
            if self.results["rdp_tests"]:
                f.write("\n\nRDP BRUTE FORCE TESTS:\n")
                f.write("-"*70 + "\n")
                for i, test in enumerate(self.results["rdp_tests"], 1):
                    f.write(f"\nTest #{i}:\n")
                    f.write(f"  Target:      {test['target']}:{test['port']}\n")
                    f.write(f"  User:        {test['username']}\n")
                    f.write(f"  Attempts:    {test['total_attempts']}\n")
                    f.write(f"  Successful:  {test['successful']}\n")
                    f.write(f"  Duration:    {test['duration_seconds']:.2f}s\n")
                    f.write(f"  Rate:        {test['attempts_per_second']:.2f}/s\n")
            
            if self.results["port_scans"]:
                f.write("\n\nPORT SCANNING TESTS:\n")
                f.write("-"*70 + "\n")
                for i, test in enumerate(self.results["port_scans"], 1):
                    f.write(f"\nTest #{i}:\n")
                    f.write(f"  Target:      {test['target']}\n")
                    f.write(f"  Scan Type:   {test['scan_type']}\n")
                    f.write(f"  Total Scanned: {test['total_scanned']}\n")
                    f.write(f"  Duration:    {test['duration_seconds']:.2f}s\n")
                    f.write(f"  Rate:        {test['scans_per_second']:.2f}/s\n")
        
        return filepath
    
    def print_summary(self):
        """Print summary to console"""
        self.calculate_summary()
        summary = self.results["summary"]
        
        print("\n" + "="*50)
        print("BRUTE FORCE TEST SUMMARY")
        print("="*50)
        print(f"SSH Tests:     {summary.get('total_ssh_tests', 0)}")
        print(f"RDP Tests:     {summary.get('total_rdp_tests', 0)}")
        print(f"Port Scans:    {summary.get('total_port_scans', 0)}")
        
        if "ssh_total_attempts" in summary:
            print(f"\nSSH: {summary['ssh_total_attempts']} attempts, "
                  f"{summary['ssh_successful']} successful")
        
        if "rdp_total_attempts" in summary:
            print(f"RDP: {summary['rdp_total_attempts']} attempts, "
                  f"{summary['rdp_successful']} successful")
        
        if "total_ports_scanned" in summary:
            print(f"Ports: {summary['total_ports_scanned']} scanned")
        
        print("="*50 + "\n")


if __name__ == "__main__":
    agg = ResultsAggregator()
    
    # Example: Add test results
    agg.add_ssh_result("192.168.1.100", 22, "admin", 100, 0, 45.2, 2.21)
    agg.add_ssh_result("192.168.1.100", 22, "admin", 100, 0, 10.1, 9.9)
    agg.add_rdp_result("192.168.1.100", 3389, "admin", 50, 0, 25.5, 1.96)
    agg.add_port_scan_result("192.168.1.100", "common", [22, 80, 443], [21, 23, 25], 5.2, 3.08)
    
    # Save results
    agg.save_json()
    agg.save_csv()
    agg.save_text_report()
    agg.print_summary()
    
    print("[+] Results saved:")
    print("    - test_results/brute_force_results.json")
    print("    - test_results/brute_force_results.csv")
    print("    - test_results/brute_force_results.txt")
