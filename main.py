from para import parsing
from experiment import Experiment

import sys
sys.path.insert(0,'/Users/Yuzhe/Documents/projects/peanuts/amiya/')
import amiya

if __name__ == '__main__':

	args = parsing()
	exp_0 = Experiment(args)
	exp_0.run()

	args.prob_type = 'relu'
	exp_1 = Experiment(args)
	exp_1.run()

	key0, value0 = exp_0.explain()
	key1, value1 = exp_1.explain()

	keys = [key0, key1]
	values = [value0, value1]

	amiya.magic_draw(values,
					 x=keys,
					 x_label="hit at #",
					 y_label="# of people",
					 legend=['plain model','relu model'],
					 title='experiment: until_hit')