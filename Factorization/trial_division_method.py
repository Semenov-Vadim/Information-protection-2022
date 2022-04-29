import math


def trial_division(x):
	y = 2
	while y <= math.sqrt(x):
		if x % y == 0:
			return y
		y += 1
	return 1


if __name__ == '__main__':
	number = 113
	print(trial_division(number))
