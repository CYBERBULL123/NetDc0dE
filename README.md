# Netktool - Network Information Extractor 🌐
## By :- NetDc0dE 

![Netktool Logo](https://link-to-your-logo-image.png)

## Overview

Netktool is a robust Python tool crafted for extracting comprehensive information about networks of class A, B, and C. Utilizing CIDR notation, it provides detailed insights, including CIDR notation, subnetwork details, net mask, network ID, broadcast IP, usable IP addresses, IP range, VLSM (Variable Length Subnet Masking), FLSM (Fixed Length Subnet Masking), available networks, and more. 🛠️ Generate reports in CSV format for easy analysis.

## Features

- Extracts information for networks of class A, B, and C using CIDR notation.
- Displays details such as CIDR notation, subnetwork information, net mask, network ID, broadcast IP, usable IP addresses, IP range, VLSM, FLSM, and available networks.
- Generates detailed reports in CSV format for seamless analysis.

## Requirements
- Python 3.9
- pip

## Compatible
- Windows
- Linux
- Termux


## Installation For Linux Kernals 

To use Netktool, ensure you have Python and pip installed. It is compatible with both Linux and Termux. 
# 1 •  Update Packages 
## For Linux
```bash
apt update && apt upgrade -y
```
## For Termux 
```bash
Pkg update && pkg upgrade -y
```
# 2 • Download Python and pip 
```bash
apt install python3 && apt install pip -y
pkg install python3 && apt install pip -y
```

# 3 • Download packages of pip
```bash
pip install -r requirements.txt
pkg install -r requirements.txt
```
# 4 • Give permission
```bash
chmod +rwx *
```
## Usage

```bash
netktool.py -n 192.168.128.220/12 -ni -s 12 45 67 21 -st VLSM/FLSM -a -o
```

- `-n`: Specify the network in CIDR notation.
- `-ni`: Retrieve network information.
- `-s`: Provide subnetwork hosting numbers in the given network.
- `-st`: Choose subnetting technique (VLSM/FLSM).
- `-a`: Display available networks.
- `-o`: Generate output in CSV format.

## Example

```bash
netktool.py -n 10.0.0.1/13 -ni -s 12 45 67 21 -st VLSM -a -o
```

## Contributing

Feel free to contribute to Netktool by opening issues or submitting pull requests. Your contributions are highly valued. 🙌

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

Special thanks to contributors and users who help improve Netktool.

For detailed information and usage examples, visit the [Netktool GitHub repository](https://github.com/CYBERBULL123/NetDc0dE).

---

**Happy Networking with Netktool! 🚀**
