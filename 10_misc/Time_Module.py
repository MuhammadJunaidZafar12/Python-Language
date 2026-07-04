import time

print(6)
time.sleep(3)
print("This is printed after 3 second")

t = time.localtime()
formated_time = time.strftime("%Y-%m-%d %H-%M-%S", t)
print(formated_time)