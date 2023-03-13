#Activity 1 by Pauline Joy O. Bautista
#Python program for Midpoint Line.
import streamlit as st
import matplotlib.pyplot as plt 

plt.title('Midpoint Line Algorithm')
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

def MidPoint(x1, y1, x2, y2, color):
    dx = (x2+x1)/2
    dy = (y2+y1)/2
    
    print ('Midpoint is:', dx, ',', dy)
   
    # calculate steps required for generating pixels 
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
         
    #calculate increment in x & y for each steps
    Xinc = float(dx/steps)
    Yinc = float(dy/steps)
    
    for i in range(0, int(steps+1)):
		 # Draw pixels
        plt.plot(float(dx), float(dy), color)
        x1 += Xinc
        y1 += Yinc

    st.pyplot(plt.gcf())

def main():
    x = st.number_input("Enter X1:", value=0)
    y = st.number_input("Enter Y1:", value=0)
    xEnd = st.number_input("Enter X2:", value=0)
    yEnd = st.number_input("Enter Y2:", value=0)
    color = "b."
    MidPoint(x, y, xEnd, yEnd, color)

if __name__ == '__main__':
    main()
