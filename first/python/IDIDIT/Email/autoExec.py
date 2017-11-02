import sendMessage
import datetime, os, platform,time
# 算了，根本不能用，骗子。。

def autoExec(sche_time):
	flag = 0
	while True:
		now = datetime.datetime.now()
		# print(now)
		if now == sche_time:
			print('hello')
			# s = sendMessage.send()
			# s.run()
			flag = 1
		else:
			if flag == 1:
				sche_time = sche_time + datetime.timedelta(munites = 1)
				print(sche_time)
				flag = 0

if __name__ == '__main__':
	s = sendMessage.send()
	s.run()
	sche_time = datetime.datetime(2017,10,27,20,27,10)
	print(sche_time)
	print(datetime.datetime.now())
	autoExec(sche_time)