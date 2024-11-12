# GhostMAC

GhostMAC is a tool to brute force DHCP by sending DISCOVER packets with random MAC addresses. This tool will generate a random MAC address and send a DHCP DISCOVER packet to the network. The tool will wait for a DHCP OFFER packet and print the corresponding IP address that was offered by the DHCP server. This tool can be used by pentesters to test the security of a network by trying to get an IP address from the DHCP server which uses MAC address filtering. This tequnique is also known as MAC address spoofing in order to bypass a NAC (Network Access Control) system.

## Installation

Install using pipx:

```sh
pipx install git+https://github.com/evait-security/ghostmac.git
```

## Usage

You can run GhostMAC with the following command but you need to have root privileges to be able to send and receive packets. With the env command you can pass the PATH variable to the sudo command so it can find the ghostmac executable you installed with pipx.

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
