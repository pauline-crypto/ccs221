import numpy as np
import cv2
import matplotlib.pyplot as plt

def read_image(filename):
    img = cv2.imread(filename)
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def translate_image(img, tx_new, ty_new):
    rows, cols = img.shape[:2]
    M = np.float32([[1, 0, tx_new], [0, 1, ty_new]])
    translated_img = cv2.warpAffine(img, M, (cols, rows))
    return translated_img

def main(): 
    img = read_image("original.jpg")
    tx, ty = 0, 0

    while True:
        tx_new = int(input("Enter new x coordinate or press 1 to exit: "))
        if tx_new == 1:
            print ("Thank you!")
            break

        ty_new = int(input("Enter new y coordinate: "))
        tx += tx_new
        ty += ty_new
        transformed_img = translate_image(img, tx, ty)
        plt.imshow(transformed_img)
        plt.show()

main()
