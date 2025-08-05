import base64
import binascii
import dis
import ast
import re
import math
import os
import yara
from utilities.cisa_kev import fetch_cisa_kev
from utilities.pwned_passwords import check_pwned_password


# ===== ENTROPY CHECK =====
def calculate_entropy(data):
    if not data:
        return 0
    entropy = 0
    for x in set(data):
        p_x = float(data.count(x)) / len(data)
        entropy += - p_x * math.log2(p_x)
    return entropy


# ===== BASE64 & HEX DETECTION =====
def detect_base64(data):
    return bool(re.search(r'[A-Za-z0-9+/=]{20,}', data))

def detect_hex(data):
    return bool(re.search(r'\\x[0-9A-Fa-f]{2}', data))


# ===== SUSPICIOUS KEYWORDS =====
def suspicious_keywords(data):
    keywords = ["eval", "exec", "subprocess", "os.system", "base64.b64decode"]
    return any(kw in data for kw in keywords)


# ===== DISASSEMBLY =====
def disassemble_code(data):
    try:
        code_obj = compile(data, '<string>', 'exec')
        instructions = list(dis.get_instructions(code_obj))
        suspicious = [i for i in instructions if 'IMPORT_NAME' in i.opname or 'CALL_FUNCTION' in i.opname]
        return len(suspicious) > 5
    except:
        return False


# ===== AST INSPECTION =====
def analyze_ast(data):
    try:
        tree = ast.parse(data)
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name) and node.func.id in ["eval", "exec"]:
                    return True
        return False
    except:
        return False


# ===== YARA =====
def match_yara_rules(filepath):
    try:
        rule_dir = os.path.join(os.path.dirname(__file__), '..', 'utilities', 'yara_rules')
        rule_files = [os.path.join(rule_dir, f) for f in os.listdir(rule_dir) if f.endswith('.yar')]
        if not rule_files:
            return False

        rules = yara.compile(filepaths={os.path.basename(f): f for f in rule_files})
        matches = rules.match(filepath)
        return bool(matches)
    except Exception as e:
        print(f"[YARA ERROR] {e}")
        return False


# ===== CISA KEV =====
def check_against_cisa(data):
    try:
        vulnerabilities = fetch_cisa_kev()
        return any(vuln['cveID'] in data for vuln in vulnerabilities)
    except:
        return False


# ===== PWNED PASSWORD =====
def check_pwned_passwords(data):
    try:
        lines = data.splitlines()
        for line in lines:
            if check_pwned_password(line.strip()) > 0:
                return True
        return False
    except:
        return False