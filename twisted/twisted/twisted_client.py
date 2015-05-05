from twisted.internet.protocol import Protocol,ClientFactory
from twisted.internet import reactor
class Echo(Protocol):
    def connectionMade(self):
        self.transport.write("hi,server")
        
    def dateReceived(self):
        print date
        
class EchoClientFactory(ClientFactory):
    def startedConnecting(self,connector):
        print "connection starting..."
    def buildProtocol(self,addr):
        print addr
        return Echo()
    def clientConnectionLost(self,connector,reason):
        print "lose reason:",reason
    def clientConnectionFailed(self,connector,reason):
        print "faild reason:",reason
def fun():
    print 'calllater'

reactor.connectTCP('115.24.161.139',8001,EchoClientFactory())
reactor.run()