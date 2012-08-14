import logging
from lamson.routing import route, route_like, stateless
from config.settings import relay
from lamson import view


@route("(address)@(host)", address=".+")
def START(message, address=None, host=None):
    return NEW_USER


@route_like(START)
def NEW_USER(message, address=None, host=None):
    return NEW_USER


@route_like(START)
def END(message, address=None, host=None):
    return NEW_USER(message, address, host)


@route_like(START)
@stateless
def FORWARD(message, address=None, host=None):
    subs = open('data/subbers.txt', 'r')
    for sub in subs:
        message['To'] = sub.rstrip("\n\r")
        message['From'] = "lameserv@lameserv.net"
        relay.deliver(message)

@route_like(START)
@stateless
def CHECK_SUB(message, address=None, host=None):
    if "subscribe" in message.body():
        logging.debug("%s@%s wants to subscribe" % (address, host))

