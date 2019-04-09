import os, sys, io

myDomainSelf = os.environ.get('localhost')
print(myDomainSelf)
myPathSelf = os.environ.get('PATH_INFO')
myURLSelf = myDomainSelf + myPathSelf
url = os.environ['HTTP_HOST']
print(url)