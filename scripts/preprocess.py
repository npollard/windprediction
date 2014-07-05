print 'YEAR,MONTH,DAY,TIME,DIRECTION,WIND,NEXT_DIRECTION,NEXT_WIND'

filename = 'data/KCASANTA132.raw.csv'
f = file(filename)
data = f.read()
rows = data.split('\n')

for i, row in enumerate(rows[1:len(rows)-2]):
  next_row = rows[i+2].split(',')
  next_direction = next_row[1]
  next_wind = next_row[2]
 
  fields = row.split(',')
  
  date = fields[0].split(' ')[0].split('-')
  year = date[0]
  month = date[1]
  day = date[2]
  
  time = '.'.join(fields[0].split(' ')[1].split(':')[:2])
  
  wind = fields[2]
  direction = fields[1]

  print year + ',' + month + ',' + day + ',' + time + ',' + direction + ',' + wind + ',' + next_direction + ',' + next_wind
