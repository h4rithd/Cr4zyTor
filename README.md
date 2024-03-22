# cresyTor

cresyTor is a Python script that facilitates IP address rotation using Tor. It periodically changes the IP address by reloading the Tor service. This can be useful for various purposes such as web scraping, anonymity, or bypassing IP-based restrictions.

## Features

- Periodically changes IP address using Tor
- Easy setup and usage
- Customizable time interval for IP changes
- Runs indefinitely until manually stopped

## Requirements

- Python 3.x
- Tor

## Installation

1. Make sure you have Python 3.x installed on your system.
2. Install Tor if you haven't already. You can usually install it using your package manager (e.g., `apt-get install tor` on Debian-based systems).
3. Clone this repository or download the `cresyTor.py` script.

## Usage

1. Open a terminal window.
2. Navigate to the directory where `cresyTor.py` is located.
3. Run the script using the following command:

```bash
sudo python cresyTor.py
```

> Note: This program requires root privileges to run, so please make sure to use sudo.

The script will continuously change the IP address using Tor every 60 seconds by default. You can modify this time interval directly in the script if needed.

# Disclaimer
This script is provided for educational and informational purposes only. Usage of this script for any illegal activities is strictly prohibited. The author assumes no liability and is not responsible for any misuse of this script.
