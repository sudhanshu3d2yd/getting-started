def square(n):
    return n * n

def cube(n):
    return n * n * n

i = int(input("Enter a number: "))
choice = input("square or cube? (s/c): ")

if choice == "s":
    print("Square =", square(i))

elif choice == "c":
    print("Cube =", cube(i))

else:
    print("Invalid choice")