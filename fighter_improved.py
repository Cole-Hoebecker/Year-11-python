import random
import time
#Class containing the types of attributes each fighter will have
class Fighter():
    def __init__(self, name, health, weapon, shield):
        self.name = name
        self.health = health 
        self.weapon = weapon
        self.shield = shield
#Making the attack power based on your weapon's stats
    def random_attack(self):
        attack_power = random.randint(int(self.weapon/2), self.weapon*2)
        print('Attack power:', attack_power)
        return attack_power
    
    def defend(self, attack_power):
        damage = attack_power - self.shield
        if damage > 0:
            self.health -= damage
            print("Damage:", damage)
        else:
            print("No damage")

#Fighter stats
you = Fighter('You', 100, 60, 20)
troll = Fighter('Troll', 200, 30, 10)

#Loop the fight. It will end when someone's health is below 0
while True:
    #Printing each player's health
    print("You: Health:", you.health)
    print("Troll: Health:", troll.health)   
    #Printing a blank line to make it easier to read
    print()
    #Will only attack if you are not dead.
    if you.health > 0:
        print("You attack the troll")
        #Deducts health based on the random attack power
        troll.defend(you.random_attack())
        print()
        print("You: Health:", you.health)
        print("Troll: Health:", troll.health)
        #Adding a 1 second delay to make it seem more like a game
        time.sleep(1)
    else:
        break
    print()
    if troll.health > 0:
        print("The troll attacks you...")
        you.defend(you.random_attack())
        time.sleep(1)
    else:
        break
    print()
#Winner is declared
if troll.health > you.health:
    print(f"Winner: {troll.name}")
else:
     print(f"Winner: {you.name}")


