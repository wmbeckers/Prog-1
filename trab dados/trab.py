# importa as bibliotecas necessárias
import numpy as np
import pandas as pd
import seaborn as sns
import sklearn
from sklearn.datasets import fetch_california_housing
import matplotlib.pyplot as plt

# Carrega o conjunto de dados 
california_housing = fetch_california_housing()

# Cria um DataFrame com os dados do conjunto 
df = pd.DataFrame(data=california_housing.data, columns=california_housing.feature_names)
df['MedHouseVal'] = california_housing.target

# Descreve estatísticas básicas do DataFrame
description = df.describe()
print(description)

# Calcula as  métricas estatísticas
metricas = df[['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup']].agg(['mean', 'median', lambda x: x.mode()[0], 'var', 'std', 'quantile'])
# Calcula o IQR
metricas.loc['IQR'] = df[['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup']].quantile(0.75) - df[['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup']].quantile(0.25)

print(metricas)

# Cria um gráfico de dispersão da latitude e longitude
sns.scatterplot(x='Longitude', y='Latitude', data=df, hue='MedHouseVal', palette='viridis', legend=None)

plt.show()

# Lista de variáveis para análise
variables = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup']

# Gera gráficos de BoxPlot e Histogramas para cada variável na lista
for var in variables:
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    sns.boxplot(y=df[var])
    plt.title(f'BoxPlot de {var}')
    
    plt.subplot(1, 2, 2)
    sns.histplot(df[var], kde=True)
    plt.title(f'Histograma de {var}')
    
    plt.show()