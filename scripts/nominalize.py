import re
from os import walk
from subprocess import call

data_dir = "data"

for (dirpath, dirnames, filenames) in walk(data_dir):
  for filename in filenames: 
    m = re.match('(K[A-Za-z]{7}[0-9]{1,3}).csv$', filename)
    if m:
      command = "java weka.filters.unsupervised.attribute.Discretize -i " + data_dir + "/" + m.group() + " -o " + data_dir + "/" + m.group(1) + ".nom.arff"
      print command
      call(command, shell=True)

  break

