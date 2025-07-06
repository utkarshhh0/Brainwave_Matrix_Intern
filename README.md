# 🕷️ BaitScan – Terminal Phishing Link Scanner

**BaitScan** is a Python-based phishing detection tool built with an old-school cyberpunk vibe. It evaluates URLs using smart local heuristics and gives instant visual feedback through animated, color-coded terminal bars — no cloud dependency required.

> 🧠 Developed for the Cyber Security Internship at **Brainwave Matrix Solutions**  
> ⚡ Fast, lightweight, and tuned to catch suspicious links in real time

---

## 🚀 Features

- ✅ **Risk Scoring Engine** (0–100)
- ✅ **Color-Coded Terminal Bars**  
  Green → Safe | Yellow → Suspicious | Red → Likely Phishing
- ✅ **Offline-First Heuristics**  
  - Suspicious TLD detection (`.xyz`, `.top`, etc.)  
  - Phishing keyword matching in URL and domain  
  - Hyphen overload flag (`secure-instagram-login`)  
  - Obfuscated characters (`%2F`, `%20`, etc.)  
  - Brand spoofing checks (e.g. `googlepay-login.com`)
- ✅ **Looped CLI** – scan one URL or many in a single run
- ✅ **No paid APIs required** (optional VirusTotal integration in progress)

---

## 🎓 Internship Context

> Built during the **Cyber Security Internship** at  
> **Brainwave Matrix Solutions** 🧠  
> Project folder and GitHub repo name follow official guidelines:  
> `Brainwave_Matrix_Intern`

---

## 📦 Quick Setup

```bash
git clone https://github.com/utkarshhh0/Brainwave_Matrix_Intern
cd Brainwave_Matrix_Intern/Brainwave_Matrix_Intern
pip install -r requirements.txt
python main.py
