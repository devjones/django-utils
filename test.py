import os
from django.conf import settings

path = os.path.abspath(os.path.dirname(__file__))
newpath = os.path.join(path,'..','logs','testing')
log = open(newpath,'a')
log.write('lhey')
log.close()
