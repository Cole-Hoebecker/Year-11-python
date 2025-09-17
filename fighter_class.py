import random
#Class containing the types of attributes each fighter will have
class Fighter():
    def __init__(self, name, health, weapon, shield):
        self.name = name
        self.__health = health #Making health private so it cannot be edited
        self.weapon = weapon
        self.shield = shield
#Making the attack power based on your weapon's stats
    def random_attack(self):
        attack_power = random.randint(int(self.weapon/2), self.weapon*2)
        print('Attack power:', attack_power)
        return attack_power
    #If health needs to be accessed even though it's private, this is used
    def get_health(self):
        return self.__health
#Fighter stats
you = Fighter('You', 100, 60, 20)
troll = Fighter('Troll', 200, 30, 10)
#Using the getter function to access health
you_health = you.get_health()
troll_health = troll.get_health()
#Loop the fight. It will end when someone's health is below 0
while True:
    #Printing each player's health
    print("You: Health:", you_health)
    print("Troll: Health:", troll_health)   
    #Printing a blank line to make it easier to read
    print()
    #Will only attack if you are not dead.
    if you_health > 0:
        print("You attack the troll")
        #Deducts health based on the random attack power
        troll_health -= you.random_attack()
        print("You: Health:", you_health)
        print("Troll: Health:", troll_health)
    else:
        break
    print()
    if troll_health > 0:
        print("The troll attacks you")
        you_health -= you.random_attack()
        print("You: Health:", you_health)
        print("Troll: Health:", troll_health)
    else:
        break
    print()
#Winner is declared
if troll_health > you_health:
    print(f"Winner: {troll.name}")
else:
     print(f"Winner: {you.name}")


