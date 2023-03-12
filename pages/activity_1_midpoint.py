#Activity 1 by Pauline Joy O. Bautista
#Python program for Midpoint Line.
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
    plt.show()

def main():
    x = int(input("Enter X1: "))
    y = int(input("Enter Y1: "))
    xEnd = int(input("Enter X2: "))
    yEnd = int(input("Enter Y2: "))
    color = "b."
    MidPoint(x, y, xEnd, yEnd, color)


if __name__ == '__main__':
    main()
    
