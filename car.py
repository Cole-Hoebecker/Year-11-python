class Car:
    def __init__(self, make, model, year, door, wheels, colour, seats, horsepower, sunroof, for_sale, price = 0):
        self.door = door
        self.wheels = wheels
        self.colour = colour
        self.seats = seats
        self.horsepower = horsepower
        self.sunroof = sunroof
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.for_sale = for_sale
    

    def __str__(self):
        car = f"Make: {self.make} \nModel: {self.model} \nYear: {self.year} \nPrice: {self.price} \nNumber of doors: {self.door} \nNumber of wheels: {self.wheels} \nColour: {self.colour} \nNumber of seats: {self.seats} \nHorsepower: {self.horsepower} \nSunroof: {self.sunroof} \nFor Sale: {self.for_sale}"
        return car

Ferrari = Car('Ferrari', 'Roma', 2009, 100000, 2, 4, 'red', 2, 900, 'True')
Porche = Car('Porche', 'GT920', 2018, 159000, 2, 4, 'blue', 2, 1500, 'True')
Nissan = Car('Nissan', 'X-Trial', 2013, 20000, 4, 4, 'white', 4, 500, 'False')

cars = [Ferrari, Porche, Nissan]

for car in cars:
    print(car)
    print()