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


class Race:

    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for i in self.cars:
            i.accelerate(random.randint(-10, 15))
            i.drive(1)

    def print_status(self):
        print("+----------+----------+----------+")
        print(f'|{"LICENCE":10s}|{"SPEED":10s}|{"DISTANCE":10s}')
        print("+----------+----------+----------+")
        for x in self.cars:
            print(f"|{x.license_plate:10s}|{x.current_speed:10d}|{x.travelled_distance:10d}")

    def race_finished(self):
        for y in self.cars:
            if y.travelled_distance >= self.distance:
                return True
        return False
