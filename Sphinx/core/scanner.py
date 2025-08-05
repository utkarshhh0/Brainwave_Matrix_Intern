import os
from core.logic import (
    calculate_entropy,
    detect_base64,
    detect_hex,
    suspicious_keywords,
    disassemble_code,
    analyze_ast,
    match_yara_rules,
    check_against_cisa,
    check_pwned_passwords
)

def scan_file(file_path):
    if not os.path.exists(file_path):
        print("[ERROR] File not found.")
        return

    print(f"\n[+] File received: {file_path}")
    print("[+] Starting analysis...")

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        data = f.read()

    # Initialize results
    threat_score = 0
    details = []

    if calculate_entropy(data) > 4.5:
        threat_score += 1
        details.append("High entropy detected")

    if detect_base64(data):
        threat_score += 1
        details.append("Base64 pattern detected")

    if detect_hex(data):
        threat_score += 1
        details.append("Hex pattern detected")

    if suspicious_keywords(data):
        threat_score += 1
        details.append("Suspicious keywords found")

    if disassemble_code(data):
        threat_score += 1
        details.append("Suspicious opcodes in disassembly")

    if analyze_ast(data):
        threat_score += 1
        details.append("Suspicious functions detected in AST")

    if match_yara_rules(file_path):
        threat_score += 2
        details.append("Matched YARA rules")

    if check_against_cisa(data):
        threat_score += 2
        details.append("CISA KEV matched CVEs")

    if check_pwned_passwords(data):
        threat_score += 1
        details.append("Password found in data breaches")

    print("\n\033[96m[+] Suspicious Behavior Report:\033[0m")
    if details:
        for item in details:
            print(f"  - {item}")
    else:
        print("  - None")

    # Print colored threat score
    print("\n\033[96m[+] Threat Score:\033[0m", threat_score)  # Bright purple

    # Final verdict with color
    if threat_score >= 5:
        print("\n\033[91m[VERDICT] MALICIOUS FILE\033[0m")  # Bright blood red
    elif threat_score >= 2:
        print("\n\033[93m[VERDICT] SUSPICIOUS FILE\033[0m")  # Bright yellow
    else:
        print("\n\033[92m[VERDICT] SAFE FILE\033[0m")  # Bright green