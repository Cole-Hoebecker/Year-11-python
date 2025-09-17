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
p1.ccard = '1231 1231 1234 2345'
print(p1)
