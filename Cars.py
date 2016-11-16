from pprint import pprint as pp
from random import randint

ENGINE_TYPE_DIESEL = 'diesel'
ENGINE_TYPE_PETROL = 'petrol'

def define_engine_type(car_number):
    if not car_number % 3:
        return ENGINE_TYPE_DIESEL
    else:
        return ENGINE_TYPE_PETROL



class Car(object):
    all_cars = []
    def __init__(self, price, tank=60, start_trip=55000, fuel_consumption=6.0):
        self.engine = define_engine_type(len(Car.all_cars))
        self.price = price
        self.mileage = 0
        self.route_length = randint(start_trip, 286000)
        self.tank_total = tank
        self.tank_current = 1
        self.money_spent = 0
        self.fuel_consumption = fuel_consumption
        Car.all_cars.append(self)
    def drive(self, km):
        self.mileage += km



c1 = Car('diesel', 150000, start_trip=5)
c2 = Car(15, start_trip=215)
c1.drive(5)
c2.drive(50)
pp(c1.mileage)
pp(c2.mileage)
pp(c1.engine)

cars_mileage_list = map(lambda x: x.mileage, Car.all_cars)
total_mileage = sum(cars_mileage_list)
pp(total_mileage)
