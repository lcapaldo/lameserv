class ThreadCounter:
     def __init__(self):
         # this is less racey than it looks
         f = open('data/threadcount.txt', 'r')
         l = f.readline().rstrip("\r\n")
         self._count = int(l) + 1
         f.close()
         f = open('data/threadcount.txt', 'w')
         f.write(str(self._count))
         f.write("\n")
         f.close()
     
     def count(self):
         return self._count

     
