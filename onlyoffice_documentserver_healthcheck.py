#!/usr/bin/python3

import urllib.request, os
try:
    healthcheck = urllib.request.urlopen("https://docsrv.technetex.net/healthcheck")
    status = healthcheck.read().decode('utf-8')
    if(str(healthcheck.getcode() == '200')):
        if(status):
            print('0 "DocSrv" - DocumentServer is running')
        else:
            print('2 "DocSrv" - DocumentServer not running')
    else:
        if(os.system('service nginx status') != 0):
            print('2 "DocSrv" - NGinX not working')
            os.system('service nginx restart')
        else:
            print('3 "DocSrv" - There seems to be a http problem not related to NGinX')
except:
    print('3 "DocSrv" - It seems a HTTP error occured')
    if(os.system('service nginx status') != 0):
        print('2 "DocSrv" - NGinX not working')
        os.system('service nginx restart')
    else:
        print('3 "DocSrv" - There seems to be a http problem not related to NGinX')
