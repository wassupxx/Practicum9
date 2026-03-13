import os
os.makedirs('simple', exist_ok=True)
with open('input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    even_lines = []

    for index in range(len(lines)):
        if index % 2 == 1:
            even_lines.append(lines[index])
    with open('simple/output.txt', 'w', encoding='utf-8') as fe:
        fe.writelines(even_lines)
