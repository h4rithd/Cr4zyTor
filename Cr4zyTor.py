import os
import time
import requests
import subprocess
import argparse
import textwrap

def get_current_ip():
    url = 'http://ifconfig.io'
    headers = {'User-Agent': 'curl/8.5.0'}
    get_ip = requests.get(url, headers=headers, proxies=dict(http='socks5://127.0.0.1:9050', https='socks5://127.0.0.1:9050'))
    return get_ip.text

def change_ip():
    subprocess.run(["service", "tor", "reload"])
    print(f"\033[1;93m[!] Your new IP: {get_current_ip()}".rstrip())

def main(args):
    if os.geteuid() != 0:
        print("\033[1;91m[!] This program requires root privileges. Please run with 'sudo'.\033[0m")
        exit(1)
    
    subprocess.run(["service", "tor", "start"])
    time.sleep(3)
    print("\033[1;94m[-] Please change your SOCKS proxy to 127.0.0.1:9050\033[0m")
    subprocess.run(["service", "tor", "start"])
    
    try:
        interval = int(args.seconds) if args.seconds else 10
        
        while True:
            time.sleep(interval)
            change_ip()
    except KeyboardInterrupt:
        print('\033[1;91m[!] Goodbye! Cr4zyTor is closed.\033[0m')
        quit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='Cr4zyTor',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
-----------------------------------------------------------	
-------[ Cr4zyTor - Change IP address automatically ]------
-----------------------------------------------------------	
	   ______     __ __            ______          
	  / ____/____/ // /____  __  _/_  __/___  _____
	 / /   / ___/ // //_  / / / / // / / __ \/ ___/
	/ /___/ /  /__  __// /_/ /_/ // / / /_/ / /    
	\____/_/     /_/  /___/\__, //_/  \____/_/     
	                      /____/                   
Welcome to Cr4zyTor created by h4rithd.com!

Usage:
    sudo python Cr4zyTor.py [-s SECONDS] [-i ITERATIONS]

Options:
    -s, --seconds      Time interval to change IP in seconds (default 10)
        '''))
    parser.add_argument("-s", "--seconds", type=int, help="Time interval to change IP in seconds (default 10)")
    args = parser.parse_args()
    main(args)

