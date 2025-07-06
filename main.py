# main.py  –  interactive launcher
from scanner.core import scan_url
from visual.bar import render_bar
from colorama import Fore, Style, init

init(autoreset=True)

BANNER = Fore.CYAN + r"""
  ____        _ _      _____ _               _    
 |  _ \      (_) |    / ____| |             | |   
 | |_) | __ _ _| |_  | |    | |__   ___  ___| | __
 |  _ < / _` | | __| | |    | '_ \ / _ \/ __| |/ /
 | |_) | (_| | | |_  | |____| | | |  __/ (__|   < 
 |____/ \__,_|_|\__|  \_____|_| |_|\___|\___|_|\_\
                                                  
""" + Style.RESET_ALL


def run_once() -> None:
    """Single scan cycle."""
    url = input("\n🔗  Enter a URL to scan: ").strip()
    score, reasons = scan_url(url)

    print("\nRisk Score:\n")
    print(render_bar(score))

    print("\n📝  Reasoning:")
    for reason in reasons:
        print(f"  • {reason}")

    if score <= 30:
        verdict = "SAFE ✅"
    elif score <= 70:
        verdict = "SUSPICIOUS ⚠️"
    else:
        verdict = "PHISHING LIKELY ❌"

    print(f"\nVerdict: {verdict}")


def main():
    print(BANNER)
    while True:
        run_once()
        again = input("\n🔄  Scan another? (Y/N): ").strip().lower()
        if again != "Y":
            print("\n👋  Exiting BaitScan. Stay safe out there!")
            break


if __name__ == "__main__":
    main()