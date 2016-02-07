# -*- coding: utf-8 -*-
from lxml import html, etree
import requests
import time
import bvglibrary as bvg

#initial code run
localtime=time.localtime(time.time())
times, lines, destinations=bvg.request(localtime)
output=bvg.writexml(times,lines,destinations)
sleeptime=bvg.detfreq(time.localtime(time.time()))
writebvglog()
bvg.writeindex(output)

sleeptime=600 #initial sleep time
while True:
    time.sleep(sleeptime)
    localtime=time.localtime(time.time())
    times, lines, destinations=bvg.request(localtime)
    output=bvg.writexml(times,lines,destinations)
    sleeptime=bvg.detfreq(time.localtime(time.time()))
    bvg.writeindex(output)
    writebvglog()
