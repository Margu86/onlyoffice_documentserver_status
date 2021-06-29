#!/usr/bin/python3

import urllib.request

healthcheck = urllib.request.urlopen("https://docsrv.technetex.net/healthcheck")
status = healthcheck.read().decode('utf-8')
if(str(healthcheck.getcode() == '200')):
    if(status):
        print('0 "DocSrv" - DocumentServer is running')
    else:
        print('2 "DocSrv" - DocumentServer not running')
else:
    print('3 "DocSrv" - Unknown state')