weight = int (input("Enter Your Weight : "))
unit = input("(L)bs or (K)g: ")

if unit.upper() == 'K':
    weight *= 2.2046
    print(f"You are {weight} pounds")

else:
    weight *= 0.4535
    print(f"You are {weight} kilos")

