from twisted.internet import reactor
from twisted.internet.protocol import Factory,Protocol
class Echo(Protocol):
    def connectionMade(self):
        self.transport.write("hi,welcome")
        #self.transport.loseConnection()
    def dateReceived(self):
        print date
        self.transport.write("haha:"+data)
factory=Factory()
factory.protocol=Echo
reactor.listenTCP(8001,factory)
reactor.run()