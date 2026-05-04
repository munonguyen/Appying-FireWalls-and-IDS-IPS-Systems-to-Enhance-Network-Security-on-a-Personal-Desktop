#!/usr/bin/env python3
"""
RDP Connection Attack Tool
"""

import socket
import sys
import argparse
import time
from datetime import datetime

class RDPBruteForceSimulator:
    
    def __init__(self, host, port=3389, username='admin'):
        self.host = host
        self.port = port
        self.username = username
        self.total_attempts = 0
        self.successful_attempts = 0
        self.failed_attempts = 0
        
    def attempt_connection(self, password):
        """Attempt RDP connection"""
        try:
            # Create socket connection
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)
            
            print(f"[{datetime.now().strftime('%H:%M:%S')}] RDP Connection attempt: {self.username}:{password}")
            
            # Try to connect to RDP port
            result = sock.connect_ex((self.host, self.port))
            
            if result == 0:
                print(f"[OPEN] RDP port {self.port} is open on {self.host}")
                self.successful_attempts += 1
                sock.close()
                return True
            else:
                print(f"[CLOSED] Could not connect to {self.host}:{self.port}")
                self.failed_attempts += 1
                sock.close()
                return False
                
        except socket.timeout:
            print(f"[TIMEOUT] Connection to {self.host}:{self.port} timed out")
            self.failed_attempts += 1
            return False
        except Exception as e:
            print(f"[ERROR] {str(e)}")
            self.failed_attempts += 1
            return False
        finally:
            self.total_attempts += 1
    
    def run_wordlist_attack(self, wordlist_file, delay_between_attempts=0.5):
        """Run RDP brute-force attack"""
        try:
            with open(wordlist_file, 'r') as f:
                passwords = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print(f"Error: Wordlist file '{wordlist_file}' not found!")
            sys.exit(1)
        
        print(f"\n[*] Starting RDP Brute-Force Attack")
        print(f"[*] Target: {self.host}:{self.port}")
        print(f"[*] Username: {self.username}")
        print(f"[*] Passwords to try: {len(passwords)}")
        print(f"[*] Delay between attempts: {delay_between_attempts} second(s)")
        print(f"[*] Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        start_time = time.time()
        
        for i, password in enumerate(passwords, 1):
            self.attempt_connection(password)
            
            # Delay between attempts (to be detected by IDS)
            time.sleep(delay_between_attempts)
            
            # Print progress
            if i % 5 == 0:
                print(f"[*] Progress: {i}/{len(passwords)} attempts")
        
        elapsed = time.time() - start_time
        self.print_summary(elapsed)
    
    def rapid_fire_attack(self, num_attempts=50, attempts_per_second=10):
        """Rapid-fire RDP connection attempts"""
        print(f"\n[*] Starting Rapid-Fire RDP Brute-Force Attack")
        print(f"[*] Target: {self.host}:{self.port}")
        print(f"[*] Username: {self.username}")
        print(f"[*] Total attempts: {num_attempts}")
        print(f"[*] Attempts per second: {attempts_per_second}")
        print(f"[*] Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        start_time = time.time()
        delay = 1.0 / attempts_per_second
        
        for i in range(1, num_attempts + 1):
            password = f"Password{i}"
            self.attempt_connection(password)
            time.sleep(delay)
            
            if i % 10 == 0:
                print(f"[*] Progress: {i}/{num_attempts} attempts")
        
        elapsed = time.time() - start_time
        self.print_summary(elapsed)
    
    def print_summary(self, elapsed_time):
        """Print attack summary"""
        print(f"\n{'='*60}")
        print(f"RDP ATTACK SUMMARY")
        print(f"{'='*60}")
        print(f"Total Attempts:       {self.total_attempts}")
        print(f"Successful (Open):    {self.successful_attempts}")
        print(f"Failed Attempts:      {self.failed_attempts}")
        print(f"Duration:             {elapsed_time:.2f} seconds")
        if self.total_attempts > 0:
            print(f"Attack Rate:          {self.total_attempts/elapsed_time:.2f} attempts/second")
        print(f"{'='*60}\n")


def main():
    parser = argparse.ArgumentParser(description='RDP Connection Tool')
    
    parser.add_argument('--host', required=True, help='Target RDP host IP address')
    parser.add_argument('--port', type=int, default=3389, help='Target RDP port (default: 3389)')
    parser.add_argument('--user', default='admin', help='Username to attack (default: admin)')
    parser.add_argument('--wordlist', help='Password wordlist file')
    parser.add_argument('--delay', type=float, default=0.5, help='Delay between attempts in seconds (default: 0.5)')
    parser.add_argument('--rapid', action='store_true', help='Use rapid-fire mode')
    parser.add_argument('--attempts', type=int, default=50, help='Number of attempts in rapid mode (default: 50)')
    
    args = parser.parse_args()
    
    # Validate arguments
    if not args.wordlist and not args.rapid:
        print("Error: Must specify either --wordlist or --rapid")
        parser.print_help()
        sys.exit(1)
    
    # Create simulator
    simulator = RDPBruteForceSimulator(
        host=args.host,
        port=args.port,
        username=args.user
    )
    
    # Run attack
    if args.rapid:
        simulator.rapid_fire_attack(num_attempts=args.attempts)
    else:
        simulator.run_wordlist_attack(args.wordlist, delay_between_attempts=args.delay)


if __name__ == '__main__':
    main()
