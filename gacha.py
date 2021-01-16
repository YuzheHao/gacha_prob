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













# # Paras for the gacha test
# persons_0 = []
# hits_0 = []
# persons_1 = []
# hits_1 = []

# epoch = 10000

# for person_id in tqdm(range(epoch)):
# 	for gacha_id in range(1,500):
# 		value_now = gacha_hit_0(gacha_id)
# 		if value_now:
# 			persons_0.append(person_id)
# 			hits_0.append(gacha_id)
# 			break

# for person_id in tqdm(range(epoch)):
# 	for gacha_id in range(1,102):
# 		value_now = gacha_hit_1(gacha_id)
# 		if value_now:
# 			persons_1.append(person_id)
# 			hits_1.append(gacha_id)
# 			break

# y0 = list(Counter(hits_0).values())
# y1 = list(Counter(hits_1).values())

# plt.grid()
# plt.plot(range(len(y0)), y0, color='deepskyblue', alpha=0.5)
# plt.plot(range(len(y1)), y1, color='orange', alpha=0.5)
# plt.show()


