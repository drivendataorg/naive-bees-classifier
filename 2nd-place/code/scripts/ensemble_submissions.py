import numpy as np
import glob


submission_files = glob.glob('../MODELS/models_*/submission.csv')
data = np.loadtxt(submission_files[0], skiprows=1, delimiter=',')

data[:,1] *= np.prod([np.loadtxt(f, skiprows=1, delimiter=',')[:,1] for f in submission_files[1:]],
                     axis=0)

f = open('ensemble.csv', 'w')
f.write('id,genus\n')
for i in xrange(data.shape[0]):
    f.write('{},{}\n'.format(int(data[i,0]), data[i,1]))
f.close()

