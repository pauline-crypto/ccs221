import numpy as np
import cv2
import streamlit as st

def read_image(filename):
    img = cv2.imread(filename)
    if img is None:
        st.error("Error: Image file not found or could not be read.")
        return None
    else:
        return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def translate_image(img, tx_new, ty_new):
    rows, cols = img.shape[:2]
    M = np.float32([[1, 0, tx_new], [0, 1, ty_new]])
    translated_img = cv2.warpAffine(img, M, (cols, rows))
    return translated_img

def main(): 
    img = read_image("original.jpg")
    if img is None:
        return

    tx, ty = 0, 0

    while True:
        tx_new = st.text_input("Enter new x coordinate or press 1 to exit: ")
        if tx_new == "1":
            st.write("Thank you!")
            break

        ty_new = st.text_input("Enter new y coordinate: ")
        tx += int(tx_new)
        ty += int(ty_new)
        transformed_img = translate_image(img, tx, ty)
        st.image(transformed_img)

if __name__ == '__main__':
    main()
