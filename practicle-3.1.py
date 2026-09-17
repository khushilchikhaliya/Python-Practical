n1 = 0
n2 = 1

n = int(input("Enter the number of term : "))

# pending code for fibonacci 
print(n1 , "\n")
print(n2 , "\n")

for i in range(0,n-2,1):
    n3 = n1 + n2
    n1 = n2
    n2 = n3 

    print(n2, "\n")

     


