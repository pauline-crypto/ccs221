#Activity 1 by Pauline Joy O. Bautista
#Python program for DDA Line.
import streamlit as st
import matplotlib.pyplot as plt

plt.title('DDA Line Algorithm + Midpoint')
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

def DDALine(x1, y1, x2, y2, color):
    dx = x2 - x1
    dy = y2 - y1

    # calculate steps required for generating pixels 
   
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
         
    #calculate increment in x & y for each steps
    Xinc = float(dx / steps)
    Yinc = float(dy / steps)
    
    #midpoint
    mx = (x2+x1)/2
    my = (y2+y1)/2
    print ('Midpoint is:', mx, ',', my)
    plt.plot (mx, my, marker="o", markerfacecolor='blue')
    
    for i in range(0, int(steps + 1)):
		 # Draw pixels
        plt.plot(int(x1), int(y1), color)
        x1 += Xinc
        y1 += Yinc
    st.pyplot(plt)


def main():
    x1 = st.sidebar.slider("X1", -100, 100, 0)
    y1 = st.sidebar.slider("Y1", -100, 100, 0)
    x2 = st.sidebar.slider("X2", -100, 100, 0)
    y2 = st.sidebar.slider("Y2", -100, 100, 0)
    color = "r."
    DDALine(x1, y1, x2, y2, color)


if __name__ == '__main__':
    main()
