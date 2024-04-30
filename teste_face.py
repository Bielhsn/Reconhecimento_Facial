import cv2

detector = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
foto = cv2.imread("Pessoas.jpg")

foto_cinza = cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY)
faces_detectadas = detector.detectMultiScale(foto_cinza)
for x, y, l, a in faces_detectadas:
    #arquivo_img, ponto_iniciaL,cor
    foto = cv2.rectangle(foto, (x,y), (x+l, y+a), (0,0,255))

print(faces_detectadas)

cv2.imshow("Pessoas aleatórias",foto)
cv2.waitKey()
