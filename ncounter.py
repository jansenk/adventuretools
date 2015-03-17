#!python
#Number of Monsters XP Multiplier
from collections import namedtuple 
xpMultiplier = [0, 1, 1.5, 2, 2, 2, 2, 2.5, 2.5, 2.5, 2.5, 3, 3, 3, 3]; 4
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

Player = namedtuple('Player', ['level', 'name'])
Enemy = namedtuple('Enemy', ['level', 'name'])
class blankContext():
	def index(self):
		print "nyi"	
	def add(self):
		print "nyi"	
	def delete(self):
		print "nyi"	
	def clone(self):
		print "nyi"	
	def edit(self, input):
		print "Invalid command"
	def save(self, input):
		print "nyi"
	def load(self, input):
		print "nyi" 
	def getMarker(self):
		return "O"
		
class Context():
	def __init__(self):
		self.components = []
	def index(self):
		print self.getTitle()
		for i, component in enumerate(self.components):
			print component.listString(i)
		self.printSummaryString()
	def indexBasedOperation(self, operation, arg):
			target = self.demandId(arg);
			if target > 0 and target <= len(self.components):
				return operation(self.components, self.components[target-1])
	def delete(self, arg):
			self.indexBasedOperation((lambda l c: del c), arg)
	def clone(self, arg):
			self.indexBasedOperation((lambda l c: l.append(self.makeComponent(c))), arg)
	def edit(self, arg):
			self.indexBasedOperation((lambda l c: ))
	def demandId(self, arg):
		if type(" ") == type(arg) and arg.isdigit():
			return int(arg)
		else:
			while not parsed:
				try:
					x = int(raw_input('ID: '))
					parsed = True # we only get here if the previous line didn't throw an exception
				except ValueError:
					print 'Invalid value!'
			return x

class Party():
	def __init__(self, verbose=False):
		self.verbose = verbose
		self.players = []
		self.xpLimits = [0, 0, 0, 0]
	def index(self):
		print "Players:"
		for i, player in enumerate(self.players):
			print "%d) %s level %d"%(i+1, player.name, player.level)
		print "-------------------------------"
		print "Party XP limits: Easy %d Medium: %d Hard: %d Deadly: %d"%tuple(self.xpLimits)
	def add(self):
		name = raw_input("Name: ")
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
	def delete(self):
		target = int(raw_input("id: "))
		if target and target > 0  and target <= len(self.players):
			del self.players[target-1]
			self.calcXpLimits()
		else:
			print "Invalid Index"
	def clone(self):
		target = int(raw_input("id: "))
		if target > 0  and target <= len(self.players):
			targetPlayer = self.players[target-1]
			self.players.append(Player(targetPlayer.level, targetPlayer.name))
		else:
			print "Invalid Index"
	def edit(self, input):
		print "Invalid command"
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
			
class Adventure():
	def __init__(self, players=None):
		self.encounters = []
		if players is None:
			self.players = Adventure()
		else:
			self.players = players
	def index(self):
		print "Encounters: "
		for i, encounter in enumerate(self.encounters):
			print encounter.descriptionString(i+1)+""
	def add(self):
		name = raw_input("Name: ")
		if not name:
			name = "encounter"
		encounters.append(Encounter(level, name))
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
		if target and target > 0  and target < len(self.encounters):
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
	def __init__(self, players=None):
		self.encounters = []
		if players is None:
			self.players = Adventure()
		else:
			self.players = players
	def index(self):
		print "Encounters: "
		for (i, encounter) in (range(1, len(self.encounters + 1)), self.encounters):
			print encounter.descriptionString(i)+""
	def add(self, input):
		name = raw_input("Name: ")
		if not name:
			name = "encounter"
		encounters.append(Encounter(level, name))
	def delete(self):
		target = int(raw_input("id: "))
		if target and target > 0  and target < len(self.encounters):
			del self.encounters[target]
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
		if target and target > 0  and target < len(self.encounters):
			return self.encounters[target]
		else:
			print "Invalid Index" 
			return self
	def save(self, input):
		print "nyi"
	def load(self, input):
		print "nyi"
	def getMarker():
		return "E"

currentContext = blankContext()
partyContext = Party()
adventureContext = Adventure(partyContext)
command = ""
while command is not "quit":
	command = raw_input("<-|%s|->"%currentContext.getMarker())
	if command == "party":
		currentContext = partyContext
	elif command == "encounters":
		currentContext = adventureContext
	elif command == "add":
		currentContext.add()
	elif command == "index":
		currentContext.index()
	elif command ==	"delete":
		currentContext.delete()
	elif command == "clone":
		currentContext.clone()
	elif command == "edit": 
		currentContext.edit()
	else:
		print command
		print "whuu"
#context add delete clone edit save load