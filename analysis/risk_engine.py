# Risk rules
RISK_RULES = {
    21: {"level": "MEDIUM", "reason": "FTP detected (unencrypted file transfer)"},
    22: {"level": "LOW", "reason": "SSH detected (secure but should be protected)"},
    23: {"level": "HIGH", "reason": "Telnet detected (insecure remote access)"},
    80: {"level": "MEDIUM", "reason": "HTTP detected (unencrypted web service)"},
    443: {"level": "LOW", "reason": "HTTPS detected (encrypted web service)"},
    445: {"level": "HIGH", "reason": "SMB detected (file sharing can expose data)"},
    3389: {"level": "HIGH", "reason": "RDP detected (remote desktop exposed)"}
}