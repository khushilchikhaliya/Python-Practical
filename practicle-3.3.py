a = int(input("Enter starting number: "))
b = int(input("Enter ending number: "))

for n in range(a, b):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            print(n, end=" ")