Remanejamento Inteligente de Produtos entre Lojas.


Visão Geral:

Este projeto utiliza Machine Learning para otimizar o remanejamento de produtos entre diferentes lojas. O objetivo é maximizar as vendas, minimizar produtos próximos à data de vencimento e melhorar a eficiência logística.

Estrutura do Repositório:

remanejamento-produtos/
│
├── data/
│   ├── vendas.csv
│   ├── estoque.csv
│   ├── lojas.csv
│   └── produtos.csv
│
├── remanejamento.py
├── requirements.txt
├── README.md
└── LICENSE


## Pré-requisitos:
Python 3.7+
Bibliotecas Python listadas em requirements.txt
Instalação

## Clone o Repositório:

```
git clone https://github.com/GuilhermeBarnekow/remanejamento-produtos.git
```
```
cd remanejamento-produtos
```

Crie um Ambiente Virtual (Opcional but recomendado):

```
python -m venv venv
```

Para ativar (Linux) 

```source venv/bin/activate```

# No Windows:

``` venv\Scripts\activate```


Instale as Dependências:

```
pip install -r requirements.txt
```
Uso


Prepare os Dados:

Coloque os arquivos CSV (vendas.csv, estoque.csv, lojas.csv, produtos.csv) na pasta data/.
Execute o Script de Remanejamento:


```python remanejamento.py``


O script realizará as seguintes etapas:

- Carregamento e Pré-processamento de Dados:
- Conversão de datas.
- Cálculo de dias para vencimento.
- Cálculo de taxa de venda por produto e loja.
- Cálculo de distância geográfica em relação ao centro logístico.
Feature Engineering:
- Criação de variáveis relevantes para a modelagem.
Modelagem Preditiva:
- Treinamento de um modelo de Random Forest para prever demanda futura.
- Avaliação do modelo usando RMSE.
- Identificação de Produtos para Remanejamento:
- Seleção de produtos com alta previsão de vendas, baixo estoque e proximidade de vencimento.
- Otimização de Remanejamento:
- Formulação e resolução de um problema de otimização linear para determinar quantidades ideais a serem transferidas entre lojas.
Principais Componentes do Código
remanejamento.py:
- Importação de Bibliotecas: pandas, numpy, scikit-learn, geopy, pulp.
Funções Principais:
- Calcular Distância Geográfica:

```
from geopy.distance import geodesic

def calcular_distancia(lat, lon, centro_logistico):
    return geodesic(centro_logistico, (lat, lon)).kilometers
```

- Pré-processamento de Dados:
- Conversão de datas.
- Cálculo de dias_para_vencimento.
- Cálculo de taxa_venda.
- Feature Engineering:
- Criação de variáveis como distancia_centro.
Modelagem:
- Treinamento e avaliação do modelo de Random Forest.
Otimização:
- Definição do problema de otimização usando PuLP.
