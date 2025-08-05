# Sphinx⚖️
## Zero Trust File Malware Detector.

**Sphinx** is a serious and minimal malware analysis CLI tool.  
It performs static analysis on suspicious files using local heuristics, known vulnerability intelligence, and pattern recognition techniques.

---

## 🔥 Features

- **Local Static Heuristics**
  - Entropy check
  - Suspicious keyword scan
  - Hex/Base64 pattern detection
  - AST analysis for Python functions
  - Opcode-level analysis
  - YARA rules matching

- **Integrated Threat Intelligence**
  - CISA KEV catalog (vulnerability awareness)
  - HaveIBeenPwned breached password scan
  - YARA rule signatures

- **Threat Scoring Engine**
  - Calculates a cumulative threat score based on multiple signals

- **Command-Line Simplicity**
  - Just run `python main.py <file_path>` and get instant analysis with verdict

- **Cinematic CLI Output**
  - ASCII art banner  
  - Status updates  
  - Highlighted verdicts:
    - 🟢 SAFE
    - 🟡 SUSPICIOUS
    - 🔴 MALICIOUS

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/utkarshhh0/Brainwave_Matrix_Intern
cd Sphinx
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run a Scan

```bash
python main.py samples/clean.txt
```

---

## 📁 Project Structure

```
Sphinx/
├── .gitignore
├── README.md
├── requirements.txt
├── core/
│   ├── main.py
│   ├── scanner.py
│   └── logic.py
├── samples/
│   └── clean.txt
├── utilities/
│   ├── banner.py
│   ├── banner.txt
│   ├── colors.py
│   ├── cisa_kev.py
│   ├── pwned_passwords.py
│   └── yara_rules/

```

---

## 🧠 Intelligence Sources

- [HaveIBeenPwned](https://haveibeenpwned.com/)
- [CISA KEV Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- [MITRE ATT&CK Framework](https://attack.mitre.org/)
- [YARA](https://virustotal.github.io/yara/)

---

## 📌 TODO (Future Versions)

- Network behavior analysis
- ML model integration
- Web-based dashboard interface
- Auto unpacking of archives
- Real-time scanning mode

---

## 🤝 Contributing

Pull requests are welcome. For major changes, open an issue first to discuss what you’d like to change.

---

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---