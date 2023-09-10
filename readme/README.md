# Desafio de Previsão de Segurança em Regiões Turísticas

Tendo em vista este contexto, uma cidade turística do Brasil disponibilizou dados de crimes contra o patrimônio (roubos e furtos), coletados diariamente durante os últimos 12 meses, os quais devem ser utilizados para a construção de um modelo capaz de prever se os turistas estão ou não estão em regiões perigosas e sujeitas a pequenos delitos. A planilha de treinamento fornecida tem 8000 instâncias (linhas) e 20 características das instâncias (colunas).

![Exemplo dos dados de treinamento](https://s3-sa-east-1.amazonaws.com/datagateway-prod/images/F5A-OPy4EXcdVzBT8Nr-mXHCFX-Mh14Y7TqpLbMLHRCPqzt8xzN5px1odRXaKnQAH5x4X1h42toq2X2UsZhwiExhgNy5WMs7QPd4TOPuoAHuVeK0IvK107WSZMXSyjAg.jpg)

## Dados

A Figura 1 apresenta um pedaço do conjunto de treinamento. A coluna id identifica cada uma das instâncias individualmente, apresentando valores de 0 a 5600. A coluna target apresenta valores 1 para instâncias que representam regiões perigosas, caso contrário, apresenta valores 0 para instâncias que representam regiões não perigosas. As outras colunas, contendo números reais, representam dados das regiões que devem embasar a decisão.

Após treinar o seu modelo, você deve realizar a predição na planilha de teste. A planilha de teste fornecida tem 2400 instâncias (linhas) e 20 características das instâncias (colunas). Ela contém informações semelhantes à planilha de treinamento, mas é fornecida sem os rótulos, ou seja, se as regiões são ou não são perigosas.

![Exemplo dos dados de teste](https://s3-sa-east-1.amazonaws.com/datagateway-prod/images/jDu2tnVbR6ZDDM92gjxgzggzebndG53anjcUTabYYwxAWxo08uXVfu-nRLs2tSCyZFi4syEAYG8yu_ad950maJbRrkmO9cFtIB4USSa7sHqN6wLGKIXsjpblOrsghD98.jpg)

## Submissão

Quando você julgar que criou um modelo competitivo, envie suas predições pelo aplicativo utilizando um arquivo com a extensão .csv com exatamente 2400 linhas e 2 colunas, uma linha para cada instância de teste. A primeira coluna de cada linha deve conter o Id da instância e a segunda coluna a Predição para esta instância. Este arquivo deve seguir o seguinte formato:
gi