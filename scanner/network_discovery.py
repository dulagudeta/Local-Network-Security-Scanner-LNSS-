from scapy.all import ARP, Ether, srp
import socket


def get_local_ip():
    """
    Returns the local machine IP address.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Doesn't need to be reachable
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


def get_subnet(ip):
    """
    Assumes /24 subnet (common for home & small networks)
    Example: 192.168.1.0/24
    """
    return ".".join(ip.split(".")[:-1]) + ".0/24"


def discover_devices():
    """
    Performs ARP scan on local network.
    Returns a list of discovered devices.
    """
    local_ip = get_local_ip()
    subnet = get_subnet(local_ip)

    arp_request = ARP(pdst=subnet)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = broadcast / arp_request

    result = srp(packet, timeout=2, verbose=False)[0]

    devices = []

    for sent, received in result:
        devices.append({
            "ip": received.psrc,
            "mac": received.hwsrc
        })

    return devices


if __name__ == "__main__":
    devices = discover_devices()
    for device in devices:
        print(f"IP: {device['ip']} | MAC: {device['mac']}")
