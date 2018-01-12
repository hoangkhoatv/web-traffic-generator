#!/usr/bin/python
# coding: utf-8
import sys, getopt, os
import smtplib
from email.Utils import formatdate
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import Encoders
def main(argv):
	me = ''
	to = ''
	content = ''
	mfile = ''
	try:
		opts, args = getopt.getopt(argv,"hc:m:t:c:f",["me=","to=","content=","file="])
	except getopt.GetoptError:
        	print 'sendMail.py -m <me> -t <to>'
        	sys.exit(2)
    	for opt, arg in opts:
        	if opt == '-h':
            		print 'sendMail.py -m <me> -t <to>'
            		sys.exit()
        	elif opt in ("-m", "--me"):
            		me = arg
        	elif opt in ("-t", "--to"):
            		to = arg
        	elif opt in ("-c", "--content"):
            		content = arg
        	elif opt in ("-f", "--file"):
            		mfile = arg
    	msg = MIMEMultipart()
	msg['From'] = me
	msg['To'] = to
	msg['Subject'] = 'Subject'
	msg['Date'] = formatdate(localtime=True)

	# noi dung email
	msg.attach(MIMEText(content))

	# attachment file setup.rar
	part = MIMEBase('application', "octet-stream")
	part.set_payload( open(mfile,"rb").read() )
	Encoders.encode_base64(part)
	part.add_header('Content-Disposition', 'attachment; filename="%s"'
	               % os.path.basename(mfile))
	msg.attach(part)
	s = smtplib.SMTP('192.168.100.251')
	s.login(me, 'Cnsc12345')
	s.sendmail(me, to, msg.as_string())
	s.quit()
if __name__ == "__main__":
   main(sys.argv[1:])
