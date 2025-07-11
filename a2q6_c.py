from scipy.integrate import nquad
import numpy as np
x,y,z=np.symbols('x y z',real=True) # Declare symbols
# Define integrand as a Python function
def integrand(z,y,x):
    return x * np.exp(-y) * np.cos(z)

# Limits for z
# def z_limits(y,x):
#     return [0, 4 - x**2 - y**2]

# # Limits for y
# def y_limits(x):
#     return [0, 1 - x**2]

# # Limits for x
# x_limits = [0,1]

# Perform numerical integration
result, error = nquad(integrand, [[0, 4 - x**2 - y**2], [0, 1 - x**2], [0,1]])

print("Numerical value (scipy):")
print(result)
