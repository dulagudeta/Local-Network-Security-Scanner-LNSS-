import nmap

# Common ports associated with security risks
COMMON_PORTS = [
    21,   # FTP
    22,   # SSH
    23,   # Telnet
    80,   # HTTP
    443,  # HTTPS
    445,  # SMB
    3389  # RDP
]


def scan_ports(target_ip):
    """
    Scans common ports on a given IP address.
    Returns a list of open ports with service names.
    """
    nm = nmap.PortScanner()
    port_range = ",".join(str(port) for port in COMMON_PORTS)

    try:
        nm.scan(
            hosts=target_ip,
            arguments=f"-p {port_range} --open"
        )
    except Exception as e:
        return {"error": str(e)}

    open_ports = []

    if target_ip in nm.all_hosts():
        for proto in nm[target_ip].all_protocols():
            ports = nm[target_ip][proto].keys()
            for port in ports:
                service = nm[target_ip][proto][port]["name"]
                open_ports.append({
                    "port": port,
                    "service": service
                })

    return open_ports


if __name__ == "__main__":
    target = "192.168.1.1"
    results = scan_ports(target)

    if isinstance(results, dict) and "error" in results:
        print("Error:", results["error"])
    else:
        for item in results:
            print(f"Port {item['port']} open ({item['service']})")
