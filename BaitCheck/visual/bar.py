from colorama import Fore, Style, init
init(autoreset=True)

BAR_CHAR = "‖"

GREEN  = Fore.GREEN + Style.BRIGHT
YELLOW = Fore.YELLOW + Style.BRIGHT
RED    = Fore.RED + Style.BRIGHT

def render_bar(score: int, width: int = 60) -> str:
    score = max(0, min(score, 100))
    bars = int(width * score / 100)

    if score <= 30:
        color = GREEN
    elif score <= 70:
        color = YELLOW
    else:
        color = RED

    bar = "".join(f"{color}{BAR_CHAR}" for _ in range(bars))
    return f"{bar}{color}{score}%{Style.RESET_ALL}"