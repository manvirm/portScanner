from socket import *

def conScan(tgtHost, tgtPort):
    # Establish tcp connection
    try:
        connskt = socket(AF_INET, SOCK_STREAM)
        connskt.connect((tgtHost, tgtPort))
        print(f'Connection open: Port {tgtPort}')
        connskt.close()
    except:
        print(f'Connection closed: Port {tgtPort}')

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP =gethostbyname(tgtHost)
    except:
        print(f'Cannot resolve: Port {tgtPort}')
        return

    try:
        tgtName = gethostbyaddr(tgtIP)
        print(f'Scan result of: {tgtName[0]}')
    except:
        print(f'Scan result of: {tgtIP}')

    setdefaulttimeout(1)
if __name__ == '__main__':
    conScan('216.58.207.238', 22)
