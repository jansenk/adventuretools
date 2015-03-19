#!python
#Number of Monsters XP Multiplier
from collections import namedtuple 
xpMultiplier = [0, 1, 1.5, 2, 2, 2, 2, 2.5, 2.5, 2.5, 2.5, 3, 3, 3, 3, 4];
xpLimitNames = ["Easy", "Medium", "Hard", "Deadly"]
xpLimitTable = [[25, 50, 75, 100],
								[50, 100, 150, 200],
								[75, 150, 225, 400],
								[125, 250, 375, 500],
								[250, 500, 750, 1100],
								[300, 600, 900, 1400],
								[350, 750, 1100, 1700],
								[450, 900, 1400, 2100],
								[550, 1100, 1600, 2400],
								[600, 1200, 1900, 2800],
								[800, 1600, 2400, 3600],
								[1000, 2000, 3000, 4500],
								[1100, 2200, 3400, 5100],
								[1250, 2500, 3800, 5700],
								[1400, 2800, 4300, 6400],
								[1600, 3200, 4800, 7200],
								[2000, 3900, 5900, 8800],
								[2100, 4200, 6300, 9500],
								[2400, 4900, 7300, 10900],
								[2800, 5700, 8500, 12700]]

def playerLevelValidator(arg):
	if numberValidation(arg):
		parsed = int(arg)
		return parsed > 0 and parsed <= 20
	return False
def numberValidation(arg):
	return arg and type(arg) == type("") and arg.isDigit()
def greaterThanZero(arg):
	return numberValidation(arg) and int(arg) > 0
def hr():
		print "-------------------------------"
def demandInput(arg, prompt, validator):
	while(!validator(arg)):
		arg = input(prompt)

Player = namedtuple('Player', ['level', 'name'])
Enemy = namedtuple('Enemy', ['xp', 'name'])
class Party():
	def __init__(self, verbose=False):
		self.verbose = verbose
		self.players = []
		self.xpLimits = [0, 0, 0, 0]
	def index(self):
		print "Players:"
		hr()
		for i, player in enumerate(self.players):
			print "%d) %s level %d"%(i+1, player.name, player.level)
		hr()
		print "Party XP limits: Easy %d Medium: %d Hard: %d Deadly: %d"%tuple(self.xpLimits)
	def add(self, args):
		if not name:
			name = "player"
		while 1:
			level = int(raw_input("Level: "))
			if level and level >= 1 and level <= 20:
				break
			else:
				print "must be 1-20"
		self.players.append(Player(level, name))
		self.calcXpLimits()
	def delete(self, args):
		target = int(raw_input("id: "))
		if target and target > 0  and target <= len(self.players):
			del self.players[target-1]
			self.calcXpLimits()
		else:
			print "Invalid Index"
		self.calcXpLimits()
	def clone(self, args):
		if target > 0  and target <= len(self.players):
			targetPlayer = self.players[target-1]
			self.players.append(Player(targetPlayer.level, targetPlayer.name))
		else:
			print "Invalid Index"
		self.calcXpLimits()
	def edit(self, input):
		print "Invalid command"
		return self
	def save(self, input):
		print "nyi"
	def load(self, input):
		print "nyi"
	def calcXpLimits(self):
		limits = [0, 0, 0, 0]
		for p in self.players:
			if self.verbose:
				print "player %s level %s: "
			for i in range(0, 4):
				if self.verbose:
					print xpLimitTable[p.level - 1][i]
				limits[i] += xpLimitTable[p.level - 1][i]
		self.xpLimits = limits
	def getMarker(self):
		return "P"
	def levelUp(self, args):
		if len(args) == 1:
			increase = 1
		else:
			try: 
				increase = int(args[1])
			except:
				print "invalid input"
		newList = []
		for p in self.players:
			newList.append(Player(p.level + increase, p.name))
		self.players = newList
			
				
				
			
class Adventure():
	def __init__(self):
		self.encounters = []
	def index(self):
		print "Encounters: "
		hr()
		for i, encounter in enumerate(self.encounters):
			print encounter.simpleDescription(i+1)+" ("+xpLimitNames[encounter.difficulty()]+")"
		hr()
	def add(self):
		self.encounters.append(Encounter(raw_input("Name: ")))
	def delete(self):
		target = int(raw_input("id: "))
		if target and target > 0  and target < len(self.encounters):
			del self.encounters[target-1]
		else:
			print "Invalid Index"
	def clone(self):
		target = int(raw_input("id: "))
		if target and target > 0  and target < len(self.encounters):
			self.encounters.append(Encounter(self.encounters[target]))
		else:
			print "Invalid Index" 
	def edit(self):
		target = int(raw_input("id: "))
		if target and target > 0  and target <= len(self.encounters):
			return self.encounters[target-1]
		else:
			print "Invalid Index" 
			return self
	def save(self, input):
		print "nyi"
	def load(self, input):
		print "nyi"
	def getMarker(self):
		return "A"
	
class Encounter():
	internalCounter = 1
	def __init__(self, name=None):
		self.enemies = []
		self.totalXp = 0
		self.multiplier = 0
		self.adjusted = 0
		print "Name is "+str(name)
		if name is None or name.strip() == "":
			self.name = "Encounter"+str(Encounter.internalCounter)
			Encounter.internalCounter += 1
		else:
			self.name = name
	def index(self):
		print "Encounter: "+self.name
		hr()
		for i, enemy in enumerate(self.enemies):
			print "%d) %s (%d XP)"%(i + 1, enemy.name, enemy.xp)
		hr()
		print self.statString()
		print self.difficultyLine()
	def add(self):
		name = raw_input("Name: ")
		if not name:
			name = "monster"
		while 1:
			xp = int(raw_input("XP: "))
			if xp and xp > 0:
				break
			else:
				print "must be a positive number"
		self.enemies.append(Enemy(xp, name))
		self.recalculate()
	def delete(self, args):
		if len(args) > 1 
		if target and target > 0  and target < len(self.enemies):
			del self.enemies[target]
		else:
			print "Invalid Index"
		self.recalculate()
	def clone(self):
		target = int(raw_input("id: "))
		if target and target > 0  and target < len(self.enemies):
			self.enemies.append(Enemy(self.enemies[target]))
		else:
			print "Invalid Index" 
		self.recalculate()
	def edit(self):
		print "nyi"
		return self
	def save(self, input):
		print "nyi"
	def load(self, input):
		print "nyi"
	def getMarker(self):
		return "E"
	def recalculate(self):
		xp = 0;
		for e in self.enemies:
			xp += e.xp
		self.totalXp = xp
		self.multiplier = xpMultiplier[min(len(self.enemies), 15)] 
		self.adjusted = self.totalXp * self.multiplier
	def simpleDescription(self, number):
		return str(number) + ") "+ self.name +": "+ self.statString()
	def statString(self):
		return "Total Xp: %d Enemies: %d Multiplier: %dx Adjusted: %d"%(self.totalXp, len(self.enemies), self.multiplier, self.adjusted)
	def difficulty(self):
		for i, val in enumerate(activeParty.xpLimits):
			#print "Checking "+xpLimitNames[i]
			#print "The limit is %d and we are adjusted xp %d"%(val, self.adjusted)
			if self.adjusted <= val:
				#print "We fall into this category"
				return i
			#print "We're too hard for this category"
		#print "Deadly it is"
		return 3
	def difficultyLine(self):
		d = self.difficulty()
		remainingXp = 0 if d == 3 else activeParty.xpLimits[d] - self.adjusted
		return "%s Encounter: %d Adjusted / %d Limit (%d Remaining)"%(xpLimitNames[d], self.adjusted, activeParty.xpLimits[d], remainingXp) 


			
parties = getParties()
activeParty = parties[0]
adventureContext = Adventure()
currentContext = activeParty
command = ""
while command is not "quit":
	args = raw_input("<-|%s|->"%currentContext.getMarker()).split(" ")
	if args[0] == "party" or args[0] == "p":
		currentContext = activeParty
		currentContext.index()
	elif args[0] == "design" or args[0] == "d":
		currentContext = adventureContext
		currentContext.index(args)
	elif args[0] == "add" or args[0] == "a":
		currentContext.add(args)
	elif args[0] == "index" or  args[0] == "list" or  args[0] == "l":
		currentContext.index(args)
	elif args[0] == "delete" or args[0] == "x":
		currentContext.delete(args)
	elif args[0] == "clone" or args[0] == "c":
		currentContext.clone(args)
	elif args[0] == "edit" or args[0] == "e": 
		currentContext = currentContext.edit(args)
		currentContext.index()
	elif args[0] == "levelup" or args[0] == "u": 

	else:
		print command
		print "whuu"

def getParties():
	return [Party()]
#context add delete clone edit save load