# coding=utf-8
import csv
import operator
from math import log
import time
import Node
import copy


def read(filename):
    file = open(filename)
    datareader = csv.reader(file, delimiter=',')
    data = []
    for line in datareader:
        data.append([int(i) for i in line])
    return data




def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for feaVec in dataSet:
        currentLabel = feaVec
        if currentLabel not in labelCounts:
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt


def splitDataSet(dataSet, feature_index, value,direction=1):
    data=[]
    if direction ==1:
        data = [i for i in dataSet if i[feature_index] <=value]
    else :
        data = [i for i in dataSet if i[feature_index] > value]
    return data


def chooseBestFeatureToSplit(dataset):
    data = []
    split = False
    for i in range(0,len(dataset[0])):
        data.append([x[i] for x in dataset])
    info_min = calcShannonEnt(data[-1])
    feature_index = None
    feature_value = None
    for i in range(0,len(data)-1):
        set_i = list(set(data[i]))
        for j in range(0,len(set_i)-1):
            response_left = [y for x,y in zip(data[i],data[-1]) if x <=set_i[j]]
            response_right = [y for x,y in zip(data[i],data[-1]) if x >set_i[j]]
            n_l = float(len(response_left))
            n_r = float(len(response_right))
            info_ij = n_l/(n_l+n_r)*calcShannonEnt(response_left)+n_r/(n_l+n_r)*calcShannonEnt(response_right)
            if info_ij < info_min:
                info_min = info_ij
                split = True
                feature_index = i
                feature_value = set_i[j]
    return [split, feature_index,feature_value]

def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    return max(classCount)


def createTree(dataSet,label=[],ID=1):
    tree = Node.Node()
    ID1 = None;
    ID2 = None;
    if ID!=None:
        tree.ID = ID
    classList = [int(example[-1]) for example in dataSet]
    tree.majority =  max(set(classList), key = classList.count)
    split_indicator = chooseBestFeatureToSplit(dataSet)
    split = split_indicator[0]
    split_index = split_indicator[1]
    split_value = split_indicator[2]

    if split == False :
        tree.depth = 0
        tree.size = 1
    else:
        if ID != None:
            ID1 = ID*10+1
            ID2 = ID*10+2

        tree.child_left = createTree(splitDataSet(dataSet,split_index,split_value,1),label,ID1)
        tree.child_right = createTree(splitDataSet(dataSet,split_index,split_value,2),label,ID2)
        tree.depth = max([tree.child_right.depth,tree.child_left.depth])+1
        tree.size = tree.child_left.size + tree.child_right.size +1
        tree.feature_value = split_value
        tree.feature_index = split_index
        if label != []:
            tree.feature = label[split_index]
    return tree

def predict (tree, data):
    if tree.child_left == None:
        return tree.majority
    else:
        if data[tree.feature_index]<= tree.feature_value:
            return predict(tree.child_left, data)
        else:
            return predict(tree.child_right,data)

def accuracy(testset,tree):
    response = [int(example[-1]) for example in testset]
    response_est = []
    for i in testset:
        response_est.append(predict(tree,i))

    right_num = len([x for x,y in zip(response,response_est) if x==y])
    return float(right_num)/len(response)



def printTree(tree,url,root = 1):
    if root ==1:
        method ='wb'
    else:
        method ='a'

    with open(url,method) as f:
        spamwriter = csv.writer(f,delimiter=',')
        if root ==1:
            spamwriter.writerow(['ID', 'majority','size', 'depth', 'feature_index', 'feature', 'value', 'left node ID', 'right node ID'])

        child1 ='None'
        child2 ='None'
        if tree.child_left != None:
            child1 = tree.child_left.ID
            child2 = tree.child_right.ID

        spamwriter.writerow([tree.ID,tree.majority,tree.size,tree.depth,tree.feature_index,tree.feature,tree.feature_value,child1,child2])
    if tree.child_left !=None :
        printTree(tree.child_left,url,2)
        printTree(tree.child_right,url,2)
