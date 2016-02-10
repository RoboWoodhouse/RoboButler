# -*- coding: utf-8 -*-
from lxml import html, etree
import requests
import time

def detEnd(day_in, month_in, year_in):
    if (month_in < 6):
        month_out=month_in+6
        year_out=year_in
    else:
        month_out=mont_in-6
        year_out=year_in+1
    out=str(day_in)+'.'+str(month_out)+'.'+str(year_out)
    return out

def writelog(time_in, url):
    with open("logfile.txt","a") as file:
        file.write('REQUEST TO '+url+ ' AT '+str(time_in[3])+':'+ str(time_in[4])+ ' ON THE '+ str(time_in[2])+'.'+str(time_in[1])+'.'+str(time_in[0])[-2:]+'\n')
    return

def request(time_in):
    dateBegin=str(time_in[2])+'.'+str(time_in[1])+'.'+str(time_in[0])[-2:]
    dateEnd=detEnd(time_in[2],time_in[1],int(str(time_in[0])[-2:]))
    url='https://fahrinfo.bvg.de/Fahrinfo/bin/stboard.bin/en?boardType=depRT&application=FILTER&view=STATIONINFO&maxJourneys=20&REQProduct_5_name=yes&REQProduct_6_name=yes&REQProduct_0_name=yes&REQProduct_1_name=yes&REQProduct_2_name=yes&REQProduct_3_name=yes&REQProduct_4_name=yes&input=+S%2BU+Hermannstr.+%28Berlin%29&REQ0JourneyStopsSID=A%3D1%40O%3DS%2BU+Hermannstr.+%28Berlin%29%40X%3D13431699%40Y%3D52467177%40U%3D80%40L%3D9079221%40B%3D1%40p%3D1452855421%40&REQ0JourneyProduct_prod_list_6=0000001000000000&REQ0JourneyProduct_prod_list_0=1000000000000000&REQ0JourneyProduct_prod_list_1=0100000000000000&REQ0JourneyProduct_prod_list_2=0010000000000000&REQ0JourneyProduct_prod_list_3=0001000000000000&REQ0JourneyProduct_prod_list_4=0000100000000000&existBikeEverywhere=yes&selectDate=today&dateBegin='+dateBegin+'&dateEnd='+dateEnd+'&time='+str(time_in[3])+'%3A'+str(time_in[4])+'&timeselectEnd=Reset&start='

    input=requests.get(url)
    variable=html.fromstring(input.content)
    times=[]
    lines=[]
    destination=[]
    for instance in variable.xpath('//table[@summary="Departures"]/tbody/tr/td[@ headers="hafasSQarrTime"]/span[@class="prognosis"]/text()'):
        times.append(instance.strip('\n'))
    for instance in variable.xpath('//table[@summary="Departures"]/tbody/tr/td[@headers="hafasSQarrLine"]/a/text()'):
        lines.append(instance.strip('\n'))
    for instance in variable.xpath('//table[@summary="Departures"]/tbody/tr/td[@headers="hafasSQarrDest"]/a/text()'):
        destination.append(instance.strip('\n').strip('\n'))

    writelog(time_in, url)

    return times, lines, destination
def detfreq(time_in):
    if time_in[6]<5:
        if time_in[3]>6 and time_in[3]<22:
            sleeptime=600
        else:
            sleeptime=1200
    else:
        if time_in[3]>8 :
            sleeptime=600
        else:
            sleeptime=1200
    return sleeptime
def writexml(times_in, lines_in, destinations_in):
    container=etree.Element('div',{'class':'table-responsive'})
    table=etree.SubElement(container,'table',{'class':'table table-striped'})
    thead=etree.SubElement(table,'thead')
    tr=etree.SubElement(thead,'tr')
    th=etree.SubElement(tr,'th')
    th.text='Time'
    th2=etree.SubElement(tr,'th')
    th2.text='Line'
    th2=etree.SubElement(tr,'th')
    th2.text='Destination'
    tbody=etree.SubElement(table,'tbody')
    for i in xrange(0,len(times_in)):
        tr=etree.SubElement(tbody,'tr')
        th=etree.SubElement(tr,'th')
        th.text=str(times_in[i])
        th2=etree.SubElement(tr,'th')
        th2.text=str(lines_in[i])
        th3=etree.SubElement(tr,'th')
        th3.text=destinations_in[i]
    output=etree.tostring(container, pretty_print=True, encoding='utf-8')

    return output
def writeindex(input):
    with open("./content/bvg.php",'w') as file:
        file.write(input)
    return
def writebvglog():
    localtime==time.localtime(time.time())
    with open("./log/bvglog.txt","a") as log:
        log.write(str(localtime[3])+':'+str(localtime[4])+'on the'+str(localtime[2])+'.'+str(localtime[1])+'.'+str(localtime[0])[-2:])
        log.write("Obtained Traffic Data from bvg.de")
