from pathlib import Path

base_dir = Path(__file__).resolve().parent

# f = open(base_dir / "myfile2.txt", "r")

# i = 0
# while True:
#     i = i + 1
#     line = f.readline()
#     if not line:
#         break
#     m1 = int(line.split(",")[0])
#     m2 = int(line.split(",")[1])
#     m3 = int(line.split(",")[2])
#     print(f"Marks of student {i} is: {m1*2}")
#     print(f"Marks of student {i} is: {m2*2}")
#     print(f"Marks of student {i} is: {m3*2}")

f = open(base_dir / 'myfile2.txt', 'w')
line = ['line 1\n', 'line 2\n', 'line 3\n', 'line 4\n']
f.writelines(line)
f.close()