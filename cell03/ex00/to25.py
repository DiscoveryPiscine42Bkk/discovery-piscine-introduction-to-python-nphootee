value = int(input("Enter a number: "))
if value >= 25:
    print("Error")
else:
    for num in range(value, 25):
        print(f"Inside the loop, my variable is {num}")