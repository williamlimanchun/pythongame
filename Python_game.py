import random

class Character:

    def __init__(self, name, *, health = 100, damage = 10, heal = 10):
        self.name = name
        self.health = health
        self.damage = damage
        self.heal = heal

    def recover(self):
        self.health = self.health + self.heal
        print("You healed yourself!")
        print("You have recovered", self.heal,'health!')
        print("You have ",self.health,"hp now!")
    
    def attack(self,*,opponent):
        damage = self.damage
        opponent.health = opponent.health - damage
        print("You attacked the monster!")
        print("You have caused",damage,'damage to the monster!')
        print(opponent.name,"has got",opponent.health,"hp left")

def count_round(num):
    print('Round',num,":")

def monster_attack():
    rand = int(random.uniform(1,3))
    if rand == 1:
        player.health = player.health - monster.damage
        print("You are attacked by the monster! You have",player.health,'hp left!')
    else:
        print("The monster tried to attack you but miss!")

player = Character(input('Enter you name here: '))
monster = Character('Monster', health=100, damage=50)

print('New character is created, named', player.name)
print('Your current health: ', player.health)
print('Your damage is ', player.damage)
print('A creature', monster.name,'is attacking you! Lets fight back!')

round = 0
while (player.health > 0 and monster.health > 0):
    print('Select the action (Attack=1 or heal=2):')

    action = input()

    if (action == '1'):
        round = round + 1
        count_round(round)
        monster_attack()
        player.attack(opponent=monster)
    elif (action == '2'):
        round = round + 1
        count_round(round)
        monster_attack()
        player.recover()
    else:
        print("Invalid input! Try again!")

if monster.health <=0:
    print("You Win! Game over!")
elif player.health <=0:
    print("You lose! Game over!")
