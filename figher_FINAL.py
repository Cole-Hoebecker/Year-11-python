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
            multiplier = 0.5
        print('Attack power:', attack_power)
        print('Multiplier:', multiplier)
        return attack_power*multiplier
    
    
    def defend(self, attack_power):
        damage = attack_power - self.shield
        if damage > 0:
            damage = round(damage, 1)
            self.health -= damage
            print("Damage:", damage)
        else:
            print("No damage")

    def is_dead(self):
        if self.health <= 0:
            return True
        else:
            return False
    
    
    def report(self):
        print(self.name+':'+ ' Health: '+ str(self.health))
#Class for the wizard. The Wizard uses magic to amplify his attack.
class Wizard(Fighter):
    def __init__(self, name, health, weapon, shield, magic): #Wizard's attributes
        super().__init__(name, health, weapon, shield) #Wizard inherits some of the Fighter's attributes
        self.magic = magic #Since he's a wizard, he obviously has magic

    def report(self):
        print(self.name+':'+ ' Health: '+ str(self.health))

    def random_attack(self):
        attack_power = (random.randint(int(self.weapon/2), self.weapon*2)) + self.magic #Magic power adds to the attack_power
        print('Attack power:', attack_power)
        return attack_power 
    
    
    def skill_attack(self):
        attack_power = random.randint(int(self.weapon/2), self.weapon*2) + int(self.magic)
        target = random.randint(3,6) #The player has to hit enter between these numbers
        print('Hit enter in exactly', target, 'seconds')
        tic = time.time() #Timing how long it takes for the player to press enter
        input()
        toc = time.time()
        time_taken = toc - tic
        multiplier = 2.5 - abs(target - time_taken) #Giving a multiplier based on how close the player got to the target
        multiplier = round(multiplier, 1) #Rounding the multipler to 1 decimal place for simpler statistics
        if multiplier < 1.5: #If the player is too far off the target, they don't do damage
            multiplier = 0.5
        print('Attack power:', attack_power)
        print('Multiplier:', multiplier)
        return attack_power*multiplier
    
    
    def defend(self, attack_power):
        damage = attack_power - self.shield
        if damage > 0:
            damage = round(damage, 1)
            self.health -= damage
            print("Damage:", damage)
        else:
            print("No damage")

    def is_dead(self):
        if self.health <= 0:
            return True
        else:
            return False

#Ninja class. The ninja has a chance to dodge attacks based on his speed
class Ninja(Fighter):
    def __init__(self, name, health, weapon, shield, speed):
        super().__init__(name, health, weapon, shield)
        self.speed = speed
    
    def random_attack(self):
        attack_power = random.randint(int(self.weapon/2), self.weapon*2)
        print('Attack power:', attack_power)
        return attack_power
    
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
        if multiplier < 1.5: #If the player is too far off the target, they do half damage
            multiplier = 0.5
        print('Attack power:', attack_power)
        print('Multiplier:', multiplier)
        return attack_power*multiplier
    
    def defend(self, attack_power):
        damage = attack_power - self.shield
        #Dodge chance is dependent on the Ninja's speed
        dodge_chance = random.randint(0,100)
        if dodge_chance < self.speed:
            damage = 0
            print(f"{self.name} dodged the attack")
        elif damage > 0:
            damage = round(damage, 1)
            self.health -= damage
            print("Damage:", damage)
        elif damage < 0:
            print("No damage")

    def is_dead(self):
        if self.health <= 0:
            return True
        else:
            return False
        
    def report(self):
        print(self.name+':'+ ' Health: '+ str(self.health))

#The player can choose their class as well as their enemy class. They can also choose a name

player_class = input("Choose a class you would like to play as: Fighter, Wizard or Ninja: ")
player_name = input("Choose a name for yourself: ")
enemy_class = input("Choose a class you want the enemy as: Fighter, Wizard or Ninja: ")
if player_class == 'Fighter':
    player_class = Fighter(player_name, 100, 60, 20)
elif player_class == 'Wizard':
    player_class = Wizard(player_name, 150, 30, 20, 50)
elif player_class == 'Ninja':
    player_class = Ninja(player_name, 80, 30, 15, 70)

if enemy_class == 'Fighter':
    enemy_class = Fighter('Fighter', 100, 60, 20)
elif enemy_class == 'Wizard':
    enemy_class = Wizard('The Black Wizard', 150, 30, 20, 50)
elif enemy_class == 'Ninja':
    enemy_class = Ninja('The Black Ninja', 80, 30, 15, 70)



#Loop the fight. It will end when someone's health is below 0
while True:
    #Printing each player's health
    enemy_class.report()
    player_class.report()  
    #Printing a blank line to make it easier to read
    print()
    #Will only attack if you are not dead.
    if player_class.is_dead() is False:
        print("You attack", enemy_class.name)
        #Deducts health based on the random attack power
        enemy_class.defend(player_class.skill_attack())
        print()
        enemy_class.report()
        player_class.report()
        #Adding a 1 second delay to make it seem more like a game
        time.sleep(1)
    else:
        break
    print()
    if enemy_class.is_dead() is False:
        print(f"{enemy_class.name} attacks {player_class.name}")
        player_class.defend(player_class.random_attack())
        time.sleep(1)
    else:
        break
    print()
#Winner is declared
if enemy_class.is_dead() is True:
    print(f"Winner: {player_class.name}")
else:
     print(f"Winner: {enemy_class.name}")


