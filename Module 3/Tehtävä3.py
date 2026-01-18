gender = input("Enter biological gender (male/female): ").lower()
hemoglobin_value = float(input("Enter hemoglobin value (g/l): "))

#male normal hemoglobin is between 134-167 g/l
if gender == "male":
    if hemoglobin_value >= 134 and hemoglobin_value <= 167:
        print("Your hemoglobin is normal.")
    elif hemoglobin_value < 134:
        print("Your hemoglobin is low.")
    elif hemoglobin_value > 167:
        print("Your hemoglobin is high.")

#female normal hemoglobin is between 117-155 g/l
elif gender == "female":
    if hemoglobin_value >= 117 and hemoglobin_value <= 155:
        print("Your hemoglobin is normal.")
    elif hemoglobin_value < 117:
        print("Your hemoglobin is low.")
    elif hemoglobin_value > 155:
        print("Your hemoglobin is high.")

else:
    print("Invalid gender.")



