# def average(a, b):
#     print("The average is ", (a+b)/2)
# average(4,6)   


# default argument
# def average(a = 9, b = 1):
#     print("The average is ", (a+b)/2)
# average() 
# average(1,7) 
# average(1)
# average(b=8)

# def name(fname, mname = "Jhon", lname="Whatson"): 
#     print("Hello,",fname, mname, lname)
# name("Amy","Agarwal","Jain")

#keyword arguments:
# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)

# name(mname = "Peter", lname = "Wesker", fname = "Jade")


#required argument
# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)
# name("Peter", "Quill")

# variable length argument
# def average(*numbers):
#     print(type(numbers))
#     sum = 0
#     for i in numbers:
#         sum = sum + i
#     print("Average is: ", sum/ len(numbers))   
# average(3,4)
# average(7,9,0,3,4,5)  

# taking argument as a dictionary   
# def name(**name):
#     print(type(name))
#     print("Hello,", name["fname"], name["mname"], name["lname"])

# name(mname = "Buchanan", lname = "Barnes", fname = "James")


#return in function
def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum/len(numbers)  

c = average(7,9,0,3,4,5) 
print(c)
