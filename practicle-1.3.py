choice = float(input("Enter 1 ( for calcius ) & 2 ( for ferenhit )"))
if choice == 1 :
        c = float(input("Enter celcius temperature : "))
        f = c * 9/5 + 32 
        print("ferenhit temperature is ", f)
elif choice == 2 :
        f = float(input("Enter ferenhit temperature : "))
        c = (f-32)*5/9
        print("celcius temperature is ", c)   
else :
        print("Unexpected error")

