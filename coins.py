print("how many coins you have?")

quarters = int( input("quarters"))
dimes = int( input("dimes"))
nickels = int( input("nickels"))
pennies = int( input("pennies"))

total = pennies * 1 + nickels * 5 + dimes * 10 + quarters * 25

cent = total % 100
dollar = total // 100

print(total, "cents")
print("The total is", dollar, "dollars and", cent, "cents")