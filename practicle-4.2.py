def simp_i(principal , rate , time):
    si = (principal*rate*time) / 100
    return si

principal = float(input("Enter the principal : "))
rate = float(input("Enter the rate : "))
time = float(input("Enter the time : "))

interest_amount = simp_i(principal , rate , time)

print(interest_amount)