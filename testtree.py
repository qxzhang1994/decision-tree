import dt
#labels = ['x1', 'y1', 'x2', 'y2', 'x3', 'y3', 'x4', 'y4', 'x5', 'y5', 'x6', 'y6', 'x7', 'y7', 'x8', 'y8']
#labels = ['clump_thickness', 'Uniform_cell_size', 'Uniform_cell_shape', 'Marginal_adhesion', 'Single_epithelial_cell_size', 'Bare_nuclei', 'Bland_Chromatin', 'Normal_Nucleoli', 'Mitoses']
labels = ['Color', 'size', 'act', 'age']

traindata = dt.read('yellow-small-Badult-stretch.csv')
#testdata = dt.read('pen-test.csv')

tree = dt.createTree(traindata,labels)
train_accuracy = dt.accuracy(traindata,tree)

#test_accuracy = dt.accuracy(testdata,tree)
#print(test_accuracy)
print(tree)
print tree.size
print tree.depth