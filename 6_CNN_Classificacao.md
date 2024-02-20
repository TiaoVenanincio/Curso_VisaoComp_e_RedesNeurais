# Seção 6 - Redes Neurais Convoluncionais Para Classificação de Imagens

## Conteúdo teórico sobre o tema:
- Usado para visão computacional
- Ex: Carros autônomos, detecçaõ de obstáculos, pedestres
- Em geral, melhor que SVM
- A convolucional nao usa todas as entradas (todos os pixels)
- Ela aprende quais são as melhores características para extrair
- Trabalha com 4 etapas: operador de convolução, pooling, flattening e construção da rede neural densa

### Operador de convolução:
- Faz uma convolução de pixels da matriz original com um kernel (por exemplo: para detecção de bordas)
- Dessa forma, as características principais são detectadas e preservadas pelo mapa de características
- Função relu: transforma valores negativos em 0, mantem os positivos (detecta melhor os padroes)
- A camada de convolução aplica diferentes kernels para ver qual o melhor


### Pooling
- Após o operador de convolução, pooling seleciona as características mais relevantes (MaxPooling)
- Reduz o mapa de características
- Reduz overfitting e ruídos desnecessários

### Flattening e Construção da Rede Neural Densa
- Pega o mapa de características após o pooling e o transforma em um vetor
- Aplica esse vetor na rede neural densa e segue-se o fluxo de uma rede neural

## Link para o colab:

Link para o Colab: https://colab.research.google.com/drive/17zjXtUgRJ8bdshU1Kb-REO8-c-WdLJOj?usp=sharing