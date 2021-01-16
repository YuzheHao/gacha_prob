from gacha import Gacha
from collections import Counter
from tqdm import tqdm


class Experiment():
	def __init__(self, args):
		self.gacha = Gacha(args)
		self.exp_type = args.exp_type
		self.num_persons = args.num_persons
		self.result = None
		print('Experiment parameters:')	
		print('* <exp_type>: %s' % self.exp_type)
		print('* <num_persons>: %d' % self.num_persons)
		print('+++++++++++++++++++++++++')

	def run(self):
		hits = []
		# each loop is an independent gacha process
		for person_id in range(self.num_persons):
		# for person_id in tqdm(range(self.num_persons)):

			# 100 times gacha for one peroson
			if self.exp_type == 'in_100':
				for gacha_id in range(1,101):
					if self.gacha.hit(gacha_id):
						hits.append(gacha_id)
						break # go to next person after hitting
			
			# keep gaching until hit!
			elif self.exp_type == 'until_hit':
				gacha_id = 1
				while(not self.gacha.hit(gacha_id)):
					gacha_id += 1
				hits.append(gacha_id)

			else:
				print('ERROR, an invalid exp_type is input.')

		self.result = hits

	def explain(self):
		if not self.result:
			print("ERROR, the experiment haven't been run.")
		else:
			keys, values = [], []
			hit_in_50 = 0
			for i in sorted(Counter(self.result)): 
				keys.append(i)
				values.append(Counter(self.result)[i])
				if i <= 50:
					hit_in_50 += Counter(self.result)[i]


			print('Result:')
			print('* <# of no-hit-people>: %d' % (self.num_persons-len(self.result)))
			print('* <%% of no-hit>: %f' % ((self.num_persons-len(self.result))/self.num_persons))
			print('* <%% of hit-in-50>: %f' % (hit_in_50/self.num_persons))
			print('* <average hit-#th>: %f' % (sum(self.result)/self.num_persons))
			print('+++++++++++++++++++++++++')

			return keys, values




