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

def writexmlrow(device,number):
    if (number==1):
        col=etree.Element('div',{'class':'col-lg-2 col-lg-offset-1 col-md-2 col-md-offset-1 placeholder'})
    else:
        col=etree.Element('div',{'class':'col-lg-2 col-md-2 placeholder'})
    if (device.status=='on'):
        image1=etree.SubElement(col,'img',{'src':'./images/green.png','width':'200','height':'200','class':'img-responsive','align':'center'})
    else:
        image1=etree.SubElement(col,'img',{'src':'./images/gray.png','width':'200','height':'200','class':'img-responsive','align':'center'})
    label1=etree.SubElement(col,'h4',{'align':'center'})
    label1.text=device.name
    return etree.tostring(col, pretty_print=True)

def writexmlpart(devices):
    output=''
    i=1
    for instance in devices:
        output=output+writexmlrow(instance,i)
        i=i+1
    with open("./content/activity.php","w") as file:
        file.write(output)
    return
def writescanlog():
    localtime==time.localtime(time.time())
    with open("./log/scanlog.txt","a") as log:
        log.write(str(localtime[3])+':'+str(localtime[4])+'on the'+str(localtime[2])+'.'+str(localtime[1])+'.'+str(localtime[0])[-2:])
        log.write("Scanned Wifi for my Devices")
