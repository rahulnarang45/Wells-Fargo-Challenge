import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np
import seaborn as sns
import math 

titanic_data=pd.read_csv("F:/Development/Machine Learning/Titanic/train.csv")
print(titanic_data.head(10))
print("the no of passengers in the list is "+str(len(titanic_data.index)))
sns.countplot(x='Survived',data=titanic_data)
plt.show()
sns.countplot(x='Survived',hue='Sex',data=titanic_data)
plt.show()
sns.countplot(x='Survived',hue='Pclass',data=titanic_data)
plt.show()
titanic_data['Age'].plot.hist()
plt.show()
titanic_data['Fare'].plot.hist(bins=20,figsize=(10,5))
plt.show()
print(titanic_data.info())
sns.countplot(x='SibSp',data=titanic_data)
plt.show()
sns.countplot(x='Parch',data=titanic_data)
plt.show()
print(titanic_data.isnull())
print(titanic_data.isnull().sum())
print("the no of null values in age column are",titanic_data['Age'].isnull().sum())
print("the no of null values in cabin column are",titanic_data['Cabin'].isnull().sum())
print("the no of null values in embarked column are",titanic_data['Embarked'].isnull().sum())
sns.heatmap(titanic_data.isnull(),yticklabels=False,cmap="viridis")
plt.show()
sns.boxplot(x="Pclass",y="Age",data=titanic_data)
plt.show()
titanic_data.drop("Cabin", axis=1,inplace=True)
print(titanic_data.head(5))
titanic_data.head(5)
titanic_data.dropna(inplace=True)
sns.heatmap(titanic_data.isnull(),yticklabels=False,cmap="viridis")
plt.show()
print(titanic_data.isnull().sum())
print(titanic_data.head(2))
Sex=pd.get_dummies(titanic_data['Sex'],drop_first=True)
print(Sex.head(5))
titanic_data.head(5)
Embark=pd.get_dummies(titanic_data["Embarked"],drop_first=True)
print(Embark.head(10))
print(titanic_data.head(5))
Pcl=pd.get_dummies(titanic_data["Pclass"],drop_first=True)
print(Pcl.head(5))
print(titanic_data.columns)
titanic_data=pd.concat([titanic_data,Sex,Embark,Pcl],axis=1)
print(titanic_data.head(5))
titanic_data.drop(["Pclass","Sex","Embarked","PassengerId","Name","Ticket",],axis=1,inplace=True)
print(titanic_data.head(5))
X=titanic_data.drop("Survived",axis=1)
y=titanic_data["Survived"]
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
from sklearn.linear_model import LogisticRegression
logmodel=LogisticRegression()
logmodel.fit(X_train, y_train)
predictions=logmodel.predict(X_test)
print(predictions)
from sklearn.metrics import classification_report
print(classification_report(y_test,predictions))
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test,predictions))
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,predictions))
