from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
import pandas as pd

data = pd.read_csv('treino.csv')

#meu conjunto de dados 

x = data.drop('target' , axis=1)

# os rótulos dos meus dados 

y = data.target

# machine learnig

x_treino , x_teste , y_treino , y_teste = train_test_split(x,y)

#instancia de modelo
modelo = DecisionTreeRegressor()

#modelo treino = dados + rotulos
modelo.fit(x_treino , y_treino)

# dados teste
y_arvore_decisao = modelo.predict(x_teste)

# resultado do rótulo nos dados de teste
resultado = r2_score(y_teste , y_arvore_decisao)

print(resultado)
