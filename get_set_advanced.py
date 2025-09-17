class Pet:
    def __init__(self, name, category, breed = None, age = 0):
        self._name = name
        self.__category = category
        self.__breed = breed
        self.age = age
        self.__ccard = 'unknown'
        self.vaccinated = False
        self.weight = 0

    def set_name(self,new_name):
        if type(new_name) == str:
            self._name = new_name
        else:
            print('Please use a string as a name attribute')
    
    def get_name(self):
        return self._name

    def get_weight(self):
        return self.weight

    def get_category(self):
        return self.__category
    
    def set_weight(self, new_weight):
        if type(new_weight) == int or type(new_weight) == float:
            if new_weight > 0:
                self.weight = new_weight
            else:
                print('Please enter a positive number for weight')
        else:
            print('Please enter a number for weight')

    def __str__(self):
        payment_status = 'unregistered'
        if len(self.__ccard) == 19:
            payment_status = 'registered'

        my_status = 'Name: ' + self._name +'\nCategory: ' + self.__category + '\nAge: ' + str(self.age) +'\nPayment status: ' + payment_status + '\nVaccinated: '+ str(self.vaccinated)
        return my_status

p1 = Pet(name='Bonnie', category='Dog')
p2 = Pet('Clyde','Cat','Persian',12)
p3 = Pet('Cindy', 'Dog',age = 10)
p4 = Pet('Sean','Sloth',12)
p5 = Pet('Ishraj', 'Dog',age = 7)


#Placing pet's attributes into a list so they can be accessed at the same time all at once
pets = [p1,p2,p3]
#Appending 2 extra pets to the list. (Extend lets you append more than 1 at a time)
pets.extend([p4, p5])
#Using a for loop to change each pet's age to be one year higher
for pet in pets:
    pet.age += 1
    print(pet)
    #Printing a space to make it easier to read
    print()

#Iterating through the pets. If the pet is a dog then it will print its information. It is calling the get function since category is a private attribute
for pet in pets:
    if pet.get_category() == 'Dog':
        print(pet)
        print()