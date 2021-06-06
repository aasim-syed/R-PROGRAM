library(tm)
setwd("G:\\phd\\work\\R work\\")
docs<- Corpus(DirSource("G:\\phd\\work\\R work\\DataSet\\my"))
docs <- tm_map(docs, removePunctuation)
docs <- tm_map(docs, removeNumbers)
docs <- tm_map(docs, tolower)
docs <- tm_map(docs, removeWords, stopwords("english"))
docs <- tm_map(docs, stemDocument)
docs <- tm_map(docs, stripWhitespace)
docs <- tm_map(docs, PlainTextDocument)

dtm <- DocumentTermMatrix(docs)
dtm.matrix <- as.matrix(dtm) 
m <- as.matrix(dtm)
featurelist<-findFreqTerms(dtm)
write(featurelist,file="featurelist.txt");
write.csv(dtm.matrix,file="mytf.csv")


tdm <- TermDocumentMatrix(docs)
tdm.matrix<-as.matrix(tdm)
write.csv(tdm.matrix,file ="tdm.csv" )
