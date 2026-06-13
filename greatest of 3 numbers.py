a = int(input("enter a number \n"))
b = int(input("enter a number \n"))
c = int(input("enter a number \n"))
if a>=b and a>=c:
    print(a , " is greatest")
else:
    if b>=a and b>=c:
        print(b , "is greatest")
    else:
        print(c , "is greatest")