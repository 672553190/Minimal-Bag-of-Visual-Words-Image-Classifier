#!/usr/bin/env python

#Load Map
import json
_map = json.loads('{"24": "17", "25": "18", "26": "19", "27": "20", "20": "13", "21": "14", "22": "15", "23": "16", "28": "21", "29": "22", "1": "1", "0": "0", "3": "23", "2": "12", "5": "33", "4": "32", "7": "35", "6": "34", "9": "37", "8": "36", "11": "3", "10": "2", "13": "5", "12": "4", "15": "7", "14": "6", "17": "9", "16": "8", "19": "11", "18": "10", "31": "25", "30": "24", "37": "31", "36": "30", "35": "29", "34": "28", "33": "27", "32": "26"}')

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


