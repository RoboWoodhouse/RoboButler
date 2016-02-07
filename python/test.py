# -*- coding: utf-8 -*-
from lxml import html, etree
import requests
import os
import time
import bvglibrary as bvg
import scanlibrary as scan
import time

devices=[scan.device('192.168.2.1','Router'),scan.device('192.168.2.118','Tablet'),scan.device('192.168.2.162','MediaLaptop'),scan.device('192.168.2.195','ChristianHandy'),scan.device('192.168.2.191','ChristianDesktop')]

devices=scan.getstatus(devices)
scan.writexmlpart(devices)
localtime=time.localtime(time.time())
times, lines, destinations=bvg.request(localtime)
output=bvg.writexml(times,lines,destinations)
bvg.writeindex(output)
