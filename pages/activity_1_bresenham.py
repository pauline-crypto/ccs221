#Activity 1 by Pauline Joy O. Bautista
#Python program for Bresenham's Line.
import streamlit as st
import matplotlib.pyplot as plt

plt.title('Bresenham Line Algorithm')
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

def bres(x1, y1, x2, y2, color):
    x,y = x1,y1
    dx = abs(x2 - x1)
    dy = abs(y2 -y1)
    a = dy/float(dx)

    if a > 1:
        dx, dy = dy, dx
        x, y = y, x
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    p = 2*dy - dx
    
    # Initialize the plotting points
    xcoordinates = [x]
    ycoordinates = [y]
         
    #calculate increment in x & y for each steps
    for i in range(2, dx + 2):
        if p > 0:
            y = y + 1 if y < y2 else y - 1
            p = p + 2 * (dy - dx)
        else:
            p = p + 2 * dy

        x = x + 1 if x < x2 else x - 1
        
        xcoordinates.append(x)
        ycoordinates.append(y)

    plt.plot(xcoordinates, ycoordinates, color)
    st.pyplot()

def main():
   st.sidebar.title("Bresenham Line Algorithm")
   x = st.sidebar.slider("X1", 0, 100, 50)
   y = st.sidebar.slider("Y1", 0, 100, 50)
   xEnd = st.sidebar.slider("X2", 0, 100, 70)
   yEnd = st.sidebar.slider("Y2", 0, 100, 70)
   color = st.sidebar.color_picker("Choose line color", "#ff0000")
   bres(x, y, xEnd, yEnd, color)

if __name__ == "__main__":
    main()