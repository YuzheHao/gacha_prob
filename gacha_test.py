import numpy as np
from random import random
from tqdm import tqdm
import matplotlib.pyplot as plt
from collections import Counter

# keep prob unchanged
def prob_0(idx):
	return 0.02

# change prob after 50
def prob_1(idx):
	if idx <=0 or idx > 100:
		print('ERROR, an invalid index is input.')
	else:
		if idx <= 50:
			return 0.02
		else:
			return 0.02*(idx-50)

def gacha_hit_0(idx):
	threshold = prob_0(idx)
	gacha_value = random()
	if gacha_value < threshold:
		return True
	else:
		return False 

def gacha_hit_1(idx):
	threshold = prob_1(idx)
	gacha_value = random()
	if gacha_value < threshold:
		return True
	else:
		return False 

# Paras for the gacha test
persons_0 = []
hits_0 = []
persons_1 = []
hits_1 = []

epoch = 10000

for person_id in tqdm(range(epoch)):
	for gacha_id in range(1,500):
		value_now = gacha_hit_0(gacha_id)
		if value_now:
			persons_0.append(person_id)
			hits_0.append(gacha_id)
			break

for person_id in tqdm(range(epoch)):
	for gacha_id in range(1,102):
		value_now = gacha_hit_1(gacha_id)
		if value_now:
			persons_1.append(person_id)
			hits_1.append(gacha_id)
			break

y0 = list(Counter(hits_0).values())
y1 = list(Counter(hits_1).values())

plt.grid()
plt.plot(range(len(y0)), y0, color='deepskyblue', alpha=0.5)
plt.plot(range(len(y1)), y1, color='orange', alpha=0.5)
plt.show()


