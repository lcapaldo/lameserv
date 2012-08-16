import logging
from lamson.routing import route, route_like, stateless
from config.settings import relay
from lamson import view, mail
from app.model import subscribers, threadcounter


@route("lameserv@example.com")
def START(message, address=None, host=None):
    subs = subscribers.Subscribers()
    if not subs.is_subscriber(message["From"]):
        return
    
    subj = "[st: %d] %s" % (threadcounter.ThreadCounter().count(), message["Subject"])
    
    for sub in subs:
        resp = mail.MailResponse(To=sub, From=message["From"], Subject=subj, Body=message.body())
        resp.attach_all_parts(message)
        resp["Reply-To"] = "lameserv@example.com" 
        resp["Sender"] = "lameserv@example.com" 
        relay.deliver(resp.to_message())

