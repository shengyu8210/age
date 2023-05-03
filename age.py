driving = input('請問你有沒有開過車?')
if driving != '有' and driving != '沒有':
	print('請輸入有/沒有！')
	raise SystemExit
age = input('請問你的年齡?')
age = int(age)

if driving == '有':
	if age >= 18: 
		print('你通過測驗啦!')
	else:
		print('奇怪！你怎麼可以開車呢?')
elif driving == '沒有':
	if age >= 18:
		print('你怎麼還不去學開車呢?')
	else:
		print('再過幾年你就可以去學開車囉！')

