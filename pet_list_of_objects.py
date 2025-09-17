class Pet:
    def __init__(self, name, category, age = 0):
        self.name = name
        self.category = category
        self.age = age
        self.ccard = 'unknown'
        self.vaccinated = False
    
    def __str__(self):
        payment_status = 'unregistered'
        if len(self.ccard) == 19:
            payment_status = 'registered'

        my_status = f'Name: {self.name} \nCategory: {self.category} \nAge: {self.age} \nPayment Status: {payment_status} \nVaccination status: {self.vaccinated}'
        return my_status


p1 = Pet('Bonnie', 'Cat')
p2 = Pet('Clyde,', 'Dog,', 7)
p3 = Pet(category = 'Rabbit', name = 'Ruby', age = 13)
p4 = Pet(name = 'Nigel', age = 4, category = 'Rat')

pets = [p1, p2, p3, p4]
for pet in pets:
    pet.vaccinated = True
    print(pet)
    print()

