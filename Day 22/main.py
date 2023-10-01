# order maintained
marks = [3,5,6, "Hozaifa", True, 12,34,56,78]
# print(marks)
# print(type(marks))

# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])

# print(marks[-3])  #negative index
# print(len(marks)-3)  #positive index


# if 7 in marks:
#     print("Yes")
# else:
#     print("No")

# if "Hozaifa" in marks:
#     print("Yes")
# else:
#     print("No")


#same thing apply for string as well
# if "Hoz" in "Hozaifa":
#     print("Yes")
# else:
#     print("No")


# print(marks)
# print(marks[:])
# print(marks[1:])
# print(marks[1:-1])
# print(marks[1:4])
# print(marks[1:4:2])
# print(marks[1:7:3])
# print(marks[1:7:2])


#list comprehension
lst = [i for i in range(10)]
print(lst)
lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2 == 0]
print(lst)