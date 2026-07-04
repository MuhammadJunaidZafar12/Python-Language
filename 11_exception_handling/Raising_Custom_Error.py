# if we want to create custom errors
a = int(input("Enter any value between 5 and 9"))
if a<5 or a<8:
    raise ValueError("Value should be between 5 and 9")

# we make also user defined exception using a class