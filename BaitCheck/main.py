from scanner.core import scan_url
from visual.bar import render_bar
from colorama import Fore, Style, init

init(autoreset=True)

BANNER = Fore.LIGHTRED_EX + r"""                                                                                                                                                         

888888b.            d8b 888     .d8888b.  888                        888      
888  "88b           Y8P 888    d88P  Y88b 888                        888      
888  .88P               888    888    888 888                        888      
8888888K.   8888b.  888 888888 888        88888b.   .d88b.   .d8888b 888  888 
888  "Y88b     "88b 888 888    888        888 "88b d8P  Y8b d88P"    888 .88P 
888    888 .d888888 888 888    888    888 888  888 88888888 888      888888K  
888   d88P 888  888 888 Y88b.  Y88b  d88P 888  888 Y8b.     Y88b.    888 "88b 
8888888P"  "Y888888 888  "Y888  "Y8888P"  888  888  "Y8888   "Y8888P 888  888                                                                                                                                                                                                                                                                                                                                                                                                                                                      
""" + Style.RESET_ALL


def run_once() -> None:
    """Run a single URL scan."""
    url = input("\nEnter a URL to scan: ").strip()
    score, reasons = scan_url(url)

    print("\nRisk Score:\n")
    print(render_bar(score))

    print("\nReasoning:")
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
        again = input("\nScan another? (Y/N): ").strip().lower()
        if again != "y":
            print("\nExiting BaitScan. Stay safe out there!\n")
            break


if __name__ == "__main__":
    main()