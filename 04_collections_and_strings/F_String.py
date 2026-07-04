# without fstring
letter = "Hey my name is {1} and I am from {0}"

country = "Pakistan"
name = "Junaid"

print(letter.format(country, name)) # the value of country and name goes to the letter string where curly braces use

# we use fstring than upper string method

print(f"Hey my name is {name} and i am from {country}")

# without fstring
# if we take two decimal places in our answer
txt = "For only {price: .2f} dollars!"
print(txt.format(price=49.09999))

# in fstring
price=49.09999
txt = f"For only {price: .2f} dollars!"
print(txt)

print(type(f"{2*38}"))

# when we display name and country as it is then we use double curly braces
print(f"Hey my name is {{name}} and i am from {{country}}")