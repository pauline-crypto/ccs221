import numpy as np
import cv2
import streamlit as st

def read_image(filename):
    img = cv2.imread(filename)
    print('Image shape:', img.shape)
    print('Image contents:', img)
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


def reflect_image(img):
    rows, cols, ch = img.shape
    m_reflection=np.float32([[1, 0, 0], [0,-1,rows],[0,0,1]])
    reflected_img=cv2.warpPerspective(img,m_reflection,(int(cols),int(rows)))
    st.image(reflected_img, use_column_width=True, caption='Reflected Image')

def rotate_image(img, angle):
    rows, cols, ch = img.shape
    angle = np.radians(angle)
    m_rotation = np.float32([[np.cos(angle), -np.sin(angle), 0], [np.sin(angle), np.cos(angle), 0], [0, 0, 1]])
    rotated_img = cv2.warpPerspective(img, m_rotation, (cols, rows))
    st.image(rotated_img, use_column_width=True, caption='Rotated Image')

def shear_image(img, shear_factor):
    rows, cols, ch = img.shape
    m_shearing = np.float32([[1, shear_factor, 0], [0, 1, 0], [0, 0, 1]])
    sheared_img = cv2.warpPerspective(img, m_shearing, (int(cols * (1 + abs(shear_factor))), rows))
    st.image(sheared_img, use_column_width=True, caption='Sheared Image')

def translate_image(img, x_offset, y_offset):
    rows, cols, channels = img.shape
    M = np.float32([[1, 0, x_offset], [0, 1, y_offset]])
    translated_img = cv2.warpAffine(img, M, (cols, rows))
    st.image(translated_img, use_column_width=True, caption='Translated Image')

def scale_image(img):
    rows, cols, ch = img.shape
    m_scaling_ = np.float32([[1.5, 0, 0],[0, 1.8, 0], [0,0,1]])
    scaled_img_ = cv2.warpPerspective(img, m_scaling_, (cols*2, rows*2))
    st.image(scaled_img_, use_column_width=True, caption='Scaled Image')

images = ['original1.jpg', 'original2.jpg', 'original3.jpg']

for filename in images:
    img = read_image(filename)
    reflect_image(img)
    rotate_image(img, 10)
    shear_image(img, 0.5)
    translate_image(img, 100, 50)
    scale_image(img)
