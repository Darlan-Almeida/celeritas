from sklearn.linear_model import  LinearRegression
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
modelo_regressao = LinearRegression()

modelo_regressao.fit(x_treino , y_treino)

y_regressao = modelo_regressao.predict(x_teste)

resultado_regressao = r2_score(y_teste , y_regressao)

erro_quadratico_regressao = mean_squared_error(y_teste , y_regressao)



print("erro quadrado médio: " , erro_quadratico_regressao)
print("r2:" ,resultado)