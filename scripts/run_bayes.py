from os import walk
from subprocess import call

data = "data/KCASANTA132.nom.arff";
models_path = "/Users/nelson/Documents/schools/independent_study/models/single_station"
models = []
for (dirpath, dirnames, filenames) in walk(models_path):
  models.extend(filenames)
  break

for model in models:
  print "________________________"
  print "MODEL: " + model

  command = "java weka.classifiers.bayes.BayesNet -t data/KCASANTA132.nom.arff -Q weka.classifiers.bayes.net.search.fixed.FromFile -- -B models/single_station/" + model + " -E weka.classifiers.bayes.net.estimate.SimpleEstimator -- -A 1.0"
  print command + "\n\n"
  call(command, shell=True)

  print "\n\n"
