#Class that contains the attributes of a pet for vet purposes
class Pet:
    def __init__(self, name, category, breed = None, age = 0):
        self._name = name
        self.__category = category
        self.__breed = breed
        self.age = age
        self.__ccard = 'unknown'
        self.vaccinated = False
        self._weight = 0
    #Getter method to access weight even though it is a protected attribute
    def get_weight(self):
        return self.weight
#Making sure the weight is a positive number
    def set_weight(self, new_weight):
        if type(new_weight) == int or type(new_weight) == float:
            if new_weight > 0:
                self.weight = new_weight
            else:
                print("Please enter a positive number")
        else:
            print("Please enter a number")
 
p1 = Pet('Bonnie', 'Cat')
#Bonnie's weight. Since it is a positive number it is valid and there will be no prompt to change it
p1.set_weight(12)
print(f"Bonnie's weight: {p1.weight}")
       