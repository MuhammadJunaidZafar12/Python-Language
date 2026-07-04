for i in range(5):
    print(i)
    if i == 4:
        break # if this break statement executes then not execution of else statement
else:
    print("Sorry Not i ")


for i in range(5):
    print("iteration on {} in for loop".format(i+1))
else:
    print("Sorry Not i ")
print("out of loop")