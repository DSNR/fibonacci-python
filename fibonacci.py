# -------------------------------------------------------------------------- 
# Basic generation of the Fibonacci number sequence written in Python
#  link:   https://www.mycompiler.io/view/6S2zX4i
#  author: milk
# -------------------------------------------------------------------------- 
#  python fibonacci.py # to run this script
# 
count=100 #set how many numbers into the sequence to show
#
# initial vars
a=0     #  first number
b=0     # second number
c=1     #  third number
i=0     # iterator
#
# loop for count
while (i<=count):
    print(c)    # display current number
    a=b         #  first step
    b=c         # second step
    c=a+b       #  third step 
    i+=1        # increment loop count
#
#
#
