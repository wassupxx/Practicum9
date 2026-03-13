from datetime import datetime

with open("input.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()
    N = int(lines[1].strip())
    year = datetime.today().year
    currentdate = lines[0].strip()
    full_currentdate = f"{currentdate}.{year}"
    current_date = datetime.strptime(full_currentdate, "%d.%m.%Y")
    result = []

    for index in range(2, 2 + N):
        line = lines[index].strip()
        cell, celldate = line.split()
        full_celldate = f"{celldate}.{year}"
        cell_date = datetime.strptime(full_celldate, "%d.%m.%Y")
        difference = current_date - cell_date
        if difference.days > 3:
            result.append(cell)

with open("output.txt", 'w', encoding='utf-8') as file:
    for cell in result:
        file.write(cell + "\n")
