# Hawaiian_RegimePredictors

This repo was forked from JBjouffray/Hawaii_RegimesPredictors for a project in my Statistical Methods and Analysis course. The folders/files added by me as a part of the SMA project are listed under the 'My additions' part of this README. The original README is located at README_JouffaryJB.md.

## Objectives of the project

1. Frame a hypothesis on the basis of Principal Component Analysis of the 4 Coral Reef Regimes
    - perform pairwise PCA and complete PCA with 2 principal components considered
   
2. Perform Exploratory Data Analysis on the dataset after splitting it into training and testing sets
    - ensure that training and testing data is equally spread across all 4 regimes
    - plot the correlation between all the predictors to ensure that none of them are very highly correlated ( possibly drop those that are)
    - ensure that training and testing data is well distributed between the 8 Hawaiian islands
    - plot a Kernel Density Estimation plot for the fish and benthic communities with mean/median markers to visualize composition of each regime
    - plot a Kernel Density Estimation plot for the anthropogenic (human) factors with mean/median markers to visualize theis contribution towards regime formation
    
3. visualize which factors are the most influential in the formation of each regime 
4. To predict which regime may found at a location on the Hawaiian islands based on the factors found there

## My additions
All the work for my project is in the following folders:

- new datasets
- scripts
- media
- report

All the other files from the previous paper have been left in place.
Note: All the datasets used in this project have been uploaded to the respective notebooks from Google Drive and can be found in the 'new datasets' folder.

## What does each script contain

| Script  | Contents  |   
|---|---|
| scripts/train_test_split_ipynb  | Data Preprocessing  |   
| scripts/PCA.ipynb  | Principal Data Analysis to frame a hypothesis  |   
| scripts/Exploratory_Data_analysis.ipynb  | Perform EDA on the datset  |  
| scripts/Baseline_Logistic_Regression.ipynb  | Initial LogReg model  |  
| scripts/Baseline_Logistic_Regression_bestmodel.ipynb  | Best selected LogReg model  |   
| scripts/SVM_polyandgauss  | Support Vector Machine models with Gaussian and Polynomial kernels  |  
|   |   |   
|   |   |   
|   |   |   
