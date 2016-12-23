sub <- read.csv('./tmp.txt')
sample <- read.csv('./SubmissionFormat.csv')

sample$genus <- NULL

sub <- merge(sample,sub,sort=F)

write.csv(sub,'submission.csv',row.names=F)
