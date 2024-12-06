 # Detecção de Gatos em um Vídeo

Este projeto utiliza o algoritmo Haar Cascade para detectar gatos (especificamente suas faces) em um vídeo. Ele identifica as faces dos gatos em cada quadro e desenha retângulos ao redor delas.


## Como Executar

1. **Instale a biblioteca CV2**


   ```bash
   pip install opencv-python
   ```

2. **Execute o script**

   ```bash
   python main.py
   ```

3. **Observe o programa**

   - O vídeo será exibido com retângulos verdes destacando os gatos detectados.
   - Pressione a tecla `q` para encerrar a execução.

## Funcionamento do Código

1. **Carregamento do Classificador Haar Cascade:**

   O código utiliza o modelo pré-treinado `haarcascade_frontalcatface.xml`, que já está incluído no OpenCV, para identificar faces de gatos.

2. **Processamento de Vídeo:**

   Cada quadro do vídeo é convertido para escala de cinza, e o modelo Haar Cascade é usado para identificar possíveis gatos.

3. **Exibição do Resultado:**

   As áreas detectadas são destacadas com retângulos verdes, e o vídeo processado é exibido em uma janela.

## Observações

- Para garantir que o vídeo seja carregado corretamente, eu utilizei um caminho absoluto no código.
- A detecção é baseada em faces de gatos. Portanto, o video precisa conter imagens claras e visíveis das faces dos gatos para obter melhores resultados.
