
x = 3
while x > 0:
	password = input('請輸入密碼')

	if password != 'a123456' and x > 1:
		print('密碼錯誤 請重新輸入 還有', x - 1, '次機會' )
		x = x - 1

	elif password != 'a123456' and x <= 1:
		print('登入失敗')
		x = x - 1
		break


	elif password == 'a123456':
		print('登入成功')
		break







