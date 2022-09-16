import sys

#Page size 2112 = 2048 + 64 ECC and other
with open(sys.argv[1], "rb") as f_in:
    f_out = open(sys.argv[2], "wb")
    r_byte = f_in.read(1)
    i = 0
    while r_byte != b"":
        if (i % (2048+64)) < 2048:
            f_out.write(r_byte)
        r_byte = f_in.read(1)
        i += 1
    f_out.close()
