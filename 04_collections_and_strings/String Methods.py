# strings are immutable

a = "Junaid! !!!!! Junaid"
print(len(a))
# x=a.upper()
x=a.lower()
print(x)
print(a.rstrip("!")) #this make the copy of string not change the Original string
print(a.replace("Junaid", "Zaid"))
print( "Split: ", a.split(" ")) # make the array of the words after or before the space
blog_heading = "introduction to js"
print(blog_heading.capitalize())

star1 = "Welcome to the console"
print(len(star1))
print((star1.center(50)))

print(a.count("Junaid"))

str1 = "Welcome to the string\n !!!"
print(str1.endswith("!!!"))
print(str1.endswith("to", 4 ,10))
print(str1.find("to")) # its give the index ... if not found then return -1

# isalnum() return true and false.... if A-Z, a-z and 0-9 words or characters are not found then gave false
# isalpha() ................ A-Z, a-z .......................
# islower() #if the strings are lowercase then return true
print(str1.isprintable()) # if not have any escape sequence then printable returns true otherwise returns false

str1 = "     "
print(str1.isspace()) # if the string has only spaces

# istitle() to check the first letter is capitalized or not of every Word

# isupper() # check upper case or not

# startswith() detect start with any charactor

# swapcase() # change uppercase to lowerCase and lowercase to upperCase

#title() #make the first letter of every word capital