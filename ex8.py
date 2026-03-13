with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    january = 0
    new_lines = []

    for index in range(31):
        steps = int(lines[index].strip())
        january += steps
        jan = january / 31
    new_lines.append(str(jan) + "\n")

    february = 0
    if len(lines) == 365:
        days = 28
    else:
        days = 29

    for index in range(31, days + 31):
        steps = int(lines[index].strip())
        february += steps
        feb = february / days
    new_lines.append(str(feb) + "\n")

    march = 0
    for index in range(days + 31, days + 62):
        steps = int(lines[index].strip())
        march += steps
        mar = march / 31
    new_lines.append(str(mar) + "\n")

    april = 0
    for index in range(days + 62, days + 92):
        steps = int(lines[index].strip())
        april += steps
        apr = april / 30
    new_lines.append(str(apr) + "\n")

    may = 0
    for index in range(days + 92, days + 123):
        steps = int(lines[index].strip())
        may += steps
        ma = may / 31
    new_lines.append(str(ma) + "\n")

    june = 0
    for index in range(days + 123, days + 153):
        steps = int(lines[index].strip())
        june += steps
        jun = june / 30
    new_lines.append(str(jun) + "\n")

    july = 0
    for index in range(days + 153, days + 184):
        steps = int(lines[index].strip())
        july += steps
        jul = july / 31
    new_lines.append(str(jul) + "\n")

    august = 0
    for index in range(days + 184, days + 215):
        steps = int(lines[index].strip())
        august += steps
        aug = august / 31
    new_lines.append(str(aug) + "\n")

    september = 0
    for index in range(days + 215, days + 245):
        steps = int(lines[index].strip())
        september += steps
        sep = september / 30
    new_lines.append(str(sep) + "\n")

    october = 0
    for index in range(days + 245, days + 276):
        steps = int(lines[index].strip())
        october += steps
        octob = october / 31
    new_lines.append(str(octob) + "\n")

    november = 0
    for index in range(days + 276, days + 306):
        steps = int(lines[index].strip())
        november += steps
        now = november / 30
    new_lines.append(str(now) + "\n")

    december = 0
    for index in range(days + 306, days + 337):
        steps = int(lines[index].strip())
        december += steps
        dec = december / 31
    new_lines.append(str(dec) + "\n")
with open("output.txt", "w", encoding="utf-8") as fe:
    fe.writelines(new_lines)
