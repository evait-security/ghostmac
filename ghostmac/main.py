import time
import random
import argparse
from scapy.all import *
import sys

# Funktion zur Generierung einer zufälligen MAC-Adresse
def generate_random_mac(prefix=''):
    """Generiert eine zufällige MAC-Adresse basierend auf dem gegebenen Präfix"""
    prefix = prefix.replace(':', '')
    if len(prefix) % 2 != 0:
        raise ValueError("Der Präfix muss eine gerade Anzahl von Zeichen haben")

    prefix_bytes = len(prefix) // 2
    remaining_bytes = 6 - prefix_bytes
    mac = [random.randint(0x00, 0xff) for _ in range(remaining_bytes)]
    mac_str = ':'.join(map(lambda x: '{:02x}'.format(x), mac))

    if prefix_bytes > 0:
        prefix_str = ':'.join([prefix[i:i+2] for i in range(0, len(prefix), 2)])
        return '{0}:{1}'.format(prefix_str, mac_str)
    else:
        return mac_str

def capture(packet):
    """Funktion zum Verarbeiten von Paketen"""
    print('Allowed: {0} = {1}'.format(str2mac(packet['BOOTP'].chaddr[:6]), packet['BOOTP'].yiaddr))

def main():
    # Argumente parsen
    parser = argparse.ArgumentParser(description='GhostMAC: A tool to brute force DHCP by sending DISCOVER packets with random MAC addresses')
    parser.add_argument('-p', '--prefix', type=str, default='', help='MAC Address Prefix (e.g., 44:55:66)')
    parser.add_argument('-i', '--interface', type=str, default='enp5s0', help='Network Interface to use (e.g., enp5s0)')
    parser.add_argument('-t', '--timeout', type=int, default=10, help='Timeout in seconds between runs')
    parser.add_argument('-c', '--counter', type=int, default=2000, help='Number of packets to send before a break')

    args = parser.parse_args()

    prefix = args.prefix
    iface = args.interface
    timeout = args.timeout
    breakcounter = args.counter

    # Starten des Sniffers
    sniffer = AsyncSniffer(iface=iface, filter='udp dst port 68', prn=capture)
    sniffer.start()

    reset = breakcounter
    try:
        while True:
            macaddress = generate_random_mac(prefix)
            p = Ether(src=macaddress, dst="ff:ff:ff:ff:ff:ff") / \
                IP(src="0.0.0.0", dst="255.255.255.255") / \
                UDP(sport=68, dport=67) / \
                BOOTP(chaddr=mac2str(macaddress)) / \
                DHCP(options=[("message-type", "discover"), ("hostname", 'scapy'), "end"])

            sys.stdout.write('Sending: {0}\r'.format(macaddress))
            sys.stdout.flush()
            sendp(p, iface=iface, verbose=0)

            if breakcounter:
                breakcounter -= 1
                if breakcounter < 1:
                    breakcounter = reset
                    break

        print()
        print('Sleeping: {0:d}s'.format(timeout))
        time.sleep(timeout)
        sniffer.stop()

    except KeyboardInterrupt:
        sniffer.stop()

    print('Shutdown...')

if __name__ == '__main__':
    main()
