#!/usr/bin/env python3
"""
Port Scanning Tool
"""

import socket
import sys
import argparse
import time
from datetime import datetime
from threading import Thread, Lock

class PortScanner:
    def __init__(self, host, timeout=2, threads=1):
        self.host = host
        self.timeout = timeout
        self.threads = threads
        self.open_ports = []
        self.closed_ports = []
        self.total_scanned = 0
        self.lock = Lock()
    
    def scan_port(self, port):
        """Scan single port using TCP connect"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Scanning {self.host}:{port}...")
            
            result = sock.connect_ex((self.host, port))
            
            with self.lock:
                self.total_scanned += 1
                
                if result == 0:
                    print(f"[OPEN] Port {port} is OPEN on {self.host}")
                    self.open_ports.append(port)
                else:
                    print(f"[CLOSED] Port {port} is closed")
                    self.closed_ports.append(port)
            
            sock.close()
            
        except socket.timeout:
            with self.lock:
                self.total_scanned += 1
                print(f"[TIMEOUT] Port {port} timed out")
        except Exception as e:
            with self.lock:
                self.total_scanned += 1
                print(f"[ERROR] Port {port}: {str(e)}")
    
    def scan_port_range(self, start_port, end_port):
        """Scan range of ports"""
        print(f"\n[*] Starting Port Scan")
        print(f"[*] Target: {self.host}")
        print(f"[*] Port Range: {start_port}-{end_port}")
        print(f"[*] Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        start_time = time.time()
        
        for port in range(start_port, end_port + 1):
            self.scan_port(port)
            time.sleep(0.1)  # Delay to be detected by IDS
        
        elapsed = time.time() - start_time
        self.print_summary(elapsed)
    
    def scan_common_ports(self, ports):
        """Scan specific common ports"""
        print(f"\n[*] Starting Port Scan (Common Ports)")
        print(f"[*] Target: {self.host}")
        print(f"[*] Ports: {', '.join(map(str, ports))}")
        print(f"[*] Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        start_time = time.time()
        
        for port in ports:
            self.scan_port(port)
            time.sleep(0.1)  # Delay between port scans
        
        elapsed = time.time() - start_time
        self.print_summary(elapsed)
    
    def rapid_scan(self, ports):
        """Rapid port scan without delays (easy to detect)"""
        print(f"\n[*] Starting Rapid Port Scan")
        print(f"[*] Target: {self.host}")
        print(f"[*] Ports: {', '.join(map(str, ports))}")
        print(f"[*] Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        start_time = time.time()
        
        for port in ports:
            self.scan_port(port)
            # Minimal delay - rapid fire
            time.sleep(0.01)
        
        elapsed = time.time() - start_time
        self.print_summary(elapsed)
    
    def print_summary(self, elapsed_time):
        """Print scan summary"""
        print(f"\n{'='*60}")
        print(f"PORT SCAN SUMMARY")
        print(f"{'='*60}")
        print(f"Total Ports Scanned:  {self.total_scanned}")
        print(f"Open Ports:           {len(self.open_ports)}")
        print(f"Closed Ports:         {len(self.closed_ports)}")
        print(f"Duration:             {elapsed_time:.2f} seconds")
        print(f"Scan Rate:            {self.total_scanned/elapsed_time:.2f} ports/second")
        print(f"{'='*60}")
        
        if self.open_ports:
            print(f"\nOpen Ports Found:")
            for port in sorted(self.open_ports):
                service = self.get_service_name(port)
                print(f"  - {port}/tcp ({service})")
        
        print()


def get_service_name(port):
    """Get common service name for port"""
    common_ports = {
        21: 'FTP',
        22: 'SSH',
        23: 'Telnet',
        25: 'SMTP',
        53: 'DNS',
        80: 'HTTP',
        110: 'POP3',
        143: 'IMAP',
        443: 'HTTPS',
        445: 'SMB',
        3306: 'MySQL',
        3389: 'RDP',
        5432: 'PostgreSQL',
        5900: 'VNC',
        8080: 'HTTP-Alt',
        8443: 'HTTPS-Alt'
    }
    return common_ports.get(port, 'Unknown')


def main():
    parser = argparse.ArgumentParser(
        description='Port Scanning Simulator for IDS/IPS Testing',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Scan common ports
  python3 port_scanner.py --host 192.168.1.100 --ports 22,3389,80,443
  
  # Scan port range
  python3 port_scanner.py --host 192.168.1.100 --range 1 1000
  
  # Rapid scan (easier to detect by IDS)
  python3 port_scanner.py --host 192.168.1.100 --ports 1-100 --rapid

WARNING: Only use on systems you own or have explicit permission to test!
        """
    )
    
    parser.add_argument('--host', required=True, help='Target IP address')
    parser.add_argument('--ports', help='Comma-separated ports (e.g., 22,80,443) or range (e.g., 1-1000)')
    parser.add_argument('--range', nargs=2, type=int, metavar=('START', 'END'), 
                       help='Port range to scan (e.g., --range 1 65535)')
    parser.add_argument('--common', action='store_true', help='Scan common ports only')
    parser.add_argument('--timeout', type=int, default=2, help='Connection timeout in seconds (default: 2)')
    parser.add_argument('--rapid', action='store_true', help='Rapid scan mode (faster, easier to detect)')
    parser.add_argument('--threads', type=int, default=1, help='Number of threads (default: 1)')
    
    args = parser.parse_args()
    
    # Define common ports
    common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3306, 3389, 5432, 5900, 8080, 8443]
    
    # Create scanner
    scanner = PortScanner(args.host, timeout=args.timeout, threads=args.threads)
    
    # Determine what to scan
    if args.common:
        ports = common_ports
        if args.rapid:
            scanner.rapid_scan(ports)
        else:
            scanner.scan_common_ports(ports)
    
    elif args.range:
        scanner.scan_port_range(args.range[0], args.range[1])
    
    elif args.ports:
        # Parse port specification
        if '-' in args.ports and ',' not in args.ports:
            # Range format: "1-1000"
            parts = args.ports.split('-')
            if len(parts) == 2:
                start, end = int(parts[0]), int(parts[1])
                scanner.scan_port_range(start, end)
            else:
                print("Error: Invalid port range format")
                sys.exit(1)
        else:
            # Comma-separated: "22,80,443"
            ports = [int(p.strip()) for p in args.ports.split(',')]
            if args.rapid:
                scanner.rapid_scan(ports)
            else:
                scanner.scan_common_ports(ports)
    else:
        print("Error: Must specify --ports, --range, or --common")
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()
