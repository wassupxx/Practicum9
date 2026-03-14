with open ("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        if len(line) > 20:
            with open ("output.txt", "a", encoding="utf-8") as fl:
                fl.write(line)
                
