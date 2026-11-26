import os

TEXT = "If the charger asks, I went out at 98%. Lie for me one last time."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(TEXT)
