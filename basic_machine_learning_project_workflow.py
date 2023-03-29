# -*- coding: utf-8 -*-
"""basic_machine_learning_project_workflow.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1n_VHsjRWv5yo5Uyz16cpa2_Kx6uSpWBy

# **Basic Machine Learning Project Workflow**

## **Data Evaluation and Data Dictionary**

**Write the Approach in which steps you are going to do the Project**

**Mention the Website where you have took the Data**

**Write the Data Dictionary**

## **Importing the Dependencies**

**Import all the Tools we Need**  
**Regular EDA(Exploratory Data Analysis) and Plotting Libraries**  
import numpy as np  
import pandas as pd  
import matplotlib.pyplot as plt  
import seaborn as sns  

**inline because we want the plots to appear inside the Notebook**  
%matplotlib inline  


**Models from Scikit-Learn**  
from sklearn.linear_model import LogisticRegression  
from sklearn.neighbors import KNeighborsClassifier  
from sklearn.ensemble import RandomForestClassifier  

**Model Evaluations**  
from sklearn.model_selection import train_test_split, cross_val_score  
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV  
from sklearn.metrics import confusion_matrix, classification_report  
from sklearn.metrics import precision_score, recall_score, f1_score

## **Loading the Data and Visualizing**

**Loading the Data**  
df = pd.read_csv("/content/heart-disease.csv")  

**Shape comes in the Form of (Rows, Columns)**  
df.shape  

**df shows the entire data**
df

## **Viewing the Data**

### **head**  
*head shows the first five rows of the Data*  
- df.head()

### **tail**  
*head shows the last five rows of the Data*  
- df.tail()

### **value counts**
*value_counts() helps us to find how many of each class are their*  
- df["target"].value_counts()

### **bar graph plotting**
*plotting a bar graph for the patient who has heart disease or not*  
- df["target"].value_counts().plot(kind="bar", color=["red", "blue"]);

### **info**
*info about he data*  
- df.info()

### **missing values check**
*check if their any missing values*  
- df.isna().sum()

### **describe**
*describe gives numerical values of all our columns*  
- df.describe()

### **crosstab**
*Compare target column to sex column*  
- pd.crosstab(df.target, df.sex)

## **Preparing Graphs**

### **Bar Graph**

*Create a Plot of crosstab*  
- pd.crosstab(df.target, df.sex).plot(kind="bar", figsize=(10, 6), color=["yellow", "orange"])

*title shows the heading of the Plot*  
- plt.title("Heart Disease Frequency for Different Genders")

*xlabel shows the data required below the plot*  
- plt.xlabel("0 = No Heart Disease, 1 = Heart Disease")

*ylabel shows the data required in the side*  
- plt.ylabel("Amount")

*legend shows the data required in the legend*    
- plt.legend(["Female", "Male"])

*shows small ticks between the bars*  
- plt.xticks(rotation=0)

### **Scatter Plot**

*Creating another figure*  
- plt.figure(figsize = (10,6))  

*scatter with positive examples*  
*age where target is 1 and thalach where target is 1*  
- plt.scatter(df.age[df.target==1], df.thalach[df.target==1], c="red")  

*scatter with negative examples*  
*age where target is 0 and thalach where target is 0*
- plt.scatter(df.age[df.target==0], df.thalach[df.target==0], c="blue")  

*Adding some helper information*  
- plt.title("Heart Disease in Function of Age and Max Heart Rate")  
- plt.xlabel("Age")  
- plt.ylabel("Max Heart Rate")  
- plt.legend(["Heart Disease","No Heart Disease"]);

### **Histogram**

*Checking the Distribution of Age Column with Histogram*  
- df.age.plot.hist()

### **Bar Graph 2**

*Make the Crosstab more visual*  
*making a bar plot between chest pain(cp) and target to make different types of chest pain more visible*  
- pd.crosstab(df.cp, df.target).plot(kind="bar", figsize=(10, 6), color=["yellow", "red"])  

*Add some Helper Text*  
- plt.title("Heart Disease Frequency per Chest Pain")
- plt.xlabel("Chest Pain Type")
- plt.ylabel("Amount")
- plt.legend(["No Heart Disease", "Heart Disease"])
- plt.xticks(rotation=0);

### **Corelation Matrix with Heatmap**

*making a corelation matrix*  
- df.corr()

*making correlation matrix a little beautiful*
- corr_matrix = df.corr()  
- fig, ax = plt.subplots(figsize=(15, 10))  

*using heatmap from seaborn*
- ax = sns.heatmap(corr_matrix,  annot=True, linewidth=0.5, fmt=".2f", cmap="RdYlGn");  
- bottom, top = ax.get_ylim()  
- ax.set_ylim(bottom + 0.5, top - 0.5)  


*Negative Correlation: Relationship Between Two Variables in which one variable increases and the other variable Decreases*

## **Machine Learning Modelling**

### **Splitting Data on X and y**

*Split data into column X and y*  

*Delete target column and storing it into X*  
- X = df.drop("target", axis = 1)

*storing only target column in y*
- y = df["target"]

Viewing X and y Data

*Split data into train and Test sets*  
- np.random.seed(42)

*Split data into train and test sets*  
- X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

### **Making a Function for Models**

*putting models in the dictionary*  
- models = {"Logistic Regression" : LogisticRegression(), "KNN" : KNeighborsClassifier(), "Random Forest" : RandomForestClassifier()}

*create a function to fit and score models*  
- def fit_and_score(models, X_train, X_test, y_train, y_test):  
      '''  
      It fits and evaluates machine learing modesl
      models are a dictionary of different Scikit-Learn machinie learning models..  
      X_train : training data with no labels  
      X_test : testing data with no labels  
      y_train : training labels  
      y_test : testing labels  
      '''  
      # setting random seed
      np.random.seed(42)

      # make dictionary to keep model scores
      model_scores = {}

      # loop through models
      for name, model in models.items():
        # fit the model to the data
        model.fit(X_train, y_train)
        # evaluate the model and append its score to model_scores
        model_scores[name] = model.score(X_test, y_test)
      return model_scores

### **Checking Model Scores**

model_scores = fit_and_score(models = models,  
                             X_train = X_train,  
                             X_test = X_test,  
                             y_train = y_train,  
                             y_test = y_test)  
model_scores

**Model Comparison**

- model_compare = pd.DataFrame(model_scores, index=["accuracy"])  
- model_compare.T.plot.bar();

### **Model Storing and Predicting**

*using the Logistic Regression model and storing it in variable known as model*  
- model = LogisticRegression()

*Now using the Logistic Regression Model
training the model with train datasets*
- model.fit(X_train, y_train)

*Accuracy on the Training Data
Predicting on X_train and storing it in variable named X_train_prediction*  
- X_train_prediction = model.predict(X_train)
- training_data_accuracy = accuracy_score(X_train_prediction, y_train)

*printing the accuracy score*  
- print("Accuracy on Training Data: ",training_data_accuracy*100)

*Accuracy on the Test Data*  
*predicting the accuracy on the test Data and storing it in variable X_test_prediction*  
- X_test_prediction = model.predict(X_test)
- test_data_accuracy = accuracy_score(X_test_prediction, y_test)

*printing the accuracy on test data*  
- print("Accuracy on Test Data:", test_data_accuracy*100)

## **Output Prediction**

*We will give the input Data except the target to check wheather it person has heart disease or not*  
- input_data = (57,1,0,130,131,0,1,115,1,1.2,1,1,3)

*Change the input Data to Numpy Array*  
- input_data_as_numpy_array = np.asarray(input_data)

*Reshape the Numpy Arrayas we Predict for only one Instance*  
- input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

- prediction = model.predict(input_data_reshaped)
print(prediction)

if(prediction[0] == 0):  
  print("The Person does not have Heart Disease")  
else:  
  print("The Person has Heart Disease")
"""
