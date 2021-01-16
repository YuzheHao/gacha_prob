import argparse

def parsing():
	parser = argparse.ArgumentParser(description='manual to this script')
	parser.add_argument('--prob_type', type=str, default='plain')
	parser.add_argument('--init_value', type=float, default=0.02)
	parser.add_argument('--num_persons', type=int, default=1000)
	parser.add_argument('--exp_type', type=str, default='in_100')

	args = parser.parse_args()

	return args