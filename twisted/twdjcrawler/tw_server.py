from twisted.internet import reactor
from twisted.internet.protocol import Factory,Protocol
import sys
import os
sys.path.insert(0,r"C:\django\twdjcrawler")
from django.conf import settings
os.environ['DJANGO_SETTINGS_MODULE']="twdjcrawler.settings"
from django.db.models.loading import get_models
loaded_models=get_models()
from cralwer.models import Task
tasks=[]
def get_tasks():
    tks=Task.objects.filter(status=0)
    tasks.extend(tks)
    print tasks
    
class SendTask(Protocol):
    def connectionMade(self):
        self.transport.write("hi,welcome")
    def dataReceived(self, data):
        print data
        self.transport.write("haha:"+data)
factory=Factory()
factory.protocol=SendTask
reactor.callLater(1,get_tasks)
reactor.listenTCP(8001,factory)
reactor.run()