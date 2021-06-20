#!/usr/bin/python3

import urllib.request

healthcheck = urllib.request.urlopen("https://docsrv.technetex.net/healthcheck")
resultcode = str(healthcheck.getcode())
status = healthcheck.read().decode('utf-8')
print (status)