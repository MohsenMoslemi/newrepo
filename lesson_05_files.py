from pathlib import Path

Path("notes.txt").write_text("helloدتتنsr5566ffpace\n")

try:
    print(Path("notes.txt").read_text())
    print(Path("missing.txt").read_text())
except FileNotFoundError as e:
    print("oops:", e)
