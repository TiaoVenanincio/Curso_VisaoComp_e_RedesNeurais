# Seção 5 - Redes Neurais Para Classificação de Imagens

## Intuição sobre redes neurais artificiais
- Neurônio aritifial: Entradas, pesos, função soma e função de ativação

## Função soma, ativação e ajuste de pesos
- Função soma: Somatório de (entradas * pesos)
- Função de ativação (step): retorna 0 ou 1
- Ajuste de pesos: peso(n+1) = peso(n) + (taxaAprendizagem * entrada * erro)
- Intuição de uma rede neural para operador AND (uma camada)
- Função Sigmoid: y = 1 / (1 + e^(-x))
- Se x for alto, o valor será aprox. 1, se for baixo, o valor será aprox. 0
- Intuição de uma rede neural para um operador XOR (multicamada)

## Calculo do erro, descida do gradiente e parâmetro delta
- Erro =  RepostaCorreta - RepostaCalculada. A tendência é diminuir.
- Na prática, o erro é calculado com MSE e RMSE (Mean Square error e Root mean square error)
- Descida do gradiente: Chegar ao menor erro possível
- Para a decida do gradiente, pode-se usar batch gadrient descent (BGD), stochastic gradient descent (SGD) ou mini batch gradient descent (MBGD)
- SGD: Ajuda a previnir mínimos locais
- MBGD: Escolhe um número de registros para rodar e atualizar os pesos. Parâmetros: Learning rate, batch size, epochs
- A derivada pacial no gradiente é calculada para ajustar os pesos
- Derivada: d = y * (1-y)
- DeltaSaída = erro * DerivadaSigmoide (da função de ativação)
- DeltaCamadaEscondida = DerivadaSigmoide * peso * DeltaSaída

## Ajustes dos pesos com backpropagation
- Peso(n+1) = (peso(n) * momento) + (entrada * delta * taxa de aprendizagem)
- Vvariável 'momento' é utilizada para acelerar o processo

## Bias
- Evita que ocorra o mesmo resultado na saída com base na entrada. Adiciona um neurônio na entrada e uma unidade para a camada de saída.

## Redes neurais usando todos os pixels das imagens
-

## Extração de caracteristicas com o OpenCV
-

## Redes neurais usando as caracteristicas das imagens
-


Link para o Colab: https://colab.research.google.com/drive/1VeuEQldsatm9kogGzlE_lcha6IgnOhMl?usp=sharing
