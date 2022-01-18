#!/usr/bin/python
import csv
import random
import sys
import pprint
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



from tabulate import tabulate
from numpy import *

from sklearn import svm
from sklearn.linear_model import Perceptron
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier


"""
seea also:
https://github.com/DarkGoomba/scikit-learn-banknote/blob/master/Banknote%20Authentication.ipynb
for some dettagle
"""

"""
In the US there is about one counterfeit banknote for every 10,000 genuine banknotes.
Although they are nearly impossible to identify with the naked eye, image
processing is one method that can be used to spot discrepencies in counterfeit notes.
Given a dataset of over a thousand notes with 4 attributes each, we can use machine
learning models such as logistic regression and K-nearest neighbors to train an
AI to classify banknotes.
"""

# Read data in from file
with open("banknotes.csv") as f:
    reader = csv.reader(f)
    next(reader)

    data = []
    for row in reader:
        # print(row)
        data.append({
            "evidence": [float(cell) for cell in row[:4]],
            "label": "Authentic" if row[4] == "0" else "Counterfeit"
        })

# pprint.pprint(data)
"""
[
  {
   'evidence': [2.3718, 7.4908, 0.015989, -1.7414],
   'label': 'Authentic'
  },
  ...
]
"""

# Separate data into training and testing groups
holdout = int(0.40 * len(data)) # prende 40% del dataset
random.shuffle(data) # mischia dati
testing = data[:holdout]
training = data[holdout:]

X = [row["evidence"] for row in data]

attr = ['Variance', 'Skewness', 'Curtosis', 'Entropy', 'Class']

# distribution of each of these attributes
X = [row["evidence"] for row in data]
fig, axarr = plt.subplots(2, 2, sharex='col', sharey='row')
axarr[0, 0].hist([ r[0] for r in X], 30, density=True, stacked=True)
axarr[0, 0].set_title(attr[0])
axarr[0, 1].hist([ r[1] for r in X], 30, density=True, stacked=True)
axarr[0, 1].set_title(attr[1])
axarr[1, 0].hist([ r[2] for r in X], 30, density=True, stacked=True)
axarr[1, 0].set_title(attr[2])
axarr[1, 1].hist([ r[3] for r in X], 30, density=True, stacked=True)
axarr[1, 1].set_title(attr[3])
plt.savefig('graphs/distribution of each of these attributes.png')
plt.close()

model = None

res = array([
    ['Model','Correct','Incorrect','Accuracy (%)','Cost (ms)'],
    [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0] ])

graf_res = array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])

for x in range(4):

    if x == 0:
        model = Perceptron()
    if x == 1:
        model = svm.SVC()
    if x == 2:
        model = KNeighborsClassifier(n_neighbors=1)
    if x == 3:
        model = GaussianNB()

    t = time.process_time()

    # Train model on training set
    X_training = [row["evidence"] for row in training]
    y_training = [row["label"] for row in training]
    model.fit(X_training, y_training)

    # Make predictions on the testing set
    X_testing = [row["evidence"] for row in testing]
    y_testing = [row["label"] for row in testing]
    predictions = model.predict(X_testing)

    # Compute how well we performed
    correct = 0
    incorrect = 0
    total = 0
    for actual, predicted in zip(y_testing, predictions):
        total += 1
        if actual == predicted:
            correct += 1
        else:
            incorrect += 1

    # Print results
    accuracy = 100 * correct / total
    cost = int(1000 * (time.process_time() - t))

    res[x+1][0] = (type(model).__name__)[:12]
    res[x+1][1] = correct
    res[x+1][2] = incorrect
    res[x+1][3] = f"{accuracy:.2f}"
    res[x+1][4] = cost

    # Res for graphs
    graf_res[0][x] = correct
    graf_res[1][x] = incorrect
    graf_res[2][x] = accuracy
    graf_res[3][x] = cost


print (tabulate(res[1:], headers=res[0]))

nomi_graf = [x[0] for x in res[1:]]

x_pos = np.arange(len(nomi_graf))

plt.bar(x_pos, graf_res[0], width=0.2, align='center', label='correct')
plt.xticks(x_pos, nomi_graf)
plt.ylabel('n answers')
plt.xlabel('model')
plt.title('Correct answers for model')
plt.savefig('graphs/graph_corr.png')
plt.clf()

plt.bar(x_pos, graf_res[0], width=0.2, align='center', label='incorrect')
plt.xticks(x_pos, nomi_graf)
plt.ylabel('n answers')
plt.xlabel('model')
plt.title('Wrong answers for model')
plt.savefig('graphs/graph_incorr.png')
plt.clf()

plt.bar(x_pos, graf_res[0], width=0.2, align='center', label='correct')
plt.bar(x_pos, graf_res[1], width=0.2, align='center', bottom=graf_res[0], label='incorrect')
plt.xticks(x_pos, nomi_graf)
plt.ylabel('n answers')
plt.xlabel('model')
plt.title('Answers for model')
plt.legend()
plt.savefig('graphs/graph_cor_inc.png')
plt.clf()

plt.bar(x_pos, graf_res[2], width=0.2, align='center', label='correct')
plt.xticks(x_pos, nomi_graf)
plt.ylabel('accuracy in %')
plt.xlabel('model')
plt.title('Accuracy for model')
plt.savefig('graphs/graph_acc.png')
plt.clf()

plt.bar(x_pos, graf_res[3], width=0.2, align='center', label='correct')
plt.xticks(x_pos, nomi_graf)
plt.ylabel('millisecond')
plt.xlabel('model')
plt.title('Cost for model')
plt.savefig('graphs/graph_cost.png')
plt.close()

ax1 = plt.subplot(1,1,1)
w=0.3
plt.xticks(x_pos + w /2, nomi_graf)
acc = ax1.bar(x_pos, graf_res[2], width=w, color='b', align='center')
ax2 = ax1.twinx()
cost = ax2.bar(x_pos + w, graf_res[3], width=w, color='y', align='center')
plt.ylabel('ms')
plt.legend([acc, cost],['accuracy for model', 'cost for model'])

plt.savefig('graphs/graph_acc_cost.png')
plt.close()
