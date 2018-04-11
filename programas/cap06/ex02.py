import cv2

imgOriginal = cv2.imread("moedas.jpeg")
imgTratada = cv2.GaussianBlur(imgOriginal, (5,5), 0)

cv2.imshow("Original", imgOriginal)
cv2.imshow("Tratada", imgTratada)

cv2.waitKey(0)
cv2.destroyAllWindows()