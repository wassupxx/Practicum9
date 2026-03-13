with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.read()
upper_lines = lines.upper()
with open("output.txt", "w", encoding="utf-8") as fi:
    fi.write(upper_lines)