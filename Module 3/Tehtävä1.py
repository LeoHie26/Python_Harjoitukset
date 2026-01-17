zander = float(input("Enter the lenght of the zander in centimeters: "))

if zander >=42:
    print("Zander meets the size limit")
else:
    puuttuvat_sentit = float(42 - zander)
    print("The zander does not meet the size limit.\nPlease release the fish back into the lake.")
    print(f"The fish was {puuttuvat_sentit:.1f} centimeters below the size limit.")
