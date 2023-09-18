# a = "1"
a = 1
# b = "2"
b = 2
print(a + b)


a = "1"
b = "2"
print(int(a) + int(b))

# error
a = "1mohd"
b = "100"
print(int(a) + int(b))



# explecit type casting
string = "15"
number = 7
string_number = int(string) #throws an error if the string is not a valid integer
sum= number + string_number
print("The Sum of both the numbers is: ", sum)



# implicit type casting
# Python automatically converts
# a to int
a = 7
print(type(a))
 
# Python automatically converts b to float
b = 3.0
print(type(b))
 
# Python automatically converts c to float as it is a float addition
c = a + b
print(c)
print(type(c))