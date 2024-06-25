# Python Control Statements
# if-else
num =7
if num>0:
    print(num,"is a non zero value")
    print("thank you..")

    num=0
    if num> 0:
        print(num, "is a non-zero value.")
        print("Thank you")
    num =7
    if num>-0:
        print("non zero or zero")
    else:
        print("neg.number")
    num=-3
    if num>=0:
        print("non zero or zero")
    else:
        print("neg.Number")

# Nested if-else
num=6.7
if num>0:
    print("pos.number")
elif num == 0:
    print("zero")
else:
    print("neg.number")

num=-8.9
if num > 0:
    print("pos.number")
elif num == 0:
    print("zero")
else:
    print("Neg.number")

num=0
if num > 0:
    print("pos.number")
elif num == 0:
    print("zero")
else:
    print("Neg.number")

# for Statement
numbers=[6, 5, 3, 8, 4, 2, 5, 4]
sum=0
for val in numbers:
    sum =sum+val 
print("the sum is" ,sum)

numbers=[0,1,3,6]
for i in numbers:
    print(i)
else:
    print("No items left.")

    # while loop
    i=2
    while i<8:
        print(i) 
        i+=1
# program to add natural numbers upto 
# add =1+2+3+..+n
n=20
add=0
i=1
while i<=n:
    add=add+i
    i=i+1
print("the sum",add)

