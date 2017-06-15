#!/usr/bin/env python3

from datetime import datetime
from time import sleep
from urllib.request import urlopen

url = "https://request-prelive.np-securepaypage-litle.com/eProtect/fonts/fontawesome-webfont.woff2?v=4.7.0"
everySec = 5
numRequests = 10

countsByNumBytes = {}
for i in range(numRequests):
    numBytes = len(urlopen(url).read())
    countsByNumBytes[numBytes] = countsByNumBytes.get(numBytes, 0) + 1
    print("{0}: {1}".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), numBytes))
    sleep(everySec)

print("Requested every {0} seconds with total number of {1} times. Distribution as follow:".format(
    everySec, numRequests
))
print(countsByNumBytes)
