from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score 
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.metrics import mean_squared_error ,r2_score
df = pd.read_csv("E:\\New Volume\\amutha\\Research\\DataSet\\Boston1.csv")
print(df.shape)
X=df.iloc[0:500,1:13]
Y=df.iloc[0:500,-1]
X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.20)
#clf = RandomForestClassifier(random_state=2)
clf = AdaBoostClassifier(n_estimators=80)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
acc=confusion_matrix(y_test,y_pred)
print ("Accuracy : ",accuracy_score(y_test,y_pred)*100) 
print(acc)
print(mean_squared_error(y_test,y_pred))