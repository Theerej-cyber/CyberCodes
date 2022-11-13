import paramiko
import optparse

def connection(client,host,user,password):
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(host,username= user,password= password)

def Command_Execution(client,command):
	ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command(command)
	return ssh_stdout
def main():
	parser = optparse.OptionParser("Usage % program : SSHBotNet -H <Host> -U <User> -P <Password> -C commands")
	parser.add_option('-H',dest='host',type='string',help="HostName")
	parser.add_option('-U',dest='user',type='string',help='User')
	parser.add_option('-P',dest='passw',type='string',help='Password')
	(options,args) = parser.parse_args()
	host = options.host
	user = options.user
	password = options.passw	
	client = paramiko.SSHClient()
	if(host==None)|(user==None):
	    print(parser.usage)
	    exit(0)
	connection(client,host,user,password)
	willingness = input("Are you willing to execute commands(yes/no): ")
	flag = 0
	if willingness == 'y':
		flag = 1 
	while flag == 1:
		command = input("Enter the command you want to execute: ")
		if command == 'exit':
			print("Exiting the Program")
			exit(0)
		results = Command_Execution(client,command)
		for line in results:
			print(line)
		print("********End of command********")
		

if __name__ == '__main__':
	main()



