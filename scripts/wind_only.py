filename = 'KCASANTA239.csv'
f = file(filename)
  
data = f.read()
rows = data.split('\n')

prev_wind = -1
for row in rows:
  fields = row.split(',')
  wind = fields[-1]
  print str(prev_wind) + "," + str(wind)
  prev_wind = wind
