import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
# from email.utils import parseaddr, formataddr

class send(object):

	def run(self):
		sender = "1239842226@qq.com"
		license  = "pyemyskkuoxigegj"         # 授权码不是邮箱密码
		receivers   = "623489699@qq.com" 

		msg = MIMEText("这个是写给定时的..\n不过好像失败了")
		msg["Subject"] = Header("emmm", 'utf-8')    # 包含中文用Header对象进行编码
		msg["From"]    = Header(sender, 'utf-8')
		msg["To"]      = Header(receivers, 'utf-8')

		"""
		好像 不用header也行？
		msg['Subject'] = "hai"
		msg['From'] = sender
		msg['To'] = receivers

		"""

		try:
		    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
		    s.login(sender, license)
		    s.sendmail(sender, receivers, msg.as_string())
		    s.quit()
		    print ("Success!")
		except smtplib.SMTPException:
		    print ("Falied,%s"%e)

class sendPureText(object):

	def run(self):
		sender = "1239842226@qq.com"
		license  = "pyemyskkuoxigegj"         # 授权码不是邮箱密码
		receivers   = "623489699@qq.com" 

		msg = MIMEText("发送纯文字")
		msg["Subject"] = Header("Noreply", 'utf-8')    # 包含中文用Header对象进行编码
		msg["From"]    = Header(sender, 'utf-8')
		msg["To"]      = Header(receivers, 'utf-8')

		"""
		好像 不用header也行？
		msg['Subject'] = "hai"
		msg['From'] = sender
		msg['To'] = receivers

		"""

		try:
		    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
		    s.login(sender, license)
		    s.sendmail(sender, receivers, msg.as_string())
		    s.quit()
		    print ("Success!")
		except smtplib.SMTPException:
		    print ("Falied,%s"%e)										

class sendHtmlText(object):

	def run(self):
		sender = "1239842226@qq.com"
		license  = "pyemyskkuoxigegj"         # 授权码不是邮箱密码
		receivers   = "623489699@qq.com" 

		# msg = MIMEText("要开始每天发邮箱喽")
		html = '<html><body><h1>emmmmm....</h1>' +\
    			'<p>	send by <a href="http://www.python.org">Python</a>...</p>' +\
    			'</body></html>'
		msg = MIMEText(html, 'html', 'utf-8')
		msg["Subject"] = Header("emmm", 'utf-8')    # 包含中文用Header对象进行编码
		msg["From"]    = Header(sender, 'utf-8')
		msg["To"]      = Header(receivers, 'utf-8')

		"""
		好像 不用header也行？
		msg['Subject'] = "hai"
		msg['From'] = sender
		msg['To'] = receivers

		"""

		try:
		    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
		    s.login(sender, license)
		    s.sendmail(sender, receivers, msg.as_string())
		    s.quit()
		    print ("Success!")
		except smtplib.SMTPException:
		    print ("Falied,%s"%e)	

class sendAnnexes(object):

	# 图片可以作为附件发，也可以内嵌需要额外设定
	def run(self):
		sender = "1239842226@qq.com"
		license  = "pyemyskkuoxigegj"         # 授权码不是邮箱密码
		receivers   = "623489699@qq.com" 

		# msg = MIMEText("要开始每天发邮箱喽")
		
		msg = MIMEMultipart()
		html = '<html><body><h1>zz....</h1>' +\
				'<p><img src = "cid:0"></p>' +\
    			'<p>	send by <a href="http://www.python.org">Python</a>...</p>' +\
    			'</body></html>'
    	# 用MIMEText对象构造正文
		msg.attach(MIMEText(html, 'html', 'utf-8'))

		# 用MIMEBase对象构造附件
		with open('annexes.png', 'rb') as f:
			# 设置附件的MIME和文件名，这里是png类型:
			mime = MIMEBase('image', 'png', filename='annexes.png')
			# 加上必要的头信息:
			mime.add_header('Content-Disposition', 'attachment', filename='annexes.png')
			mime.add_header('Content-ID', '<0>')
			mime.add_header('X-Attachment-Id', '0')
			# 把附件的内容读进来:
			mime.set_payload(f.read())
			# 用Base64编码:
			encoders.encode_base64(mime)
			# 添加到MIMEMultipart:
			msg.attach(mime)

		msg["Subject"] = Header("emmm", 'utf-8')    # 包含中文用Header对象进行编码
		msg["From"]    = Header(sender, 'utf-8')
		msg["To"]      = Header(receivers, 'utf-8')

		"""
		好像 不用header也行？
		msg['Subject'] = "hai"
		msg['From'] = sender
		msg['To'] = receivers

		"""

		try:
			# gmail的smtp
			# smtp_server = 'smtp.gmail.com'
			# smtp_port = 587
			# s = smtplib.SMTP(smtp_server, smtp_port)
		    

			# qq的smtp
		    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
		    s.login(sender, license)
		    s.sendmail(sender, receivers, msg.as_string())
		    s.quit()
		    print ("Success!")
		except smtplib.SMTPException:
		    print ("Falied,%s"%e)	


# send().run()
# sendPureText().run()
# sendHtmlText().run()
# sendAnnexes().run()
# 		