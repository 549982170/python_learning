from twisted.internet.defer import Deferred
 
def myCallback(result):
    print result
 
d = Deferred()
d.addCallback(myCallback)
d.callback("Triggering callback.")


from twisted.internet.defer import Deferred
def func(x): print x
d = Deferred()
d.addCallbacks(func, func)
d.callback('First fire')
d.callback('Second fire')