def countdown(n):
    print(n)    
    if n>0:
        return countdown(n-1)
    elif n==0:
        return 0
n=int(input("Enter the number of counts:"))
countdown(n)
print("Launch!!!")
