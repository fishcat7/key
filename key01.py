import random

r = random.randint(1, 10)
while True:
	num = input('請猜一個數字:')
	num = int(num)
	if num == r:
		print('猜對了!')
		break
	elif num > r:
		print('猜錯了,比答案大')
	elif num < r:
		print('猜錯了,比答案小')
