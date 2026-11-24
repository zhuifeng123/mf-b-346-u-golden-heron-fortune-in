import os

os.makedirs("/output", exist_ok=True)

fortune = "Your plant stretches toward the sun, dreaming of a wider windowsill."
with open("/output/entry.txt", "w") as f:
    f.write(fortune)