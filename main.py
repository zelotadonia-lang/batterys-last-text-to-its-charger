"""The Battery's Last Text to Its Charger.

A dying phone battery sends one final text to its charger: it went out
at 98% and asks the charger to lie for it one last time. The program
writes that exact line, 65 bytes with no trailing newline, to
/output/entry.txt.
"""

import os

TEXT = "If the charger asks, I went out at 98%. Lie for me one last time."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(TEXT)
