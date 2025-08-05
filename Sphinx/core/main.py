import sys
import os

# Allow relative imports when running directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.scanner import scan_file
from utilities.banner import print_banner

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <file_to_scan>")
        sys.exit(1)

    file_path = sys.argv[1]

    print_banner()               # Print ASCII banner and tagline
    scan_file(file_path)        # Run the full malware scan

if __name__ == "__main__":
    main()