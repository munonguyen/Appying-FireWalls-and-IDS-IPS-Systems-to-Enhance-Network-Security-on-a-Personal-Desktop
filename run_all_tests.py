#!/usr/bin/env python3
"""
Comprehensive IDS/IPS Test Suite
Purpose: Run all attack simulations (SSH Brute-Force, RDP Brute-Force, Port Scanning)
Usage: python3 run_all_tests.py --host <target_ip> --monitor

This script orchestrates all attack scenarios for comprehensive IDS/IPS testing.
"""

import subprocess
import sys
import argparse
import time
from datetime import datetime
import os

class TestSuite:
    def __init__(self, target_host, monitor=False):
        self.target_host = target_host
        self.monitor = monitor
        self.results = []
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
    
    def log(self, message):
        """Print timestamped log message"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"[{timestamp}] {message}")
    
    def run_test(self, test_name, command, description):
        """Run a single test"""
        self.log(f"\n{'='*70}")
        self.log(f"TEST: {test_name}")
        self.log(f"Description: {description}")
        self.log(f"Target: {self.target_host}")
        self.log(f"Command: {command}")
        self.log(f"{'='*70}\n")
        
        if self.monitor:
            self.log("⚠️  MONITORING MODE: Make sure Snort is running!")
            input("Press Enter to start test...")
        
        start_time = time.time()
        
        try:
            result = subprocess.run(command, shell=True, cwd=self.script_dir)
            elapsed = time.time() - start_time
            
            status = "✅ SUCCESS" if result.returncode == 0 else "❌ FAILED"
            self.results.append({
                'name': test_name,
                'status': status,
                'duration': elapsed,
                'description': description
            })
            
            self.log(f"\n{status} - Duration: {elapsed:.2f} seconds")
            
        except Exception as e:
            self.log(f"❌ ERROR: {str(e)}")
            self.results.append({
                'name': test_name,
                'status': '❌ ERROR',
                'duration': 0,
                'description': description
            })
    
    def test_ssh_bruteforce_standard(self):
        """Test 1: Standard SSH Brute-Force with delays"""
        command = f"""
python3 bruteforce_ssh_attack.py \\
    --host {self.target_host} \\
    --port 22 \\
    --user admin \\
    --wordlist passwords.txt \\
    --delay 1
        """
        self.run_test(
            "SSH Brute-Force (Standard)",
            command,
            "SSH brute-force attack with 1-second delays between attempts"
        )
    
    def test_ssh_bruteforce_rapid(self):
        """Test 2: Rapid SSH Brute-Force"""
        command = f"""
python3 bruteforce_ssh_attack.py \\
    --host {self.target_host} \\
    --port 22 \\
    --user admin \\
    --rapid \\
    --attempts 10
        """
        self.run_test(
            "SSH Brute-Force (Rapid)",
            command,
            "SSH brute-force attack with 10 attempts per second (easy to detect)"
        )
    
    def test_rdp_bruteforce_standard(self):
        """Test 3: Standard RDP Brute-Force"""
        command = f"""
python3 bruteforce_rdp_attack.py \\
    --host {self.target_host} \\
    --port 3389 \\
    --user admin \\
    --wordlist passwords.txt \\
    --delay 0.5
        """
        self.run_test(
            "RDP Brute-Force (Standard)",
            command,
            "RDP brute-force attack with 0.5-second delays between attempts"
        )
    
    def test_rdp_bruteforce_rapid(self):
        """Test 4: Rapid RDP Brute-Force"""
        command = f"""
python3 bruteforce_rdp_attack.py \\
    --host {self.target_host} \\
    --port 3389 \\
    --user admin \\
    --rapid \\
    --attempts 50
        """
        self.run_test(
            "RDP Brute-Force (Rapid)",
            command,
            "RDP brute-force attack with 50 connection attempts (easy to detect)"
        )
    
    def test_port_scan_common(self):
        """Test 5: Common Port Scan"""
        command = f"""
python3 port_scanner.py \\
    --host {self.target_host} \\
    --common
        """
        self.run_test(
            "Port Scan (Common Ports)",
            command,
            "Network reconnaissance: scan common service ports"
        )
    
    def test_port_scan_range(self):
        """Test 6: Port Range Scan"""
        command = f"""
python3 port_scanner.py \\
    --host {self.target_host} \\
    --range 20 100
        """
        self.run_test(
            "Port Scan (Range 20-100)",
            command,
            "Network reconnaissance: scan port range 20-100"
        )
    
    def test_port_scan_rapid(self):
        """Test 7: Rapid Port Scan"""
        command = f"""
python3 port_scanner.py \\
    --host {self.target_host} \\
    --ports 1-1000 \\
    --rapid
        """
        self.run_test(
            "Port Scan (Rapid 1-1000)",
            command,
            "Network reconnaissance: rapid port scan 1-1000 (easy to detect)"
        )
    
    def run_all_tests(self):
        """Run complete test suite"""
        self.log("\n" + "="*70)
        self.log("COMPREHENSIVE IDS/IPS TEST SUITE")
        self.log("="*70)
        self.log(f"Target Host: {self.target_host}")
        self.log(f"Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        self.log(f"Monitor Mode: {'ENABLED' if self.monitor else 'DISABLED'}")
        self.log("="*70 + "\n")
        
        # Run all tests
        self.test_ssh_bruteforce_standard()
        time.sleep(2)
        
        self.test_ssh_bruteforce_rapid()
        time.sleep(2)
        
        self.test_rdp_bruteforce_standard()
        time.sleep(2)
        
        self.test_rdp_bruteforce_rapid()
        time.sleep(2)
        
        self.test_port_scan_common()
        time.sleep(2)
        
        self.test_port_scan_range()
        time.sleep(2)
        
        self.test_port_scan_rapid()
        
        # Print summary
        self.print_summary()
    
    def run_selected_test(self, test_number):
        """Run a single selected test"""
        tests = {
            1: self.test_ssh_bruteforce_standard,
            2: self.test_ssh_bruteforce_rapid,
            3: self.test_rdp_bruteforce_standard,
            4: self.test_rdp_bruteforce_rapid,
            5: self.test_port_scan_common,
            6: self.test_port_scan_range,
            7: self.test_port_scan_rapid,
        }
        
        if test_number in tests:
            self.log(f"Starting Test #{test_number}")
            tests[test_number]()
            self.print_summary()
        else:
            print(f"Error: Test #{test_number} not found")
    
    def print_summary(self):
        """Print test summary"""
        print(f"\n{'='*70}")
        print(f"TEST SUMMARY")
        print(f"{'='*70}")
        
        for i, result in enumerate(self.results, 1):
            status_symbol = "✅" if "SUCCESS" in result['status'] else "❌"
            print(f"{i}. {status_symbol} {result['name']}")
            print(f"   Status: {result['status']}")
            print(f"   Duration: {result['duration']:.2f}s")
            print()
        
        print(f"{'='*70}")
        print(f"Total Tests: {len(self.results)}")
        print(f"Passed: {len([r for r in self.results if 'SUCCESS' in r['status']])}")
        print(f"Failed: {len([r for r in self.results if 'FAILED' in r['status'] or 'ERROR' in r['status']])}")
        print(f"Total Duration: {sum(r['duration'] for r in self.results):.2f}s")
        print(f"{'='*70}\n")


def print_menu():
    """Print test menu"""
    print("\n" + "="*70)
    print("AVAILABLE TESTS")
    print("="*70)
    print("1. SSH Brute-Force (Standard) - 1 second delay between attempts")
    print("2. SSH Brute-Force (Rapid)    - 10 attempts per second")
    print("3. RDP Brute-Force (Standard) - 0.5 second delay between attempts")
    print("4. RDP Brute-Force (Rapid)    - 50 rapid connection attempts")
    print("5. Port Scan (Common Ports)   - Scan well-known service ports")
    print("6. Port Scan (Range 20-100)   - Scan port range")
    print("7. Port Scan (Rapid 1-1000)   - Rapid scan of 1000 ports")
    print("8. Run All Tests              - Execute all tests in sequence")
    print("9. Exit")
    print("="*70 + "\n")


def main():
    parser = argparse.ArgumentParser(
        description='Comprehensive IDS/IPS Test Suite',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run all tests with Snort monitoring
  python3 run_all_tests.py --host 192.168.1.100 --monitor --all
  
  # Run specific test
  python3 run_all_tests.py --host 192.168.1.100 --test 1
  
  # Interactive mode
  python3 run_all_tests.py --host 192.168.1.100 --interactive

WARNING: Only use on systems you own or have explicit permission to test!
        """
    )
    
    parser.add_argument('--host', help='Target host IP address')
    parser.add_argument('--monitor', action='store_true', help='Monitor mode (wait for user before each test)')
    parser.add_argument('--all', action='store_true', help='Run all tests automatically')
    parser.add_argument('--test', type=int, help='Run specific test number (1-7)')
    parser.add_argument('--interactive', action='store_true', help='Interactive menu mode')
    
    args = parser.parse_args()
    
    # Default to interactive if no args
    if not args.host and not args.all and args.test is None:
        args.interactive = True
    
    # Get target host
    if not args.host:
        args.host = input("Enter target host IP address: ").strip()
        if not args.host:
            print("Error: Target host required")
            sys.exit(1)
    
    # Create test suite
    suite = TestSuite(args.host, monitor=args.monitor)
    
    # Run tests
    if args.interactive:
        while True:
            print_menu()
            choice = input("Select test (1-9): ").strip()
            
            if choice == '9':
                print("Exiting...")
                break
            elif choice == '8':
                suite.run_all_tests()
            elif choice.isdigit() and 1 <= int(choice) <= 7:
                suite.run_selected_test(int(choice))
            else:
                print("Invalid choice!")
    
    elif args.test:
        suite.run_selected_test(args.test)
    
    elif args.all:
        suite.run_all_tests()


if __name__ == '__main__':
    main()
