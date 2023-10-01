l = [11 ,2 , 45, 6, 1 , 0, 35, 1]
print(l)
# l.append(7)
# print(l)
# l.sort()
# print(l)
# l.sort(reverse=True)
# print(l)

# l.reverse()
# print(l)

# value 1 is at index 2
# print(l.index(1))

# print(l.count(1))

# copy() of list
# original list will change
# NOTE:- dont do like this
# m = l
# m[0] = 0
# print(l)

# NOTE: do like this
# m = l.copy()
# m[0] = 0
# print(l)
# print(m)

# l.insert(1, 899)
# print(l)


# m = [900, 10000, 1100]
# # l ko kholo end me m list daal do
# l.extend(m)
# print(l)


m = [900, 10000, 1100]
k = l + m
print(k)
print(l)
print(m)
