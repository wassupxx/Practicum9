with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    numbers = []
    for line in lines:
        numbers.append(line.strip())
    try:
        num_1 = int(numbers[0])
        num_2 = int(numbers[1])
        num_3 = int(numbers[2])
    except ValueError:
        with open("output.txt", "w", encoding="utf-8") as fl:
            fl.write("data error")
            exit()
            
    try:
        result = (num_1 / num_2) + num_3
    except ZeroDivisionError:
        with open("output.txt", "w", encoding="utf-8") as fl:
            fl.write("division by 0")
            exit()
            
    with open("output.txt", "w", encoding="utf-8") as fe:
        fe.write(str(result))
