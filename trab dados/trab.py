import numpy as np
import pandas as pd
import seaborn as sns
import sklearn
from sklearn.datasets import fetch_california_housing

california_housing = fetch_california_housing()

df = pd.DataFrame(data=california_housing.data, columns=california_housing.feature_names)
df['MedHouseVal'] = california_housing.target

description = df.describe()
print(description)

metrics = df[['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup']].agg(['mean', 'median', lambda x: x.mode()[0], 'var', 'std', 'quantile'])
metrics.loc['IQR'] = df[['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup']].quantile(0.75) - df[['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup']].quantile(0.25)

metrics.rename(index={metrics.index[2]: 'moda'}, inplace=True)

print(metrics)

sns.scatterplot(x='Longitude', y='Latitude', data=df, hue='MedHouseVal', palette='viridis', legend=None)

import matplotlib.pyplot as plt
plt.show()

variables = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup']

for var in variables:
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    sns.boxplot(y=df[var])
    plt.title(f'BoxPlot de {var}')
    
    plt.subplot(1, 2, 2)
    sns.histplot(df[var], kde=True)
    plt.title(f'Histograma de {var}')
    
    plt.show()