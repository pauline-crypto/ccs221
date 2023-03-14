#Activity 1 by Pauline Joy O. Bautista
#Python program for Bresenham's Line.
import streamlit as st
import matplotlib.pyplot as plt

st.title('Bresenham Line Algorithm')
st.write("Enter the values of x1, y1, x2, y2, and click on the 'Draw' button to draw the line using Bresenham's algorithm.")

def bres(x1, y1, x2, y2):
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
    
    #midpoint
    mx = (x2+x1)/2
    my = (y2+y1)/2
    st.write('Midpoint is:', mx, ',', my)
    fig, ax = plt.subplots()
    ax.plot (mx, my, marker="o", markerfacecolor='blue')
         
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

    ax.plot(xcoordinates, ycoordinates)
    st.pyplot(fig)

def main():
    x1 = st.number_input("Enter X1:", min_value=0, max_value=1000, value=0)
    y1 = st.number_input("Enter Y1:", min_value=0, max_value=1000, value=0)
    x2 = st.number_input("Enter X2:", min_value=0, max_value=1000, value=0)
    y2 = st.number_input("Enter Y2:", min_value=0, max_value=1000, value=0)

    if st.button("Draw"):
        bres(x1, y1, x2, y2)

if __name__ == "__main__":
    main()
