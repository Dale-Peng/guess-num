import random
start = input('請決定最小值:')
end = input('請決定最大值:')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0
while True:
	count += 1  # count = count + 1 (快寫法)
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('答對了!')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
		print('猜大了')
	elif num < r:
		print('猜小了')
	print('這是你猜的第', count, '次')