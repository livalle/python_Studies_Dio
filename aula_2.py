print("Think of a number...")
print("Now let's see if our bot can guess it...")
number = int(input("Digit a number: "))
if number <= 10:
    print(f"I think it is the number: {number}")
elif 10 < number <= 25:  # Corrigida a condição
    print(f"I wonder if it is: {number} ...")
elif number > 25:
    print(f"It is hard to tell, but I guess it is number: {number}")
else:
    print("Not sure...")
