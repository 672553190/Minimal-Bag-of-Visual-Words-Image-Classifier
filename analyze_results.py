#!/usr/bin/env python

#Load Map
import json
_map = json.loads(open("category_mapping.json", "r").read())

#Analyse results on the test set
TEST_FILENAMES = "filenames.txt.TEST"
TEST_PREDICTIONS = "trainingdata.svm.prediction.TEST" 

##Load predictions
predictions = open(TEST_PREDICTIONS, "r").readlines()
predictions = [x.strip() for x in predictions]

total = 0
correct = 0

for idx, _line in enumerate(open(TEST_FILENAMES, "r").readlines()):
	category = _line.split("/")[3]
	true_label = _map[category]
	prediction = predictions[idx]
	if true_label == prediction:
		correct += 1
	total += 1
print "Analysing on TEST set ::"
print "Correct : ", correct
print "Total : ", total
print "TEST_SET Accuracy : ", correct*1.0/total
print "="*80

#Analyse results on the training set
TRAIN_FILENAMES = "filenames.txt.TRAIN"
TRAIN_PREDICTIONS = "trainingdata.svm.prediction.TRAIN" 

##Load predictions
predictions = open(TRAIN_PREDICTIONS, "r").readlines()
predictions = [x.strip() for x in predictions]

total = 0
correct = 0

for idx, _line in enumerate(open(TRAIN_FILENAMES, "r").readlines()):
	category = _line.split("/")[3]
	true_label = _map[category]
	prediction = predictions[idx]
	if true_label == prediction:
		correct += 1
	total += 1
print "Analysing on TRAIN set ::"
print "Correct : ", correct
print "Total : ", total
print "TRAIN_SET Accuracy : ", correct*1.0/total
print "="*80


