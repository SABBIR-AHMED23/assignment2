import sympy as sp
from sympy.vector import CoordSys3D, curl
R = CoordSys3D('R')
x, y, z = R.x, R.y, R.z

F = 2*z*R.i + 3*x*R.j + 5*y*R.k
curl_F = curl(F)
print(curl_F)
# Surface: z = 4 - x^2 - y^2 → upward normal
r, theta = sp.symbols('r theta')
x_p = r * sp.cos(theta)
y_p = r * sp.sin(theta)
z_p = 4 - r**2

# Position vector
r_vec = x_p * R.i + y_p * R.j + z_p * R.k

# Partial derivatives
r_r = sp.diff(r_vec, r)
r_theta = sp.diff(r_vec, theta)

# Surface normal = cross product
n = r_r.cross(r_theta)
print(n)
# Substitute coordinates
curl_subs = curl_F.to_matrix().subs({x: x_p, y: y_p, z: z_p})
n_vec = n.to_matrix()
dot_product = sum(a*b for a, b in zip(curl_subs, n_vec))

dS = r
surface_integral = sp.integrate(sp.integrate(dot_product * dS, (r, 0, 2)), (theta, 0, 2*sp.pi))
print("Surface integral (Stokes):", surface_integral.evalf())
