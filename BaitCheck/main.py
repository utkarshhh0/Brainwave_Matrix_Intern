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
    """Run a single URL scan."""
    url = input("\n🔗  Enter a URL to scan: ").strip()
    score, reasons = scan_url(url)

    print("\nRisk Score:\n")
    print(render_bar(score))

    print("\n📝  Reasoning:")
    for reason in reasons:
        print(f"  • {reason}")

    verdict = (
        "SAFE ✅" if score <= 30
        else "SUSPICIOUS ⚠️" if score <= 70
        else "PHISHING LIKELY ❌"
    )
    print(f"\nVerdict: {verdict}")


def main():
    print(BANNER)
    while True:
        run_once()
        again = input("\n🔄  Scan another? (Y/N): ").strip().lower()
        if again != "y":
            print("\n👋  Exiting BaitScan. Stay safe out there!\n")
            break


if __name__ == "__main__":
    main()