number = int(input("Enter an integer: "))

if number < 2:
    print(f"{number} is not a prime number.")

else:
    primenumber = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            primenumber = False
            break
    if primenumber:
        print(f"{number} is a prime number.")

    else:
        print(f"{number} is not a prime number.")