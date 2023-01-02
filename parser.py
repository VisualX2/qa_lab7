def parser(result_dict):
    res = []
    for line in result_dict:
        if "sec" in str(line):
            x = line.split(" ")
            res.append({"Interval":x[3],"Transfer":x[6],"Bandwidth":x[10]})
    print(res)
    return res