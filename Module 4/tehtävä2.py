length_inches = float(input("Enter the length in inches (negative value to quit): "))

while length_inches >= 0:
    length_centimeters = length_inches * 2.54
    print(f"{length_inches} inches is {length_centimeters:.2f} centimeters")
    length_inches = float(input("Enter the length in inches (negative value to quit): "))
else:
    print("Program ended.")