import re
from os import walk
from subprocess import call

data_dir = "data"
models_dir = "models"

models = []
for (dirpath, dirnames, filenames) in walk(models_dir):
  models.extend(filenames)
  break

datasets = []
for (dirpath, dirnames, filenames) in walk(data_dir):
  for filename in filenames: 
    if re.match('K[A-Za-z]{7}[0-9]{1,3}.csv$', filename):
      print filename
      datasets.append(filename)
  break

for model in models:
  print "________________________"
  print "MODEL: " + model + "\n"

for data in datasets:
  print "________________________"
  print "DATA: " + data + "\n"

#  command = "java weka.classifiers.bayes.BayesNet -t data/KCASANTA132.nom.arff -Q weka.classifiers.bayes.net.search.fixed.FromFile -- -B models/single_station/" + model + " -E weka.classifiers.bayes.net.estimate.SimpleEstimator -- -A 1.0"
  #print command + "\n\n"
  #call(command, shell=True)

