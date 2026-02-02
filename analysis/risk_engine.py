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

def calculate_risk(open_ports):
    

    reasons = []
    score = 0

    for port_info in open_ports:
        port = port_info["port"]

        if port in RISK_RULES:
            rule = RISK_RULES[port]
            reasons.append(f"Port {port}: {rule['reason']}")

            if rule["level"] == "LOW":
                score += 1
            elif rule["level"] == "MEDIUM":
                score += 3
            elif rule["level"] == "HIGH":
                score += 6
    # Additional heuristic: many open ports
    if len(open_ports) >= 5:
        reasons.append("Many open ports detected (possible attack surface)")
        score += 3

    # Final risk level classification
    if score == 0:
        level = "LOW"
    elif score <= 5:
        level = "MEDIUM"
    else:
        level = "HIGH"

    return {
        "score": score,
        "level": level,
        "reasons": reasons
    }
# Test module
if __name__ == "__main__":
    sample_ports = [
        {"port": 23, "service": "telnet"},
        {"port": 80, "service": "http"},
        {"port": 445, "service": "microsoft-ds"}
    ]

    result = calculate_risk(sample_ports)
    print("Risk Level:", result["level"])
    print("Score:", result["score"])
    for r in result["reasons"]:
        print("-", r)