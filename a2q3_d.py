import numpy as np
import matplotlib.pyplot as plt
#Define the function
def T(x,y):
    return 3*x**2*y
def gradient_T(x,y):
    dT_dx=6*x*y
    dT_dy=3*x**2
    return np.array([dT_dx,dT_dy])
#Compute directional derivative 
def directional_derivatives(x,y,direction):
    grad=gradient_T(x,y)
    dierection=direction/np.linalg.norm(direction)
    return np.dot(grad,direction)
#Given point and direction
point=(-1,3/2)
direction=np.array([-1,-1/2])
#Compute and print results
grad_at_point=gradient_T(*point)
dir_deriv=directional_derivatives(*point,direction)
print(f'Gradient at {point}: {grad_at_point}')
print(f'Directional Derivative at {point} in direction {direction}: {dir_deriv}')
#Plot the directional derivatives  over the given region
x_val=np.linspace(-2,0,30)
y_val=np.linspace(0,2,30)
X,Y=np.meshgrid(x_val,y_val)
Z=np.vectorize(lambda x,y:directional_derivatives(x,y,direction))(X,Y)
#Contour plot
plt.contourf(X,Y,Z,levels=20,cmap='coolwarm')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Directional Derivative Contour')
plt.show()