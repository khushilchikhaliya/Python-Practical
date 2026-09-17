n = int(input("enter number of elements : "))

t = ()

for i in range(n):
    x = int(input("enter value: "))
    t = t + (x,)

print("Tuple", t)

print("First element : ", t[0])

print("Tuple elements : ")
for x in t: 
    print(x)