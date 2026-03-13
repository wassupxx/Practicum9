with open("input.txt", "r", encoding="utf-8") as fi:
    lines = fi.readlines()
    for line in lines:
        result = " ".join(line[0][0])
        with open ("output.txt", "a", encoding="utf-8") as fl:
            fl.write(result)