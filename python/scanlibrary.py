import os
from lxml import etree
class device:
    def __init__(self,ipadress,name):
        self.ipadress=str(ipadress)
        self.name=str(name)
        self.status="off"
    def turn_on(self):
        self.status="on"
    def turn_off(self):
        self.status="off"

def getstatus(devices):
    ips=[]
    for instance in devices:
        instance.turn_off()
    test=os.popen("nmap -sP --unprivileged 192.168.2.0/24")
    for i in test.readlines():
        if i.split(' ')[0]=='Nmap' and i.split(' ')[1]=='scan' :
            ips.append(i.split('(')[1][:-2])
    for i in xrange(0,len(ips)):
        for j in xrange(0,len(devices)):
            if ips[i]== devices[j].ipadress:
                devices[j].turn_on()
    return devices

def writexmlrow(device,container):
    col=etree.SubElement(container,'div',{'class':'col-xs-6 col-sm-2 placeholder'})
    if (device.status=='on'):
        image1=etree.SubElement(col,'img',{'src':'./images/green.png','width':'200','height':'200','class':'img-responsive','align':'center'})
    else:
        image1=etree.SubElement(col,'img',{'src':'./images/gray.png','width':'200','height':'200','class':'img-responsive','align':'center'})
    label1=etree.SubElement(col,'h4',{'align':'center'})
    label1.text=device.name
    return

def writexmlpart(devices):
    container=etree.Element('div',{'class':'row placeholder'})
    for instance in devices:
        writexmlrow(instance,container)
    output=etree.tostring(container, pretty_print=True)
    with open("./parts/part1_1.html","r") as file:
        part1=file.read()
    with open("./parts/part1_2.html","r") as file:
        part2=file.read()
    with open("./parts/part1.html","w") as file:
        file.write(part1+output+part2)
    return
def writescanlog():
    localtime==time.localtime(time.time())
    with open("./log/scanlog.txt","a") as log:
        log.write(str(localtime[3])+':'+str(localtime[4])+'on the'+str(localtime[2])+'.'+str(localtime[1])+'.'+str(localtime[0])[-2:])
        log.write("Scanned Wifi for my Devices")
