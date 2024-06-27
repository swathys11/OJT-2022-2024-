i = 1
while (i<=20):
    print(i)
    i=i+1
    
#while loop with else
num = int(input("Enter a number: "))
i = 2
while i<num :
    if num%1==0:
        print("Not a prime number")
        break
    i=i+1
else:
    print("Is a prime nummber")