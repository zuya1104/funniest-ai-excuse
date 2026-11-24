"""Writes the one-line excuse to /output/entry.txt."""

import os

ENTRY = "I did finish it — in the wrong repo, for Priya's launch, three days early — and she's already paid the invoice, so technically it's done, just not yours."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")

if __name__ == "__main__":
    main()
