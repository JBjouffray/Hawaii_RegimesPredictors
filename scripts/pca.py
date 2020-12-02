
# Principal Component Analysis

PCA is used to reduce the number of variables of a data set, while preserving as much information as possible

### General Dependacies

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import normalize
from sklearn.decomposition import PCA

df = pd.read_csv('/content/drive/My Drive/SMA project/Hawaiian_Predictors_revised.csv')
X = df.iloc[:,4:-1].values
y = df.iloc[:,32].values

scaler = StandardScaler()
scaler.fit(X)
X=scaler.transform(X)

pca = PCA(n_components=2)
pc = pca.fit(X).transform(X)

pc_reg1 = pc[y==1]
pc_reg2 = pc[y==2]
pc_reg3 = pc[y==3]
pc_reg5 = pc[y==5]

"""### Pairwise PCA"""

print('Pairwise principal component analysis of the regimes \n')
figure(num=None, figsize=(15, 30), dpi=80, facecolor='w', edgecolor='k')

plt.subplot(6,2,1)
plt.scatter(pc_reg1[:,0],pc_reg1[:,1],label='regime 1',color = 'navy')
plt.scatter(pc_reg2[:,0],pc_reg2[:,1],label='regime 2',color = 'mediumvioletred')
plt.title('Regime1 vs Regime2')
plt.legend()

plt.subplot(6,2,2)
plt.scatter(pc_reg1[:,0],pc_reg1[:,1],label='regime 1',color = 'navy')
plt.scatter(pc_reg3[:,0],pc_reg3[:,1],label='regime 3',color = 'lightcoral')
plt.title('Regime1 vs Regime3')
plt.legend()

plt.subplot(6,2,3)
plt.scatter(pc_reg1[:,0],pc_reg1[:,1],label='regime 1',color = 'navy')
plt.scatter(pc_reg5[:,0],pc_reg5[:,1],label='regime 5',color = 'moccasin')
plt.title('Regime1 vs Regime5')
plt.legend()

plt.subplot(6,2,4)
plt.scatter(pc_reg2[:,0],pc_reg2[:,1],label='regime 2',color = 'mediumvioletred')
plt.scatter(pc_reg3[:,0],pc_reg3[:,1],label='regime 3',color = 'lightcoral')
plt.title('Regime2 vs Regime3')
plt.legend()

plt.subplot(6,2,5)
plt.scatter(pc_reg2[:,0],pc_reg2[:,1],label='regime 2',color = 'mediumvioletred')
plt.scatter(pc_reg5[:,0],pc_reg5[:,1],label='regime 5',color = 'moccasin')
plt.title('Regime2 vs Regime5')
plt.legend()

plt.subplot(6,2,6)
plt.scatter(pc_reg3[:,0],pc_reg3[:,1],label='regime 3',color = 'lightcoral')
plt.scatter(pc_reg5[:,0],pc_reg5[:,1],label='regime 5',color = 'moccasin')
plt.title('Regime3 vs Regime5')
plt.legend()
plt.show()

"""### Combined PCA"""

print('\n Combined principal component analysis of the regimes \n')
figure(num=None, figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')
plt.scatter(pc_reg1[:,0],pc_reg1[:,1],label='regime 1',color = 'navy')
plt.scatter(pc_reg2[:,0],pc_reg2[:,1],label='regime 2',color = 'mediumvioletred')
plt.scatter(pc_reg3[:,0],pc_reg3[:,1],label='regime 3',color = 'lightcoral')
plt.scatter(pc_reg5[:,0],pc_reg5[:,1],label='regime 5',color = 'moccasin')
plt.legend()
plt.show()
