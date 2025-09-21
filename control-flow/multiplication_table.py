number = int(input("Enter a number to see its multiplication table: "))
for i in range(1, 11):
    X = number
    Y = i
    Z = X * Y
    print(f"{X} x {Y} = {Z}")