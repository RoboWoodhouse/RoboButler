import scanlibrary as scan
import os
from lxml import etree
import time

devices=[scan.device('192.168.2.1','Router'),scan.device('192.168.2.118','Tablet'),scan.device('192.168.2.162','MediaLaptop'),scan.device('192.168.2.195','ChristianHandy'),scan.device('192.168.2.191','ChristianDesktop')]
sleeptime=300
devices=scan.getstatus(devices)
scan.writexmlpart(devices)
writescanlog()
while True:
    time.sleep(sleeptime)
    devices=scan.getstatus(devices)
    scan.writexmlpart(devices)
    writescanlog()
