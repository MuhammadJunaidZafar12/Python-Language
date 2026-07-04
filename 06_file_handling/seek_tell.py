from pathlib import Path

base_dir = Path(__file__).resolve().parent

# with open(base_dir / 'myfile2.txt', 'r') as f:
#     print(type(f))
#
#     # move to the 10th bite in the file
#     f.seek(10)
#     # read the first 5 bites
#     f.tell() # returns the current position in the file
#     data = f.read(5)
#     print(data)
with open(base_dir / 'myfile2.txt', 'w') as f:
    f.write('Hello World!!!')
    f.truncate(5)

with open(base_dir / 'myfile2.txt', 'r') as f:
    print(f.read())

