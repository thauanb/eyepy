import cv2
import pytesseract

def readImg(file:str , LANG_TYPE="por"):
  imagem = cv2.imread(file)
  caminho = r"C:\Program Files\Tesseract-OCR"
  pytesseract.pytesseract.tesseract_cmd = caminho + r'\tesseract.exe'
  imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
  _, imagem_binaria = cv2.threshold(imagem_cinza, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
  texto = pytesseract.image_to_string(imagem_binaria,lang=LANG_TYPE)
  if (texto):
    print('[+] Imagem Lida : \n')
    print(texto)
  return texto    

readImg('ex1.png')

