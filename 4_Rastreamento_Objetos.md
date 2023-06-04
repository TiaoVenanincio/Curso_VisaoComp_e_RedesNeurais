# Seção 4 -  Rastreamento de Objetos

## Tópicos desta seção:

### Rastreamento de objetos x Deteção de objetos
- Rastreamento: Detecta e segue o objeto durante o vídeo
- Detecção: Apenas aponta se há ou não o objeto na imagem ou vídeo

### KCF (Kernel Correlation Filters)
- Mais rápido, mas com qualidade menor
- Utiliza retangulos em volta do objeto para fazer o rastreamentro frame a frame
- Estes retangulos possuem um ciclo, um maior, em seguida um médio, por fim um menor
- Assim é feito o rastreamento dentro destas áreas

### CSRT (Discriminative Correlation Filter with Channel and Spatial Reliability)
- Mais lento, mas com qualidade maior
- Utiliza informações sobre os pixel da imagem onde está marcado o objeto a ser rastreado
- Utiliza HOG para extrair informações uteis sobre a imagem
- Utiliza Random Markov Test para gerar probabilidades da movimentação do objeto