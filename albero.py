#!/usr/bin/python
import sys
import pprint
import time
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as snsfrom

from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

"""
Inspiration:
https://ichi.pro/it/alberi-decisionali-in-machine-learning-ml-con-python-tutorial-65950388571751
"""

def decision_tree_classifier(debug = False):

    data = pd.read_csv('banknotes.csv')
    data.shape

    print("\t\tDataset samples")
    print(data.head()) # data sample
    if debug: print(data.info()) # column dewscribe

    # 1. Add new column "category" with value  Authentic/Counterfeit insteda of 0/1
    data["category"] = ""
    for i in data.index:
        data.at[i, 'category'] = "Authentic" if data.at[i, 'class'] else "Counterfeit"
    # 2. Remove unnused column "class"
    data = data.drop(['class'], axis=1)
    if debug: print(data.head()) # data sample

    value_counts = data['category'].value_counts()
    target_col = ['category']

    if debug: print("value_counts:")
    if debug: print(value_counts)

    X = data.drop(['category'], axis=1) # extract category
    y = data['category']

    t = time.process_time()

    # in order to evalute test 548 samples, use test_size = 0.3989
    # random_state = 0 because the dates are mixed
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3989, random_state = 0)

    if debug: print("Train size: ", len(X_train))
    if debug: print("Test size: ", len(X_test))

    clf_gini = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=0)
    clf_gini.fit(X_train, y_train)
    predictions = clf_gini.predict(X_test)

    cost = int(1000 * (time.process_time() - t))
    accuracy = accuracy_score(y_test, predictions)
    train_score = clf_gini.score(X_train, y_train)
    test_score = clf_gini.score(X_test, y_test)
    if debug: print('Model accuracy score with criterion gini index: {0:0.4f}'.format(accuracy))
    # print('Training set score: {:.4f}'.format(train_score))
    # print('Test set score: {:.4f}'.format(test_score))
    if debug: print('Cost: {:.2f}'.format(cost))

    train_size = len(X_test)
    correct = int(train_size * accuracy)
    incorrect = train_size - correct
    if debug: print('Correct: {}'.format(correct))
    if debug: print('Incorrect: {}'.format(incorrect))

    plt.figure(figsize=(12,8))
    tree.plot_tree(clf_gini.fit(X_train, y_train))
    plt.savefig('graphs/tree.eps',format='eps',bbox_inches = "tight")
    # plt.savefig('graphs/tree.png',format='png',bbox_inches = "tight")
    plt.clf()

    return ["DecisionTree", correct, incorrect, accuracy * 100, cost]

if __name__ == "__main__":
    print(decision_tree_classifier(True))
