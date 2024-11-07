import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.cluster import KMeans
import geopandas as gpd
from geopy.distance import geodesic
import pulp

vendas = pd.read_csv('vendas.csv') 
estoque = pd.read_csv('estoque.csv')  
lojas = pd.read_csv('lojas.csv')  
produtos = pd.read_csv('produtos.csv')  

estoque['dtvencimento'] = pd.to_datetime(estoque['dtvencimento'])
estoque['dias_para_vencimento'] = (estoque['dtvencimento'] - pd.Timestamp.today()).dt.days

vendas['data_venda'] = pd.to_datetime(vendas['data_venda'])
vendas['ano_mes'] = vendas['data_venda'].dt.to_period('M')
taxa_venda = vendas.groupby(['lojaid', 'produtoid'])['quantidade_vendida'].sum().reset_index()

dados = estoque.merge(taxa_venda, on=['lojaid', 'produtoid'], how='left').fillna(0)
dados = dados.merge(lojas, on='lojaid', how='left').merge(produtos, on='produtoid', how='left')

centro_logistico = (latitude_centro, longitude_centro)

def calcular_distancia(lat, lon):
    return geodesic(centro_logistico, (lat, lon)).kilometers

dados['distancia_centro'] = dados.apply(lambda row: calcular_distancia(row['latitude'], row['longitude']), axis=1)


features = ['quantidade_estoque', 'dias_para_vencimento', 'distancia_centro', 'categoria']
X = pd.get_dummies(dados[features], columns=['categoria'])
y = dados['quantidade_vendida']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


modelo = RandomForestRegressor(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)


y_pred = modelo.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f'RMSE: {rmse}')


dados['previsao_venda'] = modelo.predict(X)


# Critérios: alta previsão de vendas, baixo estoque, proximidade de vencimento
criterios = (dados['previsao_venda'] > dados['previsao_venda'].quantile(0.75)) & \
           (dados['quantidade_estoque'] < dados['quantidade_estoque'].quantile(0.25)) & \
           (dados['dias_para_vencimento'] < 30)

produtos_para_remanejar = dados[criterios]

problema = pulp.LpProblem("Remanejamento_de_Produtos", pulp.LpMaximize)

# Definir as variáveis de decisão
# Quantidade de produto a ser remanejado de cada loja para outra
# Por simplicidade, considere remanejar entre lojas dentro do mesmo cluster

# Aqui seria necessário mais detalhes sobre as lojas, clusters, etc.

# Exemplo Simplificado:
# Suponha que temos apenas duas lojas para um produto específico

# Definir as restrições e a função objetivo conforme os dados reais

problema.solve()



