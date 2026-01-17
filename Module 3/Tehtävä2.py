cabinclass = (input("Enter the cabin class (LUX, A, B, or C): "))
if cabinclass == "LUX":
    print("Upper-deck cabin with a balcony.")

elif cabinclass == "A":
    print("Above the car deck, equipped with a window.")

elif cabinclass == "B":
    print("Windowless cabin above the car deck.")

elif cabinclass == "C":
    print("Windowless cabin below the car deck.")

else:
    print("Invalid cabin class.")