
def get_season(month):

    if month in (12, 1, 2):
        return "winter"
    elif month in (3, 4, 5):
        return "spring"
    elif month in (6, 7, 8):
        return "summer"
    elif month in (9, 10, 11):
        return "autumn"

number_of_the_month = int(input("Enter the number of a month (1-12): "))

if number_of_the_month <=12 and number_of_the_month >=1:
    print(f"You entered: {number_of_the_month}\nThe season is {get_season(number_of_the_month)}.")

else:
    print(f"You entered: {number_of_the_month}\nPlease enter a number between 1 and 12.")



