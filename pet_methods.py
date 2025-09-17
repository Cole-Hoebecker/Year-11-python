class Pet:
    def __init__(self, name, category, account_balance, age = 0):
        self.name = name
        self.category = category
        self.age = age
        self.ccard = 'unknown'
        self.vaccinated = False
        self.account_balance = account_balance
    
    def have_birthday(self):
        self.age += 1

    def __str__(self):
        my_status = f'Name: {self.name} \nCategory: {self.category} \nAge: {self.age} \nVaccination status: {self.vaccinated} \nAccount Balance: {self.account_balance}'
        return my_status
    
    def clear_balance(self):
        self.account_balance = 0

    def vaccinate(self):
        self.vaccinated = True

    def pet_age(self):
        if self.category == 'Dog':
            self.age *= 7
        elif self.category == 'Cat':
            self.age *= 6

p1 = Pet('Bonnie', 'Cat', account_balance = 69, age = 10)
p1.have_birthday()
p1.clear_balance()
p1.vaccinate()
p1.pet_age()
print(p1)
