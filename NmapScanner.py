import nmap
import optparse

def nmapScanner(trgHost,trgPort):
	try:
		scan = nmap.PortScanner()
		scan.scan(trgHost,trgPort)
		state = scan[trgHost]['tcp'][int(trgPort)]['state']
		print(" * "+trgHost+" "+trgPort+" " + state)
	except:
		print("Host Not Found: "+trgHost)

def main():
	parser = optparse.OptionParser("Usage : NmapScanner -t target -p ports")
	parser.add_option('-t',dest='target',type='string',help='Target Host')
	parser.add_option('-p',dest='port',type='string',help='Target ports')
	(options,args) = parser.parse_args()
	trgHost=options.target
	trgPort=str(options.port).split(',')
	if (trgHost==None)|(trgPort==None):
		print(par.usage)
		exit(0)

	for port in trgPort:
		nmapScanner(trgHost,port)
if __name__ == '__main__':
	main()