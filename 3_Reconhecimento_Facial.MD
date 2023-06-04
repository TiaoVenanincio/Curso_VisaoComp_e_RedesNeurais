# Seção 3

Estão sendo apresentados métodos de reconhecimento facial:
    - Algoritmo LBPH - Local Binary Pattern Histogram
        - Parâmetros:
            Raio, vizinhos, grade X e Y
        - Cria um histograma para cada local analisado
        - Depois, gera um histograma geral concatenando os locais

    - Dlib 
        - Detecção de pontos faciais (dlib.shape_predictor)
        - Descritores faciais (utilizando resnet - rede neural convolucional para reconhecimento de imagens)
        - Calculo da distância entre as faces
            - Verifica a similaridade, quanto mais prox. de 0, mais parecido



Link Colab: https://colab.research.google.com/drive/16_MLU_T5pAYkFAX3GALgqHPxpj_VrpV6?usp=sharing