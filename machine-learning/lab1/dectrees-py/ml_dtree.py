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

def main():
    dtree = DecisionTree(dt, dataset)

    # Assignment 1
    entropies = dtree.calc_entropy()
    col = ['Dataset', 'Entropy']
    row = ['MONK-1', 'MONK-2', 'MONK-3']

    rows = zip(entropies, row)

    print "Entropies for MONK Datasets \n\n", col[0], '\t', col[1]

    print row[0], '\t\t', entropies[0]
    print row[1], '\t\t', entropies[1]
    print row[2], '\t\t', entropies[2]


if __name__ == '__main__':
    main()
