import numpy as np
import glob
from sklearn.metrics import roc_auc_score



def get_prediction(model_idx):
    '''Aggregate predictions at different scales'''
    fnames = glob.glob('./model_{}/TEST/pred_test_???.npy'.format(model_idx))
    preds = [np.load(f) for f in fnames]
    prediction = np.mean(preds, axis=0)
    return prediction


# Ensemble predictions from all cross-validation models
model_idx = 0
p = get_prediction(model_idx)
for i in xrange(1,10):
    p = p + get_prediction(i)
p /= 10.0


sample = map(lambda x: int( x.split(',')[0] ),
             open('../../DATA/SubmissionFormat.csv', 'r').readlines()[1:])

# Save aggregated ensembled predictions to submission file
f = open('submission.csv', 'w')
f.write('id,genus\n')
i = 0
for idx in sample:
    f.write('{},{}\n'.format(idx, p[i,1]))
    i += 1
f.close()
