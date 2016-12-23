import pandas as pd

s1 = pd.read_csv('submission_8000.csv').genus.values
s2 = pd.read_csv('submission_15000.csv').genus.values
s3 = pd.read_csv('submission_20000.csv').genus.values

sample = pd.read_csv('SubmissionFormat.csv')

px = (s1 + s2 + s3)/3.0
sample.genus = px

sample.to_csv('FinalSubmission.csv', index=False)