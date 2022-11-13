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
	parser.add_option('-C',dest='commands',type='string',help='Commands')
	(options,args) = parser.parse_args()
	host = options.host
	user = options.user
	password = options.passw
	commands = str(options.commands).split(',')
	client = paramiko.SSHClient()
	if(host==None)|(user==None):
	    print(parser.usage)
	    exit(0)
	connection(client,host,user,password)
	for command in commands:
		results = Command_Execution(client,command)
		for line in results:
			print(line)
		print("********End of command********")

if __name__ == '__main__':
	main()




