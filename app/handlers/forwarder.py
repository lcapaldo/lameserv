import logging
import re
from lamson.routing import route, route_like, stateless
from config.settings import relay, lameserv_endpoint_address
from lamson import view, mail
from lamson.server import SMTPError
from app.model import subscribers, threadcounter

def build_subject(count, original_subject):
    m = re.search(r"^(Re:\s+)\[st (\d+)\](.*)", original_subject, re.I)
    if m is None:
        return "[st %d] %s" % (count, original_subject)
    else:
        return "%s[st %d]%s" % (m.group(1), count, m.group(3))


@route(lameserv_endpoint_address)
def START(message, address=None, host=None):
    subs = subscribers.Subscribers()
    if not subs.is_subscriber(message["From"]):
        return
    
    subj = build_subject(threadcounter.ThreadCounter().count(), message["Subject"])
    
    for sub in subs:
        resp = mail.MailResponse(To=sub, From=message["From"], Subject=subj, Body=message.body())
        resp.attach_all_parts(message)
        resp["Reply-To"] = lameserv_endpoint_address 
        resp["Sender"] = lameserv_endpoint_address
        resp["To"] = lameserv_endpoint_address
        relay.deliver(resp.to_message(), To=sub, From=lameserv_endpoint_address)

@route("(address)@(host)", address=".+")
def NOPE(message, address=None, host=None):
    raise SMTPError(11)
