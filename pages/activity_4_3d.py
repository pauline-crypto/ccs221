import numpy as np
#cube
 import matplotlib.pyplot as plt
 from mpl_toolkits.mplot3d import Axes3D
 from matplotlib import cm
 from scipy.spatial import Delaunay

 import tensorflow as tf

 def plt_basic_object(points):
    
     tri=Delaunay(points).convex_hull
    
     fig=plt.figure(figsize=(8,8))
     ax=fig.add_subplot(111, projection='3d')
     S=ax.plot_trisurf(points[:,0], points[:,1], points[:,2], triangles=tri, lw=0.5, color='orange'. shade=True)
     ax.set_facecolor('pink')
    
     ax.set_xlim3d(-5,5)
     ax.set_ylim3d(-5,5)
     ax.set_zlim3d(-5,5)
     plt.show()
    
 def cube(bottom_lower=(-2,-1,-2), side_length=5):
    
     bottom_lower=np.array(bottom_lower)
    
     points=np.vstack([
         bottom_lower,
         bottom_lower + [0, side_length, 0],
         bottom_lower + [side_length, side_length, 0],
         bottom_lower + [side_length, 0, 0],
         bottom_lower + [0, 0, side_length],
         bottom_lower + [0, side_length, side_length],
         bottom_lower + [side_length, side_length, side_length],
         bottom_lower + [side_length, 0, side_length],
         ])
    
     return points

 init_cube = cube(side_length=3)
 points = tf.constant(init_cube, dtype=tf.float32)

 plt_basic_object(points)

 octahedron
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy.spatial import Delaunay
import tensorflow as tf

def plt_basic_object_(points):
    tri=Delaunay(points).convex_hull
    fig=plt.figure(figsize=(8,8))
    ax=fig.add_subplot(111, projection='3d')
    S=ax.plot_trisurf(points[:,0], points[:,1], points[:,2], triangles=tri, shade=True, lw=0.5, color='orange')
    ax.set_xlim3d(-6,6)
    ax.set_ylim3d(-6,6)
    ax.set_zlim3d(-6,6)
    plt.show()

def octahedron_(side=8, bottom_lower=(0, 0,-2)):
    side = side / np.sqrt(2)  
    bottom_lower = np.array(bottom_lower)
    points = np.vstack([
        bottom_lower + [-side, 0, 0],  # bottom left
        bottom_lower + [0, -side, 0],  # bottom right
        bottom_lower + [side, 0, 0],   # top left
        bottom_lower + [0, side, 0],   # top right
        bottom_lower + [0, 0, side],   # front top
        bottom_lower + [0, 0, -side]   # back bottom
    ])
    return points

init_octahedron = octahedron_(side=8)
points = tf.constant(init_octahedron, dtype=tf.float32)

plt_basic_object_(init_octahedron)

#rectangle
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy.spatial import Delaunay
import tensorflow as tf

def plt_basic_object(points):
    
    tri=Delaunay(points).convex_hull
    
    fig=plt.figure(figsize=(8,8))
    ax=fig.add_subplot(111, projection='3d')
    S=ax.plot_trisurf(points[:,0], points[:,1], points[:,2], triangles=tri, shade=True, lw=0.5, color='purple')
    
    ax.set_xlim3d(-5,5)
    ax.set_ylim3d(-5,5)
    ax.set_zlim3d(-5,5)
    plt.show()
    
def rectangle(bottom_lower=(-2,-1,-2), side_lengths=(5, 3, 4)):
    
    bottom_lower=np.array(bottom_lower)
    side_lengths = np.array(side_lengths)
    points=np.vstack([
        bottom_lower,
        bottom_lower + [0, side_lengths[1], 0],
        bottom_lower + [side_lengths[0], side_lengths[1], 0],
        bottom_lower + [side_lengths[0], 0, 0],
        bottom_lower + [0, 0, side_lengths[2]],
        bottom_lower + [0, side_lengths[1], side_lengths[2]],
        bottom_lower + [side_lengths[0], side_lengths[1], side_lengths[2]],
        bottom_lower + [side_lengths[0], 0, side_lengths[2]],
        ])

    return points

init_rectangle = rectangle(side_lengths=(2, 4, 2)) #here we can customize the rectangle
points = tf.constant(init_rectangle, dtype=tf.float32)

plt_basic_object(points)

#pyramid
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial import Delaunay
import tensorflow as tf

def plt_basic_object_(points):
    tri=Delaunay(points).convex_hull
    fig=plt.figure(figsize=(8,8))
    ax=fig.add_subplot(111, projection='3d')
    S=ax.plot_trisurf(points[:,0], points[:,1], points[:,2], triangles=tri, lw=0.5, shade=True, color='yellow')
    ax.set_xlim3d(-6,6)
    ax.set_ylim3d(-6,6)
    ax.set_zlim3d(-6,6)
    plt.show()

def pyramid_(side=6, height=8, bottom_lower=(0, 0, -2)):
    side = side / np.sqrt(2)  
    height = height # calculates the tip
    bottom_lower = np.array(bottom_lower)
    points = np.vstack([
        bottom_lower + [-side, -side, 0], 
        bottom_lower + [side, -side, 0],  
        bottom_lower + [side, side, 0],  
        bottom_lower + [-side, side, 0],  
        bottom_lower + [0, 0, height],     
    ])
    return points

init_pyramid = pyramid_(side=6, height=8)
points = tf.constant(init_pyramid, dtype=tf.float32)

plt_basic_object_(points)