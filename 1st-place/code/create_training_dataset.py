import pandas as pd
import os
import random
random.seed(42)

df = pd.read_csv('labels.csv')

idx = range(len(df))
random.shuffle(idx)

validx = idx[:len(df)//10]
tridx = idx

with open('test.txt', 'w') as f:
    for id, label in df.ix[validx].values.astype('int'):
        fn = os.path.abspath('../data/images/train/{}.jpg'.format(id))
        f.write('{} {}\n'.format(fn, label))

with open('train_ext.txt', 'w') as f:
    for id, label in df.ix[tridx].values.astype('int'):
        fn = os.path.abspath('../data/images/train/{}.jpg'.format(id))
        f.write('{} {}\n'.format(fn, label))
