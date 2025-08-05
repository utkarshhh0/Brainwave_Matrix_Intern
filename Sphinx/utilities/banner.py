import os
from utilities.colors import Colors

def print_banner():
    try:
        banner_path = os.path.join(os.path.dirname(__file__), "banner.txt")
        with open(banner_path, "r", encoding="utf-8") as file:
            banner = file.read()
            print(f"{Colors.RED}{banner}{Colors.RESET}")
            print(f"{Colors.BOLD}\nZero Trust File Malware Detector{Colors.RESET}\n")
    except FileNotFoundError:
        print("Banner file not found.")
