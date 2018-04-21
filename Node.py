class Node:
    feature_index =None
    child_left = None
    child_right =None
    majority = None
    feature_value = None
    depth = None
    size = None
    feature = None
    ID = None
    def __str__(self):
        featurestr = '';
        IDstr = '';
        valuestr= '';
        leftnodestr = '';
        rightnodestr = '';

        if self.ID!=None:
            IDstr = str(self.ID)
        else:
            IDstr = "None"

        if self.feature!=None:
            featurestr = str(self.feature)
        elif self.feature_index!=None:
            featurestr = str(self.feature_index)
        else:
            featurestr = 'Leaf'

        if self.feature_value!=None:
            valuestr = " <= "+str(self.feature_value)
            leftnodestr = "left child:"+str(self.child_left.ID)
            rightnodestr = "right child:"+ str(self.child_left.ID)            
        else:
            valuestr = ''
    

        return "NodeID: "+ IDstr +"\n" + featurestr + valuestr + '\n' + leftnodestr +'\n' + rightnodestr

    def setValue(self, val):
        self.value = val

    def addChildren(self, feature, child_node):
        self.children[feature] = child_node
