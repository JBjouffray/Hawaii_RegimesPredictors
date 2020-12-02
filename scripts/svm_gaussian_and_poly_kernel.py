"""
Support Vector Machine Classifiers

SVM is based on the idea of finding a hyperplane that best separates the driving features into different regimes.

Kernel functions give us a more efficient and less expensive way to transform data into higher dimensions, using dot product.

I have chosen to use the Polynomial and RBF kernels as they work well will non-linear data which is what my data is (based on PDP). They are also the most popular kernels used in SVMs.

Poly kernel has less accuracy as compared to RBF kernel which is seen in the classifier reports
"""
### General Dependancies

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

def data_prep(df):
    df = df.astype({"id_spatial": "category", "Island": "category", "Habitat_Modification": "category", 
               "Invasive_Algae": "category", "Regime": "category"})
    return df


def load_coral_data(complete=True, CV=True, convert_to_categorical=True):
    if complete:
        df = pd.read_csv("/content/drive/My Drive/SMA project/Hawaiian_Predictors_revised.csv")
        train = pd.read_csv("/content/drive/My Drive/SMA project/Predictors_revised_train.csv")
        val = pd.read_csv("/content/drive/My Drive/SMA project/Predictors_revised_val.csv")
        test = pd.read_csv("/content/drive/My Drive/SMA project/Predictors_revised_test.csv")

    if convert_to_categorical:
        df = data_prep(df)
        train = data_prep(train)
        val = data_prep(val)
        test = data_prep(test)
        
    if CV:
        train = train.append(val)
        train = train.sample(frac=1).reset_index(drop=True)
        return df, train, test
    
    return df, train, val, test

def get_features_and_response(data):
    features =  data.iloc[:,5:-1].values
    pred_names = data.iloc[:,32].values
    response = data['Regime']
    return features, response, pred_names

def evaluate_performance(test_y, test_pred, print_vals=True):
    cnf_matrix = metrics.confusion_matrix(test_y, test_pred)
    
    class_names=['Regime1', 'Regime2', 'Regime3', 'Regime5']
    cnf_matrix = pd.DataFrame(cnf_matrix, index = class_names,
                  columns = class_names)
    
    sns.heatmap(cnf_matrix, annot=True, cmap="magma" ,fmt='g')
    plt.tight_layout()
    plt.title('Confusion matrix', y=1.1)
    plt.ylabel('Actual label')
    plt.xlabel('Predicted label')
    
    if print_vals :
        count_misclassified = (test_y != test_pred).sum()
        print('Misclassified samples: {}'.format(count_misclassified))
        accuracy = metrics.accuracy_score(test_y, test_pred)
        print('Classification Report:')
        print(metrics.classification_report(test_y, test_pred))

df, train, val, test = load_coral_data(complete=True, CV=False, convert_to_categorical=True)

train_X = train.iloc[:, 5:32]
train_y = train['Regime']

val_X = val.iloc[:, 5:32]
val_y = val['Regime']

pred_names = df.iloc[:, 5:32].columns
pred_names

scaler = StandardScaler()

scaler.fit(train_X.values)
train_X = scaler.transform(train_X.values)
val_X = scaler.transform(val_X.values)

"""### Using the Polynomial kernel

Polynomial kernel is a way of measuring the similarity between two training examples in the SVM
"""

svclassifier_poly = SVC(kernel='poly')  
svclassifier_poly.fit(train_X, train_y)
val_pred_svm_poly = svclassifier_poly.predict(val_X)
evaluate_performance(val_y, val_pred_svm_poly)

"""### Using the Radial Basis Function/Gaussian kernel

Gaussian kernel is a way of measuring the similarity between two training examples in the SVM
"""

svclassifier_gauss = SVC(kernel='rbf')  
svclassifier_gauss.fit(train_X, train_y)  
val_pred_svm_gauss = svclassifier_gauss.predict(val_X)  
evaluate_performance(val_y, val_pred_svm_gauss)
