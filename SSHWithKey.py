IP = input("Enter host_server IP: ").split()
username = input("Enter username: ").split()


#create a file on host_server for fil
import paramiko
import os
privatekeyfile = os.path.expanduser('~/.ssh/known_hosts')
mykey = paramiko.RSAKey.from_private_key_file(privatekeyfile)
ssh.connect(IP[0], username = user[0], pkey = mykey)