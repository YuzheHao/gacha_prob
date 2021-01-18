from tqdm import tqdm
from random import random

class Gacha:
	def __init__(self, args):
		self.prob_type = args.prob_type
		self.init_value = args.init_value
		print('+++++++++++++++++++++++++')
		print('Gacha model is built:')
		print('* <prob_type>: %s' % self.prob_type)
		print('* <init_value>: %f' % self.init_value)
		print('+++++++++++++++++++++++++')


	def plain(self, num_th):
		return self.init_value

	def relu(self, num_th):
		if num_th <= 50:
			return 0.02
		elif num_th > 100:
			return 1
		else:
			return 0.02*(num_th-50)

	def hit(self, num_th):
		if num_th <=0:	
			print('ERROR, an invalid index is input.')
			return

		gacha_value = random()
		if self.prob_type == 'plain':
			threshold = self.plain(num_th)
		elif self.prob_type == 'relu':
			threshold = self.relu(num_th)
		else:
			print('ERROR, an invalid prob_type is input.')


		hit = (gacha_value<=threshold)

		return hit