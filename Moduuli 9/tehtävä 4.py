import random
class Car:
    def __init__(self, license_plate, maximum_speed, current_speed=0, travelled_distance=0):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, acceleration):
        if acceleration + self.current_speed >= 0:
            self.current_speed += acceleration

        else:
            self.current_speed = 0

        if acceleration + self.current_speed >= self.maximum_speed:
            self.current_speed = self.maximum_speed

    def drive(self, time):
        if time > 0:
            self.travelled_distance += self.current_speed * time




def race(cars):
    car_one = Car(cars[0], cars[1])
    car_two = Car(cars[2], cars[3])
    car_three = Car(cars[4], cars[5])
    dist = 0

    while dist <= 10000:
        car_one.accelerate(random.randint(-10,15))
        car_two.accelerate(random.randint(-10,15))
        car_three.accelerate(random.randint(-10,15))

        car_one.drive(1)
        car_two.drive(1)
        car_three.drive(1)

        if car_one.travelled_distance > car_two.travelled_distance and car_one.travelled_distance > car_three.travelled_distance:
            dist = car_one.travelled_distance

        elif car_two.travelled_distance > car_one.travelled_distance and car_two.travelled_distance > car_three.travelled_distance:
            dist = car_two.travelled_distance

        elif car_three.travelled_distance > car_one.travelled_distance and car_three.travelled_distance > car_two.travelled_distance:
            dist = car_three.travelled_distance

    print(f"Car: {car_one.license_plate}\nTravelled: {car_one.travelled_distance}km\n-----------------\n"
          f"Car: {car_two.license_plate}\nTravelled: {car_two.travelled_distance}km\n-----------------\n"
          f"Car: {car_three.license_plate}\nTravelled: {car_three.travelled_distance}km\n-----------------\n")

list_of_cars = ["ABC-123", 140, "CBA-321", 140, "BCA-213", 140]
race(list_of_cars)