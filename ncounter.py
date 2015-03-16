#!python
#Number of Monsters XP Multiplier
Single Monster —
Pair (2 monsters) × 1.5
Group (3-6 monsters) × 2
Gang (7-10 monsters) × 2.5
Mob (11-14 monsters) × 3
Horde (15 or more monsters) × 4
xpLimits = [[25, 50, 75, 100],
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
Enemy = namedtuple('Enemy', ['level', 'name'])]

class Party():
	def __init__(self):
		self.players = []
		self.xpLimits = [0, 0, 0, 0]
	def index(self):
		print "Players:\n"
		for (i, player) in (range(1, len(self.players + 1)), self.players):
			print "%d) %s level %d\n"%(i, player.name, player.level)
		print "-------------------------------\n"
		print "Party XP limits: Easy %d Medium: %d Hard: %d Deadly: %d\n"%self.xpLimits	
	def add(self, input):
		name = input("Name: ")
		if not name:
			name = "player"
		while 1:
			level = int(input("Level: "))
			if level and level >= 1 and level <= 20:
				break
			else
				print "must be 1-20\n"
		players.append(Player(level, name))
	def delete(self, input):
		target = int(input)
		if target and target > 0  and target < len(self.players):
			del self.players[target]
		else:
			print "Invalid Index\n"
	def clone(self, input):
		target = int(input)
		if target and target > 0  and target < len(self.players):
			targetPlayer = self.players[target]
			self.players.append(Player(targetPlayer.level, targetPlayer.name))
		else:
			print "Invalid Index\n"
	def edit(self, input):
		print "Invalid command\n"
	def save(self, input):
		print "nyi"
	def load(self, input):
		print "nyi"
	def calcXpLimits(self):
		limits = [0, 0, 0, 0]
		for p in self.players:
			for i in range(0, 4):
				limits[i] += xpLimitTable[p.level - 1][i]
		self.xpLimits = limits
			
class Adventure():
	def __init__(self, players=None):
		self.encounters = []
		if players is None:
			self.players = Adventure()
		else:
			self.players = players
	def index(self):
		print "Encounters: "
		for (i, encounter) in (range(1, len(self.encounters + 1)), self.encounters):
			print encounter.descriptionString(i)+"\n"
	def add(self, input):
		name = input("Name: ")
		if not name:
			name = "encounter"
		encounters.append(Encounter(level, name))
	def delete(self, input):
		target = int(input)
		if target and target > 0  and target < len(self.encounters):
			del self.encounters[target]
		else:
			print "Invalid Index\n"
	def clone(self, input):
		target = int(input)
		if target and target > 0  and target < len(self.encounters):
			self.encounters.append(Encounter(self.encounters[target])
		else:
			print "Invalid Index\n" 
	def edit(self, input):
		target = int(input)
		if target and target > 0  and target < len(self.encounters):
			return self.encounters[target]
		else:
			print "Invalid Index\n" 
			return self
	def save(self, input):
		print "nyi"
	def load(self, input):
		print "nyi"
	
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
			print encounter.descriptionString(i)+"\n"
	def add(self, input):
		name = input("Name: ")
		if not name:
			name = "encounter"
		encounters.append(Encounter(level, name))
	def delete(self, input):
		target = int(input)
		if target and target > 0  and target < len(self.encounters):
			del self.encounters[target]
		else:
			print "Invalid Index\n"
	def clone(self, input):
		target = int(input)
		if target and target > 0  and target < len(self.encounters):
			self.encounters.append(Encounter(self.encounters[target])
		else:
			print "Invalid Index\n" 
	def edit(self, input):
		target = int(input)
		if target and target > 0  and target < len(self.encounters):
			return self.encounters[target]
		else:
			print "Invalid Index\n" 
			return self
	def save(self, input):
		print "nyi"
	def load(self, input):
		print "nyi"

currentContext = blankContext()
players = Party()
adventure = Adventure(players)
while command is not "quit":
	command = input("<-|->")
	if command is "party":
	elif command is "encounters":
	elif command is "add":
	elif command is	"delete":
	elif command is "clone":
	elif command is "edit": 

//context add delete clone edit save load