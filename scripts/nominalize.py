import re
from os import walk
from subprocess import call

data_dir = "data"

for (dirpath, dirnames, filenames) in walk(data_dir):
  for filename in filenames: 
    m = re.match('(K[A-Za-z]{7}[0-9]{1,3}).csv$', filename)
    if m:
      print m.group()
      print m.group(1) + ".nom.arff"

  break

#  command = "java weka.classifiers.bayes.BayesNet -t data/KCASANTA132.nom.arff -Q weka.classifiers.bayes.net.search.fixed.FromFile -- -B models/single_station/" + model + " -E weka.classifiers.bayes.net.estimate.SimpleEstimator -- -A 1.0"
  #print command + "\n\n"
  #call(command, shell=True)

