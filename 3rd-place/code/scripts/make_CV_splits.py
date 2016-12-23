# make K-fold cross-validation splits

import numpy as np
from collections import Counter
from sklearn.cross_validation import StratifiedKFold

# number of splits
K = 10

# Load train data
data = np.loadtxt('../DATA/train_labels.csv', skiprows=1, delimiter=',')

# create K train / validation splits
skf = StratifiedKFold(data[:,1], n_folds=K, shuffle=True, random_state=609)

# save K train / validation splits to corresponded files
for idx, (train_idx, val_idx) in enumerate(skf):
    print 'Fold #{}: train, {} images'.format(idx, len(train_idx))
    f = open('../DATA/LMDBs/train_{}.txt'.format(idx), 'w')
    for i in train_idx:
        f.write('images/train/{}.jpg {}\r\n'.format(int(data[i,0]), int(data[i,1])))
    f.close()

    print 'Fold #{}: validation, {} images'.format(idx, len(val_idx))
    f = open('../DATA/LMDBs/val_{}.txt'.format(idx), 'w')
    for i in val_idx:
        f.write('images/train/{}.jpg {}\r\n'.format(int(data[i,0]), int(data[i,1])))
    f.close()
