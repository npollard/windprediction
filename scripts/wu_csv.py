import urllib2
import sys

station = 'KCADAVEN4'

print >> sys.stderr, 'STATION: ' + station

# print header
print "UTC_DATETIME,WIND_DIRECTION,WIND_SPEED_GUST_MPH,WIND_SPEED_MPH"

# grab csv data from wunderground for 12/31/2011 - 5/31/2014
for day in range(882):
  print >> sys.stderr, '.',
  f = urllib2.urlopen('http://www.wunderground.com/weatherstation/WXDailyHistory.asp?ID=' + station + '&day=' + str(day) + '&month=1&year=2012&graphspan=day&format=0')
  
  # alternatively, can grab csv from local files
#for day in range(26, 28):
  #filename = './WXDailyHistory.asp?day=' + str(day) + '.html'
  #f = file(filename)
  
  data = f.read()
  rows = data.split('\n<br>\n')
  
  # check if the page we requested has actual data
  if len(rows) < 3:
    continue

  for row in rows:
    fields = row.split(',')
    
    # handle EOF
    if len(fields) == 1:
      continue
    
    # grab UTC datetime, wind direction, windspeed (mph), windspeed gust (mph)
    print "{0},{1},{2},{3}".format(fields[-2], fields[-13], fields[-11], fields[-10])

