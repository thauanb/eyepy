# OCR com Python utilizando OpenCV e Tesseract

Este é um script simples em Python para realizar a leitura de texto em imagens utilizando a biblioteca OpenCV para processamento de imagens e o Tesseract para reconhecimento óptico de caracteres (OCR).

## Instalação

Certifique-se de ter o Python instalado em seu ambiente. Você também precisará instalar as seguintes bibliotecas:
 - cv2
 - pytesseract ( se for usuário do Windows você deve instalar o Tesseract-OCR)

Você pode encontrar o instalador em: [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract).

Após a instalação, atualize o caminho do executável do Tesseract neste script:

```python
caminho = r"C:\Program Files\Tesseract-OCR"
pytesseract.pytesseract.tesseract_cmd = caminho + r'\tesseract.exe'
```

## Uso

Para utilizar a função readImg, forneça o caminho da imagem como argumento. Você também pode especificar o idioma do texto a ser reconhecido, padrão é "por" (português).

```python
readImg('ex1.png')
```

## Exemplos de Aplicação

 - Extração de texto de imagens: Ideal para extrair informações de documentos digitalizados, recibos, cartões de visita, entre outros.
 - Tradução de texto em imagens: O texto extraído pode ser traduzido para outros idiomas utilizando bibliotecas de tradução como o Google  Translate.
 - Automatização de tarefas: Pode ser integrado em sistemas para automatizar processos que envolvam leitura de documentos ou imagens. Por exemplo, processamento de formulários digitalizados.

Certifique-se de que as imagens fornecidas sejam nítidas e legíveis para melhores resultados.