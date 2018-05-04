## software
- This software is to learn a decision tree from a traning data set
- report the size of the learned tree.
- run that tree on a data set(both the training data and test data),producing statistics on accuracy.
## Data
- The data sets are all represented in a standard format, consisting of four files per data set. The first file, .names, describes the categories and features of the dataset, and is formatted as follows (comma separated values, although the lines are not equal length; this is not a spreadsheet format):
- cat1, cat2, cat3, ... catn
- feature1, feature2, feature3, ... featurek
- Where cat1 ... catn are the n names of the output categories, and feature1 ... featurek are the names of the input features. Assuming that all features will be numeric-valued, taking on continuous values (we've recoded any discrete features as integers). Categories are also numeric, although discrete integers.
### BALLOONS 
- These are four very very small files you can use to test your program on. They are simple enough that you will know the correct answer (see balloon.info) and each feature is binary and there are only two classes. There are no test or pruning sets provided, you may make some up.
### Wisconsin 
- Diagnostic Breast Cancer This is a medical database representing the classification of 569 patients into those with and without malignant breast tumors.
### Handwritten 
- Pen/Tablet Digit Recognition This data are from 44 subjects each writing a random sequence of 250 single digits on an electronic tablet; the classification task is to identify which digit they wrote. The training data for this set has been further partitioned into pen_10 ... pen_60 each representing a fraction of the available training data. This will allow you to generate a “happy graph” (hopefully) demonstrating that your algorithm does, in fact, learn the concept better as it is presented with more training data.
### pen2 
- This is the same data set as pen_60, but with the last eight features removed.
- pen3 This is also the same data as pen_60, but this time with every other feature removed.
