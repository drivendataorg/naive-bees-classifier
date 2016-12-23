cv11 <- read.csv('./cv11_submission.csv')
cv12 <- read.csv('./cv12_submission.csv')
cv13 <- read.csv('./cv13_submission.csv')
cv14 <- read.csv('./cv14_submission.csv')
cv16 <- read.csv('./cv16_submission.csv')
cv17 <- read.csv('./cv17_submission.csv')
cv18 <- read.csv('./cv18_submission.csv')
cv19 <- read.csv('./cv19_submission.csv')
cv20 <- read.csv('./cv20_submission.csv')
cv21 <- read.csv('./cv21_submission.csv')
cv24 <- read.csv('./cv24_submission.csv')
cv26 <- read.csv('./cv26_submission.csv')

sub <- cv11

sub[,2] <- (cv11[,2] + cv12[,2] + cv13[,2] + cv14[,2] + cv16[,2] + cv17[,2] + cv18[,2] + cv19[,2] + cv20[,2] + cv21[,2] + cv24[,2] + cv26[,2]) / 12

write.csv(sub, './10fold16top12runsusinglastwithaugsubmission.csv', row.names=F)
