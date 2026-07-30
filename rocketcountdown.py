def rocketcount(x):
    if x==0:
        print("Launch!!")
        return
    print(x)
    rocketcount(x-1)

n= int(input("enter the countdown value"))
rocketcount(n)
