import random

r = random.randint(1, 100)
while True:
	num = input('請猜1-100的數字: ')
	num = int(num)
	if num == r:
		print('答對了!')
		break
	elif num > r:
		print('猜大了')
	elif num < r:
		print('猜小了')