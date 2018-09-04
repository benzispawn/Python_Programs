import optparse
import socket
from socket import *
from threading import *

screenLock = Semaphore(value=1)

def connScan(tgtHost, tgtPort):
                  try:
                                    connSkt = socket(AF_INET, SOCK_STREAM)
                                    connSkt.connect((tgtHost, tgtPort))
                                    connSkt.send('ViolentPython\r\n')
                                    results = connSkt.recv(100)
                                    screenLock.acquire()
                                    print '[+]%d/tcp open' % tgtPort
                                    print '[+]' + str(results)
                  except:
                                    screenLock.acquire()
                                    print '[-]%d/tcp closed' % tgtPort
                  finally:
                                    screenLock.relese()
                                    connSkt.close()

def portScan(tgtHost, tgtPort):
                  try:
                                    tgtIP = gethostbyname(tgtHost)
                  except:
                                    print "Cannot resolve '%s': Unknow host" % tgtHost
                                    return
                  try:
                                    tgtName = gethostbyaddr(tgtIP)
                                    print '\n[+] Scan Results for:' + tgtName[0]
                  except:
                                    print '\n[+] Scan Results for:' + tgtIP
                  setdefaulttimeout(1)
                  for tgtPort in tgtPorts:
                                    t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
                                    t.start()
def main():
                  parser = optparse.OptionParser('usage%prog'+\
                                                 '-H <target host> -p <target port>')
                  parser.add_option('-H', dest='tgtHost', type='string',\
                                    help='specify target host')
                  parser.add_option('-p', dest='tgtPort', type='string',\
                                    help='specify target port[s] separated by comma')
                  (options, args) = parser.parse_args()
                  tgtHost = options.tgtHost
                  tgtPort = str(options.tgtPort).split('.')
                  if (tgtHost == None) | (tgtPort[0] == None):
                                    print parser.usage
                                    exit(0)
if __name__ == '__main__':
                  main()
