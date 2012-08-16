from email.utils import parseaddr

class Subscribers:
  def __init__(self):
      subs = open('data/subbers.txt', 'r')
      self._subs = set()
      for sub in subs:
          self._subs.add(sub.rstrip("\r\n"))
      subs.close()
  
  def is_subscriber(self, addr):
      return parseaddr(addr.lower())[1] in self._subs
  
  def __iter__(self):
    for sub in self._subs:
        yield sub

  
      
    
