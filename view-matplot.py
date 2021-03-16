import math, random, keyboard
from time import sleep
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#AREA FINDER - Functions that return the area of triangle defined by three points in 3D space

# For Horizontal Area
def tri_area_h(p1,p2,p3):
          a = ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**(1/2)
          b = ((p2[0]-p3[0])**2 + (p2[1]-p3[1])**2)**(1/2)
          c = ((p3[0]-p1[0])**2 + (p3[1]-p1[1])**2)**(1/2)
          s = (a + b + c)/2
          return round((abs((s)*(s-a)*(s-b)*(s-c)))**(1/2),10)
# For Vertical Area
def tri_area_v(p1,p2,p3):
          a = ((p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)**(1/2)
          b = ((p2[1]-p3[1])**2 + (p2[2]-p3[2])**2)**(1/2)
          c = ((p3[1]-p1[1])**2 + (p3[2]-p1[2])**2)**(1/2)
          s = (a + b + c)/2
          return round((abs((s)*(s-a)*(s-b)*(s-c)))**(1/2),10)

#VIEW WINDOW - Defined as a Triangle horizontally and vertically
origin = [0,0,0]
v1 = [-1,1,0]
v2 = [1,1,0]
v3 = [0,1,1]
v4 = [0,1,-1]


# Stores the Area of the View Window
view_window_area_h = tri_area_h(origin,v1,v2)
view_window_area_v = tri_area_v(origin,v3,v4)

#3D OBJECTS - This section defines 3D geometry

object_res = 0.05 # The resolution at which lines and planes are drawn, defined by the horizontal/vertical distance between two adjacent points


point_array = [] # The Array that holds ALL points in the engine


#Line Function: interpolates the distance between two points in 3D space, and draws additional points inbetween based off the object resolution set earlier. Interpolation happens
# independently for x, y, and z components of each point.

def line(p1,p2):
          points = [p1]
          inter = int(round((( (p1[0]-p2[0])**2 +(p1[1]-p2[1])**2 +(p1[2]-p2[2])**2  )**(1/2))/object_res))
          #X
          if (p1[0] != p2[0]):
                    diff_x = (p2[0]-p1[0])/inter
          else:
                    diff_x = 0
          #Y
          if (p1[1] != p2[1]):
                    diff_y = (p2[1]-p1[1])/inter
          else:
                    diff_y = 0
          #Z
          if (p1[2] != p2[2]):
                    diff_z = (p2[2]-p1[2])/inter
          else:
                    diff_z = 0             
          for i in range(inter):
                    point = [(p1[0]+diff_x*(i+1)),(p1[1]+diff_y*(i+1)),(p1[2]+diff_z*(i+1))] # This line function appends directly to the full point array to be used immediately
                    point_array.append(point)
def linep(p1,p2):
          points = []
          inter = int(round((( (p1[0]-p2[0])**2 +(p1[1]-p2[1])**2 +(p1[2]-p2[2])**2  )**(1/2))/object_res))
          #X
          if (p1[0] != p2[0]):
                    diff_x = (p2[0]-p1[0])/inter
          else:
                    diff_x = 0
          #Y
          if (p1[1] != p2[1]):
                    diff_y = (p2[1]-p1[1])/inter
          else:
                    diff_y = 0
          #Z
          if (p1[2] != p2[2]):
                    diff_z = (p2[2]-p1[2])/inter
          else:
                    diff_z = 0             
          for i in range(inter):
                    point = [(p1[0]+diff_x*(i+1)),(p1[1]+diff_y*(i+1)),(p1[2]+diff_z*(i+1))] # This variation of the line function is used during the Plane Generation function, and does NOT
                    points.append(point)                                                     # append directly to the point array
          return points

def plane(p1,p2,p3,p4): # This function renders a plane between 4 given points in 3D space by interpolating with lines
          L1 = linep(p1,p2)
          L2 = linep(p3,p4)
          if (len(L1) == len(L2)):
                    for index,point in enumerate(L1):
                              line(point,L2[index])
          for point in (L1+L2):
                    point_array.append(point)


# This section defines the physical geometry we want present in the 3D space
p = 0.2 # height of demo object
di = 0.20 # width of demo object
a = [-di,0.4,-p]
b = [-di,0.8,-p]
c = [di,0.8,-p]
d = [di,0.4,-p]

e = [-di,0.4,p]
f = [-di,0.8,p]
g = [di,0.8,p]
h = [di,0.4,p]


point_array.append(a)
point_array.append(b)
point_array.append(c)
point_array.append(d)
point_array.append(e)
point_array.append(f)
point_array.append(g)
point_array.append(h)

line(a,b)
line(b,c)
line(c,d)
line(d,a)
line(e,f)
line(f,g)
line(g,h)
line(h,e)
line(a,e)
line(b,f)
line(d,h)
line(c,g)

plane(e,f,h,g)
plane(a,b,e,f)
plane(c,d,g,h)
plane(a,b,d,h)
#plane(b,c,f,g)


#Line Check H and V returns TRUE if p1,p2,p3 all lie on the same line in 3d space, non-diagonally
def line_check_h(p1,p2,p3):
          if (p1[0] == p2[0]):
                    if (p3[0] != p1[0]):
                              return True
                    else:
                              return False
          elif (p1[1] == p2[1]):
                    if (p3[1] != p1[1]):
                              return True
                    else:
                              return False
          else:
                    if (p1[0] != p3[0] and p2[0] != p3[0]):
                              if ((p1[1]-p2[1])/(p1[0]-p2[0]) != (p1[1]-p3[1])/(p1[0]-p3[0])):
                                        return True
                              else:
                                        return False
                    else:
                              if (p1[1] != p3[1] and p2[1] != p3[1]):
                                        return True
                              else:
                                        return False
def line_check_v(p1,p2,p3):
          if (p1[1] == p2[1]):
                    if (p3[1] != p1[1]):
                              return True
                    else:
                              return False
          elif (p1[2] == p2[2]):
                    if (p3[2] != p1[2]):
                              return True
                    else:
                              return False
          else:
                    if (p1[1] != p3[1] and p2[1] != p3[1]):
                              if ((p1[2]-p2[2])/(p1[2]-p2[2]) != (p1[2]-p3[2])/(p1[1]-p3[1])):
                                        return True
                              else:
                                        return False
                    else:
                              if (p1[2] != p3[2] and p2[2] != p3[2]):
                                        return True
                              else:
                                        return False

#Domain Check H and V return True if the point passed lies within the view window area, and is eligable to be rendered by the engine
def domain_check_h(point):
          #Line Check
          if (line_check_h(origin,v1,point) == True and line_check_h(origin,v2,point) == True and line_check_h(v1,v2,point) == True):
                    #print('LineH Check')
                    #Area Check
                    if ( (round((tri_area_h(origin,v1,point) + tri_area_h(origin,v2,point) + tri_area_h(v1,v2,point)),9)) ==
                         view_window_area_h):
                              return True
                    else:
                              return False
          else:
                    return False

def domain_check_v(point):
          #Line Check
          if (line_check_v(origin,v3,point) == True and line_check_v(origin,v4,point) == True and line_check_v(v3,v4,point) == True):
                    #Area Check
                    #print('LineV Check')
                    if ((round((tri_area_v(origin,v3,point) + tri_area_v(origin,v4,point) + tri_area_v(v3,v4,point)),9)) ==
                         view_window_area_v):
                              return True
                    else:
                              #print((round((tri_area_v(origin,v3,point) + tri_area_v(origin,v4,point) + tri_area_v(v3,v4,point)),10)),view_window_area_v)
                              return False
          else:
                    return False

#Horizontal and Vertical uses an algebraic method to determine the horizontal and vertical positioning of the point to be rendered on the viewing screen
def horizontal(point):
          v1_a = ((origin[0]-v1[0])**2 + (origin[1]-v1[1])**2)**(1/2)
          v1_b = ((v1[0]-point[0])**2 + (v1[1]-point[1])**2)**(1/2)
          v1_c = ((point[0]-origin[0])**2 + (point[1]-origin[1])**2)**(1/2)
          v1_s = (v1_a+v1_b+v1_c)/2
          v1_area = tri_area_h(origin,v1,point)

          v2_a = ((origin[0]-v2[0])**2 + (origin[1]-v2[1])**2)**(1/2)
          v2_b = ((v2[0]-point[0])**2 + (v2[1]-point[1])**2)**(1/2)
          v2_c = ((point[0]-origin[0])**2 + (point[1]-origin[1])**2)**(1/2)
          v2_s = (v2_a+v2_b+v2_c)/2
          v2_area = tri_area_h(origin,v2,point)

          #horizontal_position = round((res[0])*((v1_area)/(v1_area+v2_area)))
          horizontal_position = (v1_area)/(v1_area+v2_area)
          return horizontal_position

def vertical(point):
          v3_a = ((origin[1]-v3[1])**2 + (origin[2]-v3[2])**2)**(1/2)
          v3_b = ((v3[1]-point[1])**2 + (v3[2]-point[2])**2)**(1/2)
          v3_c = ((point[1]-origin[1])**2 + (point[2]-origin[2])**2)**(1/2)
          v3_s = (v3_a+v3_b+v3_c)/2
          v3_area = tri_area_v(origin,v3,point)

          v4_a = ((origin[1]-v2[1])**2 + (origin[2]-v2[2])**2)**(1/2)
          v4_b = ((v2[1]-point[1])**2 + (v2[2]-point[2])**2)**(1/2)
          v4_c = ((point[1]-origin[1])**2 + (point[2]-origin[2])**2)**(1/2)
          v4_s = (v4_a+v4_b+v4_c)/2
          v4_area = tri_area_v(origin,v4,point)

          #vertical_position = round((res[1])*((v3_area)/(v3_area+v4_area)))
          vertical_position = (v3_area)/(v3_area+v4_area)
          return vertical_position

#rotate_h is a passive function that rotates all points around the center specified, is called once per frame rendered
def rotate_h(point,center,degree):

          new_pos = [( (point[0]-center[0])*math.cos(degree)-(point[1]-center[1])*math.sin(degree) + center[0]  ),( (point[0]-center[0])*math.sin(degree) + (point[1]-center[1])*math.cos(degree) + center[1]  ),(point[2])]

          point[0] = new_pos[0]
          point[1] = new_pos[1]
          point[2] = new_pos[2]


#Motion allows for user input to controll the viewing angle and distance inside the engine
def motion(step,middle,rstep):
          points = [origin,v1,v2,v3,v4]
          if keyboard.is_pressed('a'):
                    for point in points:
                              point[0] += -step
          elif keyboard.is_pressed('d'):
                    for point in points:
                              point[0] += step
          elif keyboard.is_pressed('s'):
                    for point in points:
                              point[1] += -step
          elif keyboard.is_pressed('w'):
                    for point in points:
                              point[1] += step
          elif keyboard.is_pressed('up'):
                    for point in points:
                              point[2] += -step
          elif keyboard.is_pressed('down'):
                    for point in points:
                              point[2] += step
          elif keyboard.is_pressed('left'):
                    for point in point_array:
                              rotate_h(point,middle,-rstep)
          elif keyboard.is_pressed('right'):
                    for point in point_array:
                              rotate_h(point,middle,rstep)

#Render and Animate collect and draw the points to be rendered every frame
def render(i):
          xs = []
          ys = []
          xs.append(0.0)
          xs.append(1)
          ys.append(0)
          ys.append(1)
          motion(0.01,[0,0.6,0],0.05)
          for point in point_array:
                    rotate_h(point,[0,0.6,0],0.015)
                    
                    if (domain_check_h(point) == True and domain_check_v(point) == True):
                              two = [horizontal(point),vertical(point)]
                              xs.append(horizontal(point))
                              ys.append(vertical(point))
          ax1.clear()
          ax1.plot(xs,ys,'w+')

def animate():
    fig = plt.figure(figsize=(8,8))
    fig.set_facecolor('#000000')
    global ax1
    ax1 = fig.add_subplot(1,1,1)
    ax1.set_facecolor('#000000')
    ani = animation.FuncAnimation(fig,render,interval=1)
    plt.show()
    
animate()

