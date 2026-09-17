a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

if (a>b) & (a>c) :
    print("a is largest")
elif (b>a) & (b>c) :
    print("b is largest")
elif (c>a) & (c>b) :
    print("c is largest")
else :
    print("invalid input")