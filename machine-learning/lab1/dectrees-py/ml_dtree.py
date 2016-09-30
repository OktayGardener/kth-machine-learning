import dtree as dt
import monkdata as dataset


class DecisionTree:
    "Driver class"

    def __init__(self, dtree, dataset):
        self.dtree = dtree
        self.monk1 = dataset.monk1
        self.monk1test = dataset.monk1test
        self.monk2 = dataset.monk2
        self.monk2test = dataset.monk2test
        self.monk3 = dataset.monk3
        self.monk3test = dataset.monk3test

    def calc_entropy(self):
        e_m1 = dt.entropy(self.monk1)
        e_m2 = dt.entropy(self.monk2)
        e_m3 = dt.entropy(self.monk3)
        return [e_m1, e_m2, e_m3]

    def calc_avg_gain(self):
        monk1 = []
        monk2 = []
        monk3 = []
        attributes = dataset.attributes
        for x in attributes:
            monk1.append(dt.averageGain(self.monk1, x))
            monk2.append(dt.averageGain(self.monk2, x))
            monk3.append(dt.averageGain(self.monk3, x))
        return [monk1, monk2, monk3] # [ [] , [] , [] ]

def main():
    dtree = DecisionTree(dt, dataset)

    # Assignment 1
    entropies = dtree.calc_entropy()
    col = ['Dataset', 'Entropy']
    row = ['MONK-1', 'MONK-2', 'MONK-3']

    rows = zip(entropies, row)

    print "Entropies for MONK Datasets \n", col[0], '\t', col[1]

    print row[0], '\t\t', entropies[0]
    print row[1], '\t\t', entropies[1]
    print row[2], '\t\t', entropies[2]
    print '\n'
    # Assignment 2
    col = ['Dataset', 'a_1', 'a_2', 'a_3', 'a_4', 'a_5', 'a_6']

    avg_gains = dtree.calc_avg_gain()

    print 'Information Gain for MONK Datasets'
    print '\t\t'.join(col)
    for x in range(0, 3):
        print row[x], '\t'.join(map(str, avg_gains[x]))
    # the a_n (information gain) that is the highest is the best one
    # the highest a_n is the one that reduces the most uncertainty in the sub-tree prediction
    # therefore, a _ 5 minimizes MONK-1 and MONK-3 uncertainty

    # Assignment 3

if __name__ == '__main__':
    main()
