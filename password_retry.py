password = 'a123456'
x = 3 #剩餘機會
while True:
	pwd = input('請輸入密碼: ')
	if pwd == password:
		print('登入成功!') 
		break #逃出迴圈
	else: 
		x =  x - 1
		print('密碼錯誤! 還有' ,x, '次機會')
		if x == 0:
			break