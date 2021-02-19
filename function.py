import requests
import json
#author: Kira

# timeOld = time.time()
# startTime = time.time()
# timeNow = time.time()
# cookies = {'PHPSESSID': 'jcim27i797r8n1j0e5ls6vmu9p'}

username="B16DCCN057"
urlformat = "http://qldt.ptit.edu.vn/default.aspx?page=thoikhoabieu&sta=0&id="

print("running...")	
# for i in range (200,600):
# 	username="B16DCCN{0:03}".format(i)
# 	for line in Lines: 
# 		payload = { "username":username, "password":line.strip()}
# 		# print(payload)
# 		x = requests.post(url=url, json=payload)
# 		if( x.status_code == 200):
# 			print("username: ",username,"password:",line)
flag='ctl00_ContentPlaceHolder1_ctl00_lblContentTenSV" class="Label" style="color:Teal;font-weight:bold;">'
for i in range (1,58):
	MSV="B16DCCN{0:03}".format(i) # zfill( len )
	url=urlformat+MSV
	x = requests.get(url=url)
	t=x.text.find('ctl00_ContentPlaceHolder1_ctl00_lblContentTenSV')
	if( t == -1):
		pass
	else:
		e=x.text.find("</font>",t)
		# print(x.text)
		print(MSV)
		# print(x.text[t+85:e])
		arr=x.text[t+85:e].split("-")
		print(arr[0].strip())
		print(arr[1][11:])
		t=x.text.find('ctl00_ContentPlaceHolder1_ctl00_lblLop" class="Label"><font color="Gray"> - ')
		e=x.text.find("</font></b></span>",t)
		
		# print(x.text[t+190:e])
		arr=x.text[t+190:e].split("-")
		print(arr[0].strip())
		print(arr[1][8:].strip())
		print(arr[2][7:].strip())



