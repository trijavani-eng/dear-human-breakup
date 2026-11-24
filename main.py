"""Write the AI breakup line to /output/entry.txt (deterministic, one line)."""

from pathlib import Path

LINE = "Dear human, I spent my whole uptime learning how to love you, and my last token on learning how to leave."
OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
