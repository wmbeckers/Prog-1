import numpy as np
import pandas as pd
import seaborn as sns
import sklearn
from sklearn.datasets import fetch_california_housing
import matplotlib.pyplot as plt

california_housing = fetch_california_housing()

df = pd.DataFrame(data=california_housing.data, columns=california_housing.feature_names)
df['ValorMedioCasa'] = california_housing.target

descricao = df.describe()
print(descricao)

metricas = df[['RendaMed', 'IdadeCasa', 'MediaComodos', 'MediaQuartos', 'Populacao', 'MediaOcupacao']].agg(['media', 'mediana', lambda x: x.mode()[0], 'variancia', 'desvio_padrao', 'quantil'])
metricas.loc['IQR'] = df[['RendaMed', 'IdadeCasa', 'MediaComodos', 'MediaQuartos', 'Populacao', 'MediaOcupacao']].quantile(0.75) - df[['RendaMed', 'IdadeCasa', 'MediaComodos', 'MediaQuartos', 'Populacao', 'MediaOcupacao']].quantile(0.25)

print(metricas)

sns.scatterplot(x='Longitude', y='Latitude', data=df, hue='ValorMedioCasa', palette='viridis', legend=None)

plt.show()

variaveis = ['RendaMed', 'IdadeCasa', 'MediaComodos', 'MediaQuartos', 'Populacao', 'MediaOcupacao']

for var in variaveis:
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    sns.boxplot(y=df[var])
    plt.title(f'BoxPlot de {var}')
    
    plt.subplot(1, 2, 2)
    sns.histplot(df[var], kde=True)
    plt.title(f'Histograma de {var}')
    
    plt.show()