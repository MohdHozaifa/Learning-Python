#ques:- Create a python program capable of greeting you with Good Morning, Good Afternoon 
#       and Good Evening. Your program should use time module to get the current hour. 
#       Here is a sample program and documentation link for you:

# https://docs.python.org/3/library/time.html#time.strftime
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hour = int(time.strftime('%H'))
print(hour)
minutes = int(time.strftime('%M'))
print(minutes)
second = int(time.strftime('%S'))
print(second)



if(hour>=4 and hour<12):
    print("Good Morning")
elif(hour>=12 and hour<16):
    print("Good Afternoon")
elif(hour>=16 and hour<22):
    print("Good Evening")
else:
    print("Good Night")
