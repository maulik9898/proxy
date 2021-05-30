import os

from twisted.web import proxy, http

from twisted.internet import reactor

from twisted.python import log

import sys

log.startLogging(sys.stdout)

print(os.getenv('PORT',8080) )

class ProxyFactory(http.HTTPFactory):

 protocol = proxy.Proxy



reactor.listenTCP(os.getenv('PORT',8080), ProxyFactory( ))

reactor.run( )
