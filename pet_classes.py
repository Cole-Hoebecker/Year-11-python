class Pet:
    def __init__(self, name, category, age, vaccinated, ccard, billing_address): #Initialise class
        self.name = name #Define variables as themself
        self.category = category
        self.age = age
        self.vaccinated = vaccinated
        self.ccard = ccard
        self.billing_address = billing_address
        self.owner_name = 'unknown' #owner name is preset to unknown
        self.account_balance = 0 #account balance is preset to 0

#Pet's information

p1 = Pet('Bonnie', 'cat', 3, True, '1200 1291 8128 2672', 'Vietnam') 
print(f"{p1.name}'s vaccinated status is {p1.vaccinated}")
p2 = Pet('Foxy', 'dog', 3, True, '1200 1291 8128 2672', 'Vietnam') 
