# scanner/core.py  –  quick‑boost heuristics edition
from typing import Tuple
import re
from urllib.parse import urlparse

# ---------- CONFIG --------------------------------------------------------
PHISH_KEYWORDS  = ["login", "verify", "secure", "account", "bank",
                   "update", "confirm", "password", "signin"]

SUSPICIOUS_TLDS = [".xyz", ".top", ".info", ".click", ".support",
                   ".live", ".site", ".online", ".store"]

SHORTENERS      = ["bit.ly", "tinyurl.com", "t.co", "goo.gl", "is.gd", "buff.ly"]

BRAND_TARGETS   = ["paypal", "google", "amazon", "facebook", "apple", "microsoft"]

# ---------- MAIN SCAN FUNCTION -------------------------------------------
def scan_url(url: str) -> Tuple[int, list]:
    """
    Analyse a URL and return (risk_score 0‑100, reasons list)
    """
    score   = 0
    reasons = []

    # Ensure scheme is present for urlparse
    if "://" not in url:
        url = "http://" + url

    parsed  = urlparse(url)
    scheme  = parsed.scheme.lower()
    domain  = parsed.netloc.lower()
    full    = (parsed.netloc + parsed.path).lower()

    # 1. HTTP (not HTTPS)
    if scheme != "https":
        score += 20
        reasons.append("Uses HTTP (not secure)")

    # 2. Raw IPv4 address
    if re.fullmatch(r"\d{1,3}(?:\.\d{1,3}){3}", domain):
        score += 25
        reasons.append("URL uses raw IP address")

    # 3. URL shortener
    if any(short in domain for short in SHORTENERS):
        score += 25
        reasons.append("URL shortener detected")

    # 4. Phishing keywords anywhere in URL
    hits = sum(1 for kw in PHISH_KEYWORDS if kw in full)
    if hits:
        score += 10 * hits
        reasons.append(f"{hits} phishing keyword(s) found")

    # 5. Extra weight: keywords in the **domain** itself
    domain_hits = sum(1 for kw in PHISH_KEYWORDS if kw in domain)
    if domain_hits:
        score += 10 * domain_hits
        reasons.append(f"{domain_hits} keyword(s) in domain")

    # 6. Suspicious TLD (weight bumped to +30)
    if any(domain.endswith(tld) for tld in SUSPICIOUS_TLDS):
        score += 30
        reasons.append("Suspicious top‑level domain")

    # 7. Too many subdomains (dots ≥ 2 before TLD)
    if domain.count(".") >= 2:
        score += 10
        reasons.append("Multiple subdomains")

    # 8. Hyphen‑heavy domain
    hyphens = domain.count("-")
    if hyphens >= 2:
        score += 15
        reasons.append("Multiple hyphens in domain")

    # 9. Obfuscated characters in path (%xx)
    if "%" in parsed.path:
        score += 10
        reasons.append("Obfuscated characters in URL path")

    # 10. Brand‑spoof check (simple substring match)
    for brand in BRAND_TARGETS:
        if brand in domain and not domain.startswith(brand):
            score += 20
            reasons.append(f"Potential brand spoofing: {brand}")
            break

    # 11. Excessive length
    if len(full) > 60:
        score += 10
        reasons.append("URL is unusually long")

    # Clamp 0‑100
    final_score = min(score, 100)
    return final_score, reasons