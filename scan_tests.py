import cv2

# Carregando a imagem
image = cv2.imread('Foto_2023-12-01_141717.jpg')

# Definindo as coordenadas do recorte (x, y, largura, altura)
x, y, width, height = 100, 80, 300, 250

# Recortando a região da imagem
cropped_image = image[y:y+height, x:x+width]

cv2.rectangle(image, (x, y), (x + width, y + height), (0, 255, 0), 2)

# Mostrando a imagem original e a imagem recortada
cv2.imshow('Imagem Original', image)
cv2.imshow('Imagem Recortada', cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()