from random import randint
class PlayerClass ():
	def __init__ (self, Name, Healing, Armour):
		self._Name = Name
		self._Healing = Healing
		self._Armour = Armour

	def getHealing(self):
		return self._Healing
	def getName(self):
		return self._Name
	def getHealing(self):
		return self._Healing
	def getArmour(self):
		return self._Armour
	def getName(self):
		return self._Name

class Mage (PlayerClass):
	def __init__ (self):
		super().__init__ ("Mage", 5, 0)
		self._BasicAttack = BasicAttack(15,15)

class Hunter (PlayerClass):
	def __init__ (self):
		super().__init__ ("Hunter", 3, 0)
		self._BasicAttack = BasicAttack (10,25)

class Soldier (PlayerClass):
	def __init__ (self):
		super().__init__ ("Soldier", 3, 0)
		self._BasicAttack = BasicAttack(35,7)



class Medic (PlayerClass):
	def __init__ (self):
		super().__init__ ("Medic", 10, 20)
		self._BasicAttack = BasicAttack(10,10)



class BasicAttack ():
	def __init__ (self, Damage, Range):
		self._Damage = Damage
		self._Range = Range

	def getDamage(self):
		return self._Damage
	def getRange(self):
		return self._Range


#####################################################################


class Race ():
	def __init__ (self, Health, Name, SpeedMod):
		self._Health = Health
		self._Name = Name
		self._SpeedMod = SpeedMod

	def getHealth(self):
		return self._Health
	def getName(self):
		return self._Name

class Elf (Race):
	def __init__ (self):
		super().__init__(40, "Elf",6)

class Humanoid (Race):
	def __init__ (self):
		super().__init__(45, "Humanoid",5)

class HalfOrc (Race):
	def __init__ (self):
		super().__init__(60, "Half Orc",2)

class Dwarf (Race):
	def __init__ (self):
		super().__init__(30, "Dwarf",8)

#####################################################################

class Monsters ():
	def __init__(self, name, hp, Damage, Range, Speed, position = randint(20,40)):
		self._hp = hp
		self._Name = name
		self._Damage = Damage
		self._Range = Range
		self._Speed = Speed
		self._Position = position
		self._hasAttacked = 0

	def printStats(self, player):
		print(
		"The Monster is a,", self._Name,"\n"
		"Health:", self._hp,"\n"
		"Damage:", self._Damage,"\n"
		"Range:", self._Range,"\n"
		"Position:", self._Position,"\n"
		"Movement:", self._Speed,"blocks \n"
		"The enemy is", (abs(self.getPosition() - player.getPosition())), "blocks away.\n"
		)



	def attack (self, player):
		if (abs(self.getPosition() - player.getPosition()) <= self._Range ):
			player.takeDamage(self._Damage)
			print("The enemy has attacked! Your health is now,", player.getHealth(),"\n")
			self.attacked()
			input()

	def block (self, player):
		if player.getSuccessfulSpecialAttack() == True:
			print("The computer has attempted to block your attack but was unsuccessful.")
		elif player.getSuccessfulAttack() == True:
			self._hp += player.getDamagePlayer()
			print("The enemy has blocked the attack! Their Health is still,", self._hp)
			input()
		else:
			print("The enemy has attempted to block")
			input()
			pass


	def takeDamage (self, DamageTaken):
		self._hp -= DamageTaken

	def getPosition(self):
		return self._Position

	def getHealth (self):
		return self._hp

	def move (self, player):
		if (abs(self.getPosition() - player.getPosition()) >= self._Speed):
			self._Position -= self._Speed
			print("The enemy has moved and is now,", (abs(self.getPosition() - player.getPosition())), "blocks away. \n" )
			input()
		else:
			self._Position -= ((abs(self.getPosition() - player.getPosition())) - self._Range)
			print("The enemy has moved and is now,", (abs(self.getPosition() - player.getPosition())), "blocks away. \n" )
			input()

	def turn (self, player):
		self.resetAttacked()
		self.printStats(player)
		if (abs(self.getPosition() - player.getPosition()) > self._Range ) and (abs(self.getPosition() - player.getPosition())<= player.getRangePlayer()):
			choice= randint(0,1)
			if choice == 0:
				self.move(player)
			else:
				self.block(player)
		elif (abs(self.getPosition() - player.getPosition()) > self._Range) and (abs(self.getPosition() - player.getPosition()) > player.getRangePlayer()):
			self.move(player)
		elif (abs(self.getPosition() - player.getPosition()) <= self._Range) and (abs(self.getPosition() - player.getPosition()) > player.getRangePlayer()):
			self.attack(player)
		else:
			choice = randint(0,1)
			if choice == 0:
				self.attack(player)
			else:
				self.block(player)

	def getMonDamage(self):
		return self._Damage

	def resetAttacked(self):
		self._hasAttacked = False
	def attacked(self):
		self._hasAttacked = True
	def getAttacked(self):
		return self._hasAttacked


class Dragon (Monsters):
	def __init__(self):
		super().__init__("Dragon",80, 20, 9, 10)

class Orc (Monsters):
	def __init__(self):
		super().__init__("Orc",150, 15, 5, 6)

class FrostGiant (Monsters):
	def __init__(self):
		super().__init__("Frost Giant",110, 13, 7, 8)
monsterList = [Dragon(),Orc(),FrostGiant()]
#####################################################################

def ChooseClass ():

	classList = [Mage(), Hunter(), Soldier(), Medic()]
	raceList = [Elf(), Humanoid(), HalfOrc(), Dwarf()]

	while True:
		try:
			ClassInput = int(input("""

Choose a Class:
1 = Mage (Damage = 15, Range = 15, Healing = 5, Armour = 0)
2 = Hunter (Damage = 10, Range = 25, Healing = 3, Armour = 0)
3 = Soldier (Damage = 35, Range = 7, Healing = 3, Armour = 0)
4 = Medic (Damage = 10, Range = 10, Healing = 10, Armour = 20)

"""))
			break

		except ValueError:
			print("\nyou have not entered a number, please try again.\n")


	while ClassInput not in [1,2,3,4]:
		try:
			ClassInput = int(input("""
Please choose a valid number

Choose a Class:
1 = Mage (Damage = 15, Range = 15, Healing = 5, Armour = 0)
2 = Hunter (Damage = 10, Range = 25, Healing = 3, Armour = 0)
3 = Soldier (Damage = 35, Range = 7, Healing = 3, Armour = 0)
4 = Medic (Damage = 10, Range = 10, Healing = 10, Armour = 20 - This is added on to the health of the player.)

"""))

		except ValueError:
			print("\nyou have not entered a number, please try again.\n")


	Class = classList[ClassInput-1]
	return Class

#####################################################################


class Player():

	def __init__ (self, Class, hp = 20, speed = 2, position = 0):
		self.myClass = Class
		self._hp = hp
		self._PlayerSpeed = speed
		self._Position = position
		self.race = 0
		self._successfulAttack = 0
		self._turns= 0
		self._SpecialAttackDamage = 1.5 * self.myClass._BasicAttack.getDamage()

		self._classList = [Mage(), Hunter(), Soldier(), Medic()]
		self._raceList = [Elf(), Humanoid(), HalfOrc(), Dwarf()]

	def setStats(self):
		self._hp += self.race._Health + self.myClass._Armour
		self._PlayerSpeed += self.race._SpeedMod

	def PlayerRaceInput (self):
		while True:
			try:
				RaceInput = int(input("""

Choose a Race:
1 = Elf (Health = 40, Speed Modifier = 6)
2 = Humanoid (Health = 45, Speed Modifier = 5)
3 = HalfOrc (Health = 60, Speed Modifier = 2)
4 = Dwarf (Health = 30, Speed Modifier = 8)

"""))
				break

			except ValueError:
				print("\nyou have not entered a number, please try again.\n")


		while RaceInput not in [1,2,3,4]:
			try:
				RaceInput = int(input("""
Please choose a valid number

Choose a Race:
1 = Elf
2 = Humanoid
3 = HalfOrc
4 = Dwarf

"""))
			except ValueError:
				print("\nyou have not entered a number, please try again.\n")

		self.race = self._raceList[RaceInput-1]
		return self.race


	def printStats(self):
		print(
			"You are a,", self.myClass.getName(), self.race.getName(),"\n"
			"Health = ", self.getHealth(), "\n"
			"Healing Ability = ", self.myClass.getHealing(),"\n"
			"Attack Damage =" ,self.myClass._BasicAttack.getDamage(),"\n"
			"Range =", self.myClass._BasicAttack.getRange(),"\n"
			"Position = " ,self._Position ,"\n"
			"Movement =", self._PlayerSpeed, "blocks \n"
			"Turns =", self._turns,"\n"
			)
	def printControls(self):
		print(
		"To ATTACK type: 'a' \n"
		"To BLOCK type: 'b' (Deals 20 percent of enemies damage) \n"
		"To HEAL type: 'h' \n"
		"To MOVE type: 'm' \n"
		"SPECIAL ATTACK : 's' (Can only be used every 5 turns) \n"
		)

	def attack (self, enemy):
		self.resetSuccessfuAttack()
		if (abs(self.getPosition() - enemy.getPosition()) <= self.myClass._BasicAttack.getRange() ):
			enemy.takeDamage(self.myClass._BasicAttack.getDamage())
			self.successfulAttack()
			print("Enemy Health is now,", enemy.getHealth(),"\n")
			input()
		else:
			print("Enemy is out of range. Attack missed. \n")
			input()

	def specialAttack (self, enemy):
		self.successfulSpecialAttack()
		enemy.takeDamage(self._SpecialAttackDamage)
		print("You have successfully used your Special Attack.")
		print("Enemy Health is now,", enemy.getHealth(),"\n")
		input()


	def heal (self):
		self._hp += self.myClass.getHealing()
		print("Your health is now,", self._hp ,"\n")
		input()

	def move (self):
		while True:
			blocks = int(input("\nHow many blocks would you like to move? (use negative numbers to move backwards) \n"))
			if blocks <= self._PlayerSpeed:
				self._Position += blocks
				break

			else:
				print("This number is greater than your allowed movement. Try again\n")
		input()

	def turn (self, enemy):
		self.printStats()
		self.printControls()
		self.resetSuccessfuAttack()
		self.resetSpecialAttack()
		print("the enemy is,", (abs(self.getPosition() - enemy.getPosition())),"blocks away \n")
		while True:
			decision = input("what would you like to do? \n")
			if decision == 'a':
				self.attack(enemy)
				self._turns+=1
				break

			elif decision == 'b':
				self.block(enemy)
				self._turns+=1
				break

			elif decision == 'h':
				self.heal()
				self._turns+=1
				break

			elif decision == 'm':
				self.move ()
				self._turns+=1
				break
			elif decision == 's':
				if self._turns % 5 == 0:
					self.specialAttack(enemy)
					self._turns +=1
					break
				else:
					print("You can only use your special attack every 5 turns. \n")

			else:
				print("invalid input, try again \n")




	def successfulAttack (self):
		self._successfulAttack = True
	def resetSuccessfuAttack (self):
		self._successfulAttack = False
	def getSuccessfulAttack (self):
		return self._successfulAttack

	def successfulSpecialAttack(self):
		self._successfulSpecialAttack = True
	def resetSpecialAttack(self):
		self._successfulSpecialAttack = False
	def getSuccessfulSpecialAttack (self):
		return self._successfulSpecialAttack


	def getPosition(self):
		return self._Position
	def getHealth(self):
		return self._hp
	def takeDamage(self, DamageTaken):
		self._hp -= DamageTaken

	def getDamagePlayer(self):
		return self.myClass._BasicAttack.getDamage()

	def getRangePlayer(self):
		return self.myClass._BasicAttack.getRange()


	def block(self,enemy):
		if enemy.getAttacked() == True:
			self._hp += (round(0.2*enemy.getMonDamage()))
			print("You have successfully blocked the enemy's attack!")
			input()
		else:
			print("You have attempted to block but the enemy has not attacked. \n")
			input()
			pass


def GameOver (player, enemy):
	if player.getHealth() <= 0 or enemy.getHealth() <=0  :
		print("\n Game Over \n")

		if player.getHealth()>0:
			print("YOU WIN :) \n")
		else:
			print("YOU LOSE :( \n")
		return True
	else:
		return False
