from pathlib import Path

base_dir = Path(__file__).resolve().parent

# f = open(base_dir / "myfile.txt", "r") # r for read its also by default
# # print(f) # this not read the content in the file
# text = f.read()
# print(text)
# f.close()

# f = open(base_dir / "myfile2.txt", "w") # w for write
fs = open(base_dir / "myfile2.txt", "a") # a for append
fs.write("Hello world!\n")
fs.close()


# with method
with open(base_dir / 'myfile.txt', 'a') as f:
    f.write("Hay i am inside with\n")