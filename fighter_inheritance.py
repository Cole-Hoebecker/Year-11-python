import random
import time
#Class containing the types of attributes each fighter will have
class Fighter():
    def __init__(self, name, health, weapon, shield):
        self.name = name
        self.__health = health 
        self.weapon = weapon
        self.shield = shield
#Making the attack power based on your weapon's stats
    def random_attack(self):
        attack_power = random.randint(int(self.weapon/2), self.weapon*2)
        print('Attack power:', attack_power)
        return attack_power
    #Multiplying the attack power based on a minigame the player goes through
    def skill_attack(self):
        attack_power = random.randint(int(self.weapon/2), self.weapon*2)
        target = random.randint(3,6) #The player has to hit enter between these numbers
        print('Hit enter in exactly', target, 'seconds')
        tic = time.time() #Timing how long it takes for the player to press enter
        input()
        toc = time.time()
        time_taken = toc - tic
        multiplier = 2.5 - abs(target - time_taken) #Giving a multiplier based on how close the player got to the target
        multiplier = round(multiplier, 1) #Rounding the multipler to 1 decimal place for simpler statistics
        if multiplier < 1.5: #If the player is too far off the target, they don't do damage
            multiplier = 0
        print('Attack power:', attack_power)
        print('Multiplier:', multiplier)
        return attack_power*multiplier
    
    
    def defend(self, attack_power):
        damage = attack_power - self.shield
        if damage > 0:
            damage = round(damage, 1)
            self.__health -= damage
            print("Damage:", damage)
        else:
            print("No damage")

    def is_dead(self):
        if self.__health <= 0:
            return True
        else:
            return False
    
    
    def report(self):
        print(self.name+':'+ ' Health: '+ str(self.__health))
#Class for the wizard
class Wizard(Fighter):
    def __init__(self, name, health, weapon, shield, magic): #Wizard's attributes
        super().__init__(name, health, weapon, shield) #Wizard inherits some of the Fighter's attributes
        self.magic = magic #Since he's a wizard, he obviously has magic

    def random_attack(self):
        attack_power = random.randint(int(self.weapon/2), self.weapon*2)
        print('Attack power:', attack_power)
        return attack_power + self.magic #Magic power increases the attack_power

#Fighter stats
you = Fighter('You', 100, 60, 20)
wizard = Wizard('The Black Wizard', 150, 30, 20, 50)

#Loop the fight. It will end when someone's health is below 0
while True:
    #Printing each player's health
    wizard.report()
    you.report()  
    #Printing a blank line to make it easier to read
    print()
    #Will only attack if you are not dead.
    if you.is_dead() is False:
        print("You attack the", wizard.name)
        #Deducts health based on the random attack power
        wizard.defend(you.skill_attack())
        print()
        wizard.report()
        you.report()
        #Adding a 1 second delay to make it seem more like a game
        time.sleep(1)
    else:
        break
    print()
    if wizard.is_dead() is False:
        print(f"The {wizard.name} attacks you...")
        you.defend(you.random_attack())
        time.sleep(1)
    else:
        break
    print()
#Winner is declared
if wizard.is_dead() is True:
    print(f"Winner: {you.name}")
else:
     print(f"Winner: {wizard.name}")


