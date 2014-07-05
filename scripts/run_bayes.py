import re
from os import walk
from subprocess import call

data_dir = "data"
models_dir = "models"

models = []
print "MODELS:"
for (dirpath, dirnames, filenames) in walk(models_dir):
  for filename in filenames:
    if re.match('.*\.xml$', filename):
      print filename
      models.append(filename)
  break

datasets = []
print "\nDATASETS:"
for (dirpath, dirnames, filenames) in walk(data_dir):
  for filename in filenames: 
    if re.match('K[A-Za-z]{7}[0-9]{1,3}\.nom\.arff$', filename):
      print filename
      datasets.append(filename)
  break
print "\n"

for model in models:
  print "___________________________________________"
  print "MODEL: " + model

  for data in datasets:
    print "\t_____________________________"
    print "\tDATA: " + data

    command = "java -Xmx1500m weka.classifiers.bayes.BayesNet -v -o -t " + data_dir + "/" + data + " -Q weka.classifiers.bayes.net.search.fixed.FromFile -- -B " + models_dir + "/" + model + " -E weka.classifiers.bayes.net.estimate.SimpleEstimator -- -A 1.0"
    print "\t" + command
    call(command, shell=True)

