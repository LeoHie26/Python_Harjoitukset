#Nimi ja tervehdys AKA. kysymys 1
name = input("Give name: ")
greeting = ("Hello, " + name + "!")
print (greeting)




#ympyrän pinta-ala AKA. kysymys 2
import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
print("The area of the circle is", + area)




#Suorakulmion pinta-ala AKA. kysymys 3
import math
lenght = float(input("Enter the lenght of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

perimeter = 2 * (lenght + width)
area = lenght * width

print("The perimeter of the rectangle is", + perimeter)
print("The area of the rectangle is", + area)




#Joku hävytön numero generaattori laskin juttu AKA. kysymys 4
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))
sum_of_numbers = num1 + num2 + num3
product_of_numbers = num1 * num2 * num3
average_of_numbers = sum_of_numbers / 3

print("The sum of the numbers:", sum_of_numbers)
print("The product of the numbers:", product_of_numbers)
print("The average of the numbers:", average_of_numbers)




#Naula juttu AKA. kysymys 5
talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

total_grams = (talents * 20 * 32 * 13.3) + (pounds * 32 * 13.3) + (lots * 13.3)

kilograms = int(total_grams // 1000)
remaining_grams = round(total_grams % 1000, 2)

print("The weight in modern units: ")
print(f"{kilograms} kilograms and {remaining_grams:.2f} grams.")




#Arpoja AKA. tehtävä 6
import random

lock_3_digit = "".join(str(random.randint(0, 9)) for i in range(3))

lock_4_digit = "".join(str(random.randint(1, 6)) for i in range(4))

print("3-digit code:", lock_3_digit)
print("4-digit code:", lock_4_digit)
