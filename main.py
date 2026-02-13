"""
Local Network Security Scanner (LNSS)
Main Orchestrator
"""

from scanner.network_discovery import discover_devices
from scanner.port_scanner import scan_ports
from analysis.risk_engine import calculate_risk
from colorama import Fore, Style, init
from tabulate import tabulate

init(autoreset=True)


def color_risk(level):
    if level == "HIGH":
        return Fore.RED + level + Style.RESET_ALL
    elif level == "MEDIUM":
        return Fore.YELLOW + level + Style.RESET_ALL
    else:
        return Fore.GREEN + level + Style.RESET_ALL


def main():
    print(Fore.CYAN + "\n🔐 Local Network Security Scanner (LNSS)")
    print(Fore.CYAN + "Scanning local network...\n")

    devices = discover_devices()

    if not devices:
        print(Fore.RED + "No devices found.")
        return

    table_data = []

    for device in devices:
        ip = device["ip"]
        mac = device["mac"]

        print(Fore.BLUE + f"\nScanning device: {ip}")

        ports = scan_ports(ip)

        if isinstance(ports, dict) and "error" in ports:
            print(Fore.RED + f"Error scanning {ip}: {ports['error']}")
            continue

        risk = calculate_risk(ports)

        table_data.append([
            ip,
            mac,
            len(ports),
            color_risk(risk["level"])
        ])

        print(Fore.WHITE + "Open Ports:")
        for p in ports:
            print(f"  - {p['port']} ({p['service']})")

        print(color_risk(risk["level"]) + f" | Score: {risk['score']}")
        print("Reasons:")
        for reason in risk["reasons"]:
            print(f"  - {reason}")

    print(Fore.CYAN + "\n📊 Scan Summary\n")

    headers = ["IP Address", "MAC Address", "Open Ports", "Risk Level"]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))


if __name__ == "__main__":
    main()
