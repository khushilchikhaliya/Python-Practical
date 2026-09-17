n = int(input("Enter n : "))

a=[]
for i in range(n):
    a.append(int(input("enter number : ")))

print("original list:" , a)

pos = int(input("enter position : "))
value = int(input("enter value : "))
a.insert(pos , value)

print("after insertaion : ", a)

pos = int(input("enter position : "))
a.pop(pos)

print("after deletation : ", a)