import sys

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

    for line in lines:
        line = line.rstrip("\n")
        full = ""
        for i in range(0, int(len(line) / 4)):
            start = i*4
            end = (i+1)*4
            if end >= len(line):
                end = len(line)
            full += "".join(line[start:end])[::-1]
        print(full)
