from random import randint, shuffle


class Creature:
	def __init__(self, name, hit_points = 10):
		self.name = name
		self.hp = hit_points * 10
		self.damage = 2

	def __repr__(self):
		return self.name

	def attack(self, target):
		result = self.damage + randint(1,5)
		print(f'{self.name} hits {target} for {result} damage')
		return result

	def take_damage(self, damage):
		self.hp = self.hp-damage
		print(f'{self.name} has {self.hp} left')

	def is_alive(self):
		alive = self.hp > 0
		if not alive: 
			print('Oh no!', self.name, 'dies.')
		return alive


class Game:
	def __init__(self):
		self.monsters = [Creature(title) for title in ['Joe', 'Your Mom']]
		self.battle_on = True
		self.turn = 0
		self.loop()

	def count_turn(self):
		self.turn+=1
		print('\nTurn:', self.turn)

	def loop(self):
		self.count_turn()
		orks = self.monsters[:]
		shuffle(orks)
		for num in range(len(orks)):
			self.battle_on = self.fight(orks, num)
			if not self.battle_on: 
				return
		if self.battle_on: 
			self.loop()

	def fight(self, creature_list, number):
			attacker = creature_list[number]
			victim = creature_list[number-1]
			dmg = attacker.attack(victim)
			victim.take_damage(dmg)
			return victim.is_alive()

my_game = Game()

