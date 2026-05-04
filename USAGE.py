#!/usr/bin/env python3
"""
Usage Guide for Brute Force Test Suite
"""

def print_usage():
    guide = """
╔════════════════════════════════════════════════════════════════════╗
║           BRUTE FORCE TEST SUITE - USAGE GUIDE                    ║
╚════════════════════════════════════════════════════════════════════╝

📦 AVAILABLE SCRIPTS:

1. bruteforce_ssh_attack.py
   - SSH connection testing
   - Usage: python3 bruteforce_ssh_attack.py --host <IP> --user admin --wordlist passwords.txt
   - Modes: standard (1/s) or rapid (10/s)

2. bruteforce_rdp_attack.py
   - RDP connection testing
   - Usage: python3 bruteforce_rdp_attack.py --host <IP> --user admin --rapid
   - Tests RDP port 3389

3. port_scanner.py
   - Port reconnaissance
   - Usage: python3 port_scanner.py --host <IP> --common
   - Modes: common ports, custom range (1-65535), rapid

4. run_all_tests.py
   - Orchestrates all test scenarios
   - Usage: python3 run_all_tests.py --host <IP> --all

5. data_collector.py
   - Parses Snort IDS logs
   - Exports results to CSV, JSON, HTML
   - Usage: python3 data_collector.py

6. results_aggregator.py
   - Aggregates all test results
   - Generates summary reports
   - Usage: python3 results_aggregator.py

🔧 CONFIGURATION:

- passwords.txt: Password wordlist for brute force tests
- snort_custom_rules.conf: 15 custom Snort IDS detection rules

📊 OUTPUT FILES:

After running results_aggregator.py:
- brute_force_results.json   (Structured data)
- brute_force_results.csv    (Summary)
- brute_force_results.txt    (Human readable)
- ssh_results.csv            (SSH test details)
- rdp_results.csv            (RDP test details)
- port_scan_results.csv      (Port scan details)

🚀 QUICK START:

Step 1: Run all tests
    python3 run_all_tests.py --host 192.168.1.100 --all

Step 2: Collect results
    python3 results_aggregator.py

Step 3: View reports
    cat test_results/brute_force_results.txt
    
════════════════════════════════════════════════════════════════════
"""
    print(guide)

if __name__ == "__main__":
    print_usage()
