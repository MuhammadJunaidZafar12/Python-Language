import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)

timestamp1 = int(time.strftime('%H'))
print(timestamp1)

timestamp2 = int(time.strftime('%M'))
print(timestamp2)

timestamp3 = int(time.strftime('%S'))
print(timestamp3)

if 4<=timestamp1<=12:
    print("Good Morning")
elif 12<timestamp1<=17:
    print("good afternoon")
elif 17<timestamp1<=24:
    print("Good Night")

