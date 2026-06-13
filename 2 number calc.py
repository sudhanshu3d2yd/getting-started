a = int(input("enter a number: "))
b = int(input("enter second number: "))
o = input("select operation (+,-,*,/): ")
print(a,o,b,"is")
if o == "+":
    print(a+b)
elif o == "-":
    print(a-b)
elif o == "/":
    print(a/b)
elif o == "*":
    print(a*b)
else:
    print("enter valid inputs")
