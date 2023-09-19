# string is immutable no change in original string
a = "!!!! Hozaifa!! !!!!!!! Hozaifa!! !!!"
print(len(a))
print(a.upper())   # immutable --> no change in original string
print(a.lower())
print(a.rstrip("!"))

print(a.replace("Hozaifa", "john"))

# By using this we can form a list
print(a.split(" "))

blogHeading = "introduction to pYthOn."
print(blogHeading.capitalize())

str1 = "Welcome to the Console !!!"
print(len(str1))
print(len(str1.center(50)))

print(a.count("Hozaifa"))
print(a.endswith("!!!"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))

#find method
str1 = "He's name is Dan. He is an honest man."
print(str1.find("is")) 
print(str1.find("ishh")) 

#index method
# print(str1.index("ishh"))

#isalnum
str1 = "WelcomeToTheConsole20"
print(str1.isalnum())

#isalpha
str1 = "Welcome20"
print(str1.isalpha())

str1 = "hello world"
print(str1.islower())

str1 = "We wish you a Merry Christmas"
print(str1.isprintable())
str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())


#isspace()
str1 = "        "       #using Spacebar
print(str1.isspace())
str2 = "        "       #using Tab
print(str2.isspace())


#istitle()
str1 = "World Health Organization" 
print(str1.istitle())

str2 = "To kill a Mocking bird"
print(str2.istitle())


#isupper()
str1 = "WORLD HEALTH ORGANIZATION" 
print(str1.isupper())


#startswith()
str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))



#swapcase()
str1 = "Python is a Interpreted Language" 
print(str1.swapcase())


#title()
str1 = "He's name is Dan. Dan is an honest man."
print(str1.title())