#-*- coding:utf-8 -*-
import xmpp
server = ('183.56.157.196', 5222) 
user = '16'

passwd = '9cc3ef0d1d3863ba0f896a1963a797ce'

touser="20"
domain = 'moxiancn.com'

class Bot:
    """ Jabber Bot Base Class """
    JID = ''
    PASSWORD = ''
 
    client = None  
 
    def __init__ (self, jid, password):
        self.JID = xmpp.JID(jid)
        self.PASSWORD = password
 
        self.login()
 
    def login (self):         
        self.client = xmpp.Client(domain, debug=[])
        if not self.client.connect(server) :
            raise IOError('JabberBot not connected.')
        if not self.client.auth(str(self.JID) , self.PASSWORD):
            raise IOError('JabberBot authentication failed.')
         
        self.client.RegisterHandler('message', self.message_callback)
        self.client.RegisterHandler('presence', self.presence_callback)
        self.client.sendInitPresence()

    def presence_callback (self, client, message):
        """ 默认事件回调,包括下面几个(可通过继承自定义) """
        type = message.getType()
        who = message.getFrom().getStripped()

    def send (self, jid, message):
        """ 发消息给某人"""
        attrs = {"id":"G766K-19"}
        message_tmp = xmpp.protocol.Message(jid, message,typ="chat",attrs=attrs)
        # print dir(message_tmp)
        message_tmp.setTagData('mx',"")
        message_tmp.setTagAttr('mx',"xmlns","urn:xmpp:mx")
        message_tmp.setTagAttr('mx',"v","request")
        message_tmp.setTagAttr('mx',"id","G766K-19")
        print "\r\n"
        print "send:",message_tmp
        return  self.client.send(message_tmp)
 
    def step (self):
        """ 用在循环中 """
        try:
            self.client.Process(1)
            
        except KeyboardInterrupt:   # Ctrl+C停止
            return False
        return True
 
 
#===========================
# 测试
#===========================
class Bot(Bot):
    def message_callback (self, cl, msg):
        fromid = msg.getFrom().getStripped()
        cont = msg.getBody()
        print "\r\n"
        print "receive:",msg
 
    def send2admin (self, message):
        return self.send(touser+'@'+domain, message)
 
if __name__ == '__main__':
    gb = Bot (user, passwd)

 
    # 开始运行
    while (gb.step()): pass
