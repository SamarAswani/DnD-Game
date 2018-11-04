from DnDGame import *
from random import randint

Class = ChooseClass()

player = Player(Class)

player.PlayerRaceInput()

player.setStats()

player.printStats()

monster = monsterList[randint(0,2)]

print("You are fighting a,", monster._Name,"! \n")

monster.printStats(player)

print("\n LET THE BATTLE BEGIN!!!!!! \n")

while True:
    monster.turn(player)
    if GameOver(player, monster) == True:
        break
    player.turn(monster)
    if GameOver(player, monster) == True:
        break
