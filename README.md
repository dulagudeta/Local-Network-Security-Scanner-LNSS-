
# 🔐 Local Network Security Scanner (LNSS)

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green)

A defensive cybersecurity tool that scans a local network to identify connected devices, exposed services, and potential security risks.

> Designed for educational use, ethical network auditing, and security awareness.

---

## 📌 Overview

Local Network Security Scanner (LNSS) helps users understand what is happening inside their local network by answering questions like:

- Which devices are connected to my network?
- What services and ports are exposed?
- Are there insecure or risky configurations?
- Which devices require attention?

The tool performs **non-intrusive security analysis** and does **not exploit vulnerabilities**.

---

## 🎯 Features

### 🔎 Network Discovery
- Detects active devices on the local subnet
- Displays:
  - IP Address
  - MAC Address

### 🚪 Controlled Port Scanning

Scans commonly abused ports only:

| Port | Service |
|------|----------|
| 21 | FTP |
| 22 | SSH |
| 23 | Telnet |
| 80 | HTTP |
| 443 | HTTPS |
| 445 | SMB |
| 3389 | RDP |

---

### ⚠️ Risk Analysis Engine

Each device is analyzed using predefined security rules.

Risk Levels:
- 🟢 **LOW**
- 🟡 **MEDIUM**
- 🔴 **HIGH**

The scanner provides clear explanations for each detected risk.

---

### 📊 Professional CLI Output
- Colored risk levels
- Clean formatted summary table
- Structured security reasoning

---

# 🛠️ Requirements

## 🐍 Python Version (Important)

Recommended:

```

Python 3.11

````

⚠️ Python 3.13 may cause compatibility issues with networking libraries like Scapy.

---

## 📦 Python Dependencies

Install using:

```bash
pip install -r requirements.txt
````

### requirements.txt

```
scapy
python-nmap
colorama
tabulate
fpdf2
```

---

# 🖥️ System Dependencies (Windows Users)

## 1️⃣ Nmap (Required)

Download:

[https://nmap.org/download.html](https://nmap.org/download.html)

During installation:

* Ensure **"Add Nmap to PATH"** is enabled

Verify installation:

```bash
nmap --version
```

---

## 2️⃣ Npcap (Required for ARP Scanning)

Download:

[https://npcap.com/](https://npcap.com/)

During installation:

* ✔ Install in **WinPcap API-compatible Mode**
* ✔ Default settings are fine

Restart your computer after installation.

---

# 🔐 Administrator Privileges

On Windows:

* Run VS Code or Terminal **as Administrator**
* ARP scanning requires elevated permissions

---

# 🚀 Installation

```bash
git clone https://github.com/yourusername/lnss.git
cd lnss

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```

Run the scanner:

```bash
python main.py
```

---

# 🧠 Project Structure

```
lnss/
│
├── scanner/
│   ├── network_discovery.py
│   ├── port_scanner.py
│
├── analysis/
│   ├── risk_engine.py
│
├── main.py
└── README.md
```

---

# ⚠️ Ethical Use Disclaimer

This tool:

* Scans only local networks
* Performs no exploitation
* Is intended for defensive and educational use

⚠️ Only scan networks you own or have explicit permission to test.

Unauthorized scanning may violate laws or policies.

---

# 🧯 Troubleshooting

## ❗ Error: "No libpcap provider available"

Install Npcap and restart your system.

---

## ❗ Error: "winpcap is not installed"

Install Npcap in WinPcap compatibility mode.

---

## ❗ Error: "No module named X"

Run:

```bash
pip install -r requirements.txt
```

Ensure you are using the correct Python interpreter.

---

# 📈 Future Enhancements

* MAC address vendor detection
* Scan history comparison
* Alert on new devices
* GUI dashboard
* PDF report export
* Cloud-based agent version

---

# 👨‍💻 Author

DULA GUDETA
Software Engineering Student
Cybersecurity Enthusiast

Portfolio: [https://dulagudeta.netlify.app/](https://dulagudeta.netlify.app/)

---

⭐ If you found this project useful, consider starring the repository.

```
