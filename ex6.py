with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    try:
        N = int(lines[0].strip())
    except ValueError:
        with open("output.txt", "w", encoding="utf-8") as fl:
            fl.write("ERROR")
            exit()
    with open("output.txt", "w", encoding="utf-8") as fl:
        if N == len(lines) - 1:
            fl.write("YES")
        else:
            fl.write("NO")
