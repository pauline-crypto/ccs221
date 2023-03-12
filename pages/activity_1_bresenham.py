#Activity 1 by Pauline Joy O. Bautista
#Python program for Bresenham's Line.
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

    plt.plot(xcoordinates, ycoordinates)
    plt.show()

def main():
   x = int(input("Enter X1: "))
   y = int(input("Enter Y1: "))
   xEnd = int(input("Enter X2: "))
   yEnd = int(input("Enter Y2: "))
   color = "y."
   bres(x, y, xEnd, yEnd, color)

if __name__ == "__main__":
    main()
    
    