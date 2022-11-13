from socket import *
import optparse
from threading import Thread
from threading import Semaphore
lock = Semaphore(value=1)
def connScan(trgHost,trgPort):
    try:
        soc = socket(AF_INET,SOCK_STREAM)
        soc.connect((trgHost,trgPort))
        soc.send("HelloMan".encode())
        result = soc.recv(100)
        print("TCP open: %d"%trgPort)
        print("Results for this port"+str(result))

    except:
        lock.acquire()
        print("Tcp is closed: %d"%trgPort)

    finally:
        lock.release()
        soc.close()

def portScan(trgHost,trgPorts):
    try:
        trgIp = gethostbyname(trgHost)
    except:
        print("Host Not Found: "+trgHost)

    try:
        trgName = gethostbyaddr(trgIp)
        print("Scan results for:"+trgName[0])
    except:
        print("Scan results for:"+trgIp)
    setdefaulttimeout(1)
    for ports in trgPorts:
        print("Scanning port: "+ports)
        t = Thread(target=connScan,args=(trgHost,int(ports)))
        t.start()
def main():
    parser = optparse.OptionParser("usage %prog :-H+<targetHost -P <target Port>")

    parser.add_option('-H',dest='hostname',type='string',help='give correct host name')
    parser.add_option('-P',dest='portnumber',type='string',help='give perfext port number')
    (options, args) = parser.parse_args()
    trgHost = options.hostname
    trgPort = options.portnumber
    trgPorts = str(options.portnumber).split(',')
    if(trgPort==None)|(trgHost==None):
        print(parser.usage)
        exit(0)
    portScan(trgHost,trgPorts)
if __name__ == '__main__':
    main()