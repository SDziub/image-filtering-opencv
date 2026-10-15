import cv2 as cv
import numpy as np

obraz=cv.imread(Neuvillette.png)
if obraz is None:
    print("Nie udało się wczytać obrazu.")
    exit()

#rozmycie
kernel1=np.arry([
    [1,1,1],
    [1,1,1],
    [1,1,1]
], dtype=np.float32)/9
#wyostrzenie
kernel2 = np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
], dtype=np.float32)

kernel3 = np.array([
    [1,2,1],
    [2,4,2],
    [1,2,1]
], dtype=np.float32)

kernel4 = np.array([
    [-1,0,1],
    [-2,0,2],
    [-1,0,1]
], dtype=np.float32)

kernel5 = np.array([
    [-1,-2,-1],
    [0,0,0],
    [1,2,1]
], dtype=np.float32)

wynik=cv.filter2D(obraz,-1,kernel1)
cv.imshow("Oryginał", obraz)
cv.imshow("Po filtrowaniu", wynik)

cv.imwrite("wynik.jpg",wynik)
cv.waitKey(0)
cv.destroyAllWindows()