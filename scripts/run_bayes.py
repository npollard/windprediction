import re
import sys
from os import walk
from subprocess import call

data_dir = "data"
models_dir = "models"
model = "naive_1.xml"

datasets = []
print "\nDATASETS:"
for (dirpath, dirnames, filenames) in walk(data_dir):
  for filename in filenames: 
    if re.match('K[A-Za-z]{7}[0-9]{1,3}\.nom\.arff$', filename):
      print filename
      datasets.append(filename)
  break
print "\n"

print "MODEL: " + model

for data in datasets:
  print "\t_____________________________"
  print "\tDATA: " + data
  command = "java -Xmx1500m weka.classifiers.bayes.BayesNet -o -t " + data_dir + "/" + data + " -Q weka.classifiers.bayes.net.search.fixed.FromFile -- -B " + models_dir + "/" + model + " -E weka.classifiers.bayes.net.estimate.SimpleEstimator -- -A 1.0"
  print "\t" + command
  sys.stdout.flush()
  call(command, shell=True)

