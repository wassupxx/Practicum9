with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(lines)
    for line in lines:
        print(line[0][0])
        if line[0][0] == "a" or line[0][0] == "A":
            with open("output.txt", "a", encoding="utf-8") as fi:
                fi.write(line)