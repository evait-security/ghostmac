# GhostMAC

**GhostMAC** is a powerful Python-based tool designed to perform DHCP brute force attacks by sending multiple DISCOVER packets with randomly generated MAC addresses. It enables network penetration testers to assess the resilience of DHCP servers, particularly those implementing MAC address filtering or Network Access Control (NAC).

GhostMAC generates random MAC addresses and sends DHCP DISCOVER packets to the network. It then waits for DHCP OFFER packets and prints the IP addresses offered by the DHCP server. This tool can be especially useful for testing network defenses, spoofing MAC addresses to bypass filtering, and checking how a DHCP server handles numerous unknown requests.

### Features:
- Generate random MAC addresses, with an optional prefix to target specific vendors.
- Send DHCP DISCOVER packets to receive DHCP OFFERs from a server.
- Capture and display DHCP OFFER packets to view the offered IP addresses.
- Command line options for easy customization (network interface, MAC prefix, timeout, number of packets, etc.).

### Disclaimer:
**Warning:** GhostMAC is intended for legal and authorized testing purposes only. Unauthorized use of this tool may result in criminal penalties. The authors are not responsible for any misuse or damage caused.

## Installation

Install using `pipx`:

```sh
pipx install git+https://github.com/evait-security/ghostmac.git
```

GhostMAC requires root privileges to send and receive raw packets. You can use the env command to pass your user's PATH variable to sudo, allowing the installed ghostmac executable to be found.

You may also need to install pipx if you don't have it already:
  
  ```sh
python3 -m pip install --user pipx
python3 -m pipx ensurepath
  ```

## Usage

GhostMAC provides flexibility to customize the DHCP brute force process with different options. You need root privileges to run the tool due to the requirement to access raw sockets for sending and receiving packets.

Here are some examples of how you can use GhostMAC:

```sh
# go with the defaults (interface=enp5s0, prefix="", counter=2000)
sudo env "PATH=$PATH" ghostmac

# run ghostmac with eth0 interface fully random mac addresses
sudo env "PATH=$PATH" ghostmac --interface eth0

# run ghostmac with eth0 interface random mac addresses with a specific vendor
sudo env "PATH=$PATH" ghostmac --interface eth0 --prefix "00:11:22"

# run ghostmac with eth0 interface and a custom counter of 10 which results in 10 packets that are sent
sudo env "PATH=$PATH" ghostmac --interface eth0 --counter 10
```

### Command Line Arguments:

- **`--prefix` / `-p`**:
  - Define a MAC address prefix (e.g., a vendor prefix like `00:11:22`). If omitted, GhostMAC generates fully random MAC addresses.
  - Example: `--prefix "00:11:22"`

- **`--interface` / `-i`**:
  - Specify the network interface to use for sending and receiving packets. Defaults to `enp5s0` if not provided.
  - Example: `--interface eth0`

- **`--timeout` / `-t`**:
  - Set the timeout period between sending batches of DHCP DISCOVER packets (in seconds). Defaults to `10`.
  - Example: `--timeout 5`

- **`--counter` / `-c`**:
  - Define how many DHCP DISCOVER packets to send before taking a break. Defaults to `2000`.
  - Example: `--counter 500`

## Example Use Cases
1. Testing Network Security:
- GhostMAC can be used to test the resilience of your DHCP server by generating numerous requests with random MAC addresses to see how it handles unknown devices. This can simulate a real-world attack scenario where an attacker attempts to exhaust the available DHCP leases.

2. Bypassing NAC Systems:
- Network Access Control (NAC) systems may rely on filtering based on known MAC addresses. GhostMAC can generate new random MAC addresses to determine whether unauthorized devices can bypass such filters and gain network access.

## Requirements
Python 3.6+.
Scapy library for packet crafting and sending. This will be installed automatically when using pipx or pip.

## Security Considerations
Since GhostMAC requires root privileges to send raw packets, it is recommended to run the tool on a dedicated testing system or virtual machine to avoid impacting a production environment. You may also use the setcap command to allow Python to send raw packets without requiring sudo, though this has security implications:

```sh
sudo setcap cap_net_raw+ep $(which python3)
```

## Contributing
If you'd like to contribute to GhostMAC, please feel free to fork the repository and submit a pull request. All contributions are welcome, whether it's improving documentation, adding new features, or fixing bugs.

## License
GhostMAC is licensed under the MIT License. See the LICENSE file for more details.

## Disclaimer
Use this tool responsibly and only on networks for which you have explicit permission to test. Unauthorized use is illegal and unethical.

## Special Thanks
@FrankSpierings (https://github.com/FrankSpierings) for the mac-bruteforce.py script (https://gist.github.com/FrankSpierings/a263b3097f87c3a2c3c9a7d121535253) as a base for this project
