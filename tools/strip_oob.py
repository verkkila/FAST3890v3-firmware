import sys
import os

DATA_SIZE = 2048
OOB_SIZE = 64
PAGE_SIZE = DATA_SIZE + OOB_SIZE

def strip_oob(infile, outfile):
    page_count = 0
    print(f"Source file size: {os.path.getsize(infile)}")
    with open(infile, "rb") as f_in, open(outfile, "wb") as f_out:
        while True:
            data = f_in.read(PAGE_SIZE)
            if not data:
                break
            f_out.write(data[:DATA_SIZE])
            page_count += 1
        print(f"Destination file size: {os.path.getsize(outfile)}")
        print(f"Page count: {page_count}")

if __name__ == "__main__":
    strip_oob(sys.argv[1], sys.argv[2])
