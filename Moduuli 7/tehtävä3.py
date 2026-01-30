airports = {}

while True:
    print("\nAirport Data Management")
    user_input = input("1. Enter a new airport\n2. Fetch airport information\n3. Quit\nPlease choose an option (1-3): ")

    if user_input == "1":
        icao = input("Enter the ICAO code: ").strip().upper()
        if icao == "":
            print("ICAO code can not be empty.")
            continue

        airport_name = input("Enter the airport name: ").strip()
        if airport_name == "":
            print("Airport name can not be empty. ")

        airports[icao] = airport_name
        print(f"Airport {airport_name} with ICAO code {icao} has been added.")

    elif user_input == "2":
        icao = input("Enter the ICAO code: ")
        if icao in airports:
            print(f"The airport with ICAO code {icao} is {airports[icao]}.")

        else:
            print(f"No airport found with ICAO code {icao}.")

    elif user_input == "3":
        print("Thank you for using the Airport Data Management system. Goodbye!")
        break

    else:
        print("Invalid option, please enter number between 1 to 3.")
