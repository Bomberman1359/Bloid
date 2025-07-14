

import math
from decimal import Decimal, getcontext
getcontext().prec = 50


L = [Decimal('0.04'), Decimal('0.065'), Decimal('0.04'), Decimal('0.065')]




def Dsqrt(x):
   return x.sqrt()




def Dsin(x):
   return Decimal(math.sin(float(x)))




def Dcos(x):
   return Decimal(math.cos(float(x)))




def Datan2(y, x):
   return Decimal(math.atan2(float(y), float(x)))




def Ddegrees(x):
   return Decimal(math.degrees(float(x)))




def Dradians(x):
   return Decimal(math.radians(float(x)))




def kinema_inv(n, Pz):
   Pz = Decimal(str(Pz))
   n = [Decimal(str(v)) for v in n]
   A = (L[0] + L[1]) / Pz
   B = (Pz**2 + L[2]**2 - (L[0]+L[1])**2 - L[3]**2) / (2 * Pz)
   C = A**2 + Decimal('1')
   D = Decimal('2') * (A * B - (L[0] + L[1]))
   E = B**2 + (L[0]+L[1])**2 - L[2]**2
   Pmx = (-D + Dsqrt(D**2 - Decimal('4') * C * E)) / (Decimal('2') * C)
   Pmz = Dsqrt(L[2]**2 - Pmx**2 + Decimal('2') *
               (L[0]+L[1])*Pmx - (L[0]+L[1])**2)


   # --- Leg A ---
   a_m_x = (L[3]/Dsqrt(n[0]**2 + n[2]**2)) * n[2]
   a_m_z = Pz + (L[3]/Dsqrt(n[0]**2 + n[2]**2)) * (-n[0])
   A = (L[0] - a_m_x) / a_m_z
   B = (a_m_x**2 + a_m_z**2 - L[2]**2 - L[0] **
        2 + L[1]**2) / (Decimal('2') * a_m_z)
   C = A**2 + Decimal('1')
   D = Decimal('2') * (A * B - L[0])
   E = B**2 + L[0]**2 - L[1]**2
   ax = (-D + Dsqrt(D**2 - Decimal('4') * C * E)) / (Decimal('2') * C)
   az = Dsqrt(L[1]**2 - ax**2 + Decimal('2')*L[0]*ax - L[0]**2)
   if a_m_z < Pmz:
       az = -az
   theta_a = Decimal('90') - Ddegrees(Datan2(ax - L[0], az))


   # --- Leg B ---
   k = Dsqrt(n[0]**2 + Decimal('3')*n[1]**2 + Decimal('4')*n[2]
             ** 2 + Decimal('2')*Dsqrt(Decimal('3'))*n[0]*n[1])
   b_m_x = (L[3]/k)*(-n[2])
   b_m_y = (L[3]/k)*(-Dsqrt(Decimal('3'))*n[2])
   b_m_z = Pz + (L[3]/k)*(Dsqrt(Decimal('3'))*n[1] + n[0])
   A = -(b_m_x + Dsqrt(Decimal('3'))*b_m_y + Decimal('2')*L[0]) / b_m_z
   B = (b_m_x**2 + b_m_y**2 + b_m_z**2 +
        L[1]**2 - L[2]**2 - L[0]**2) / (Decimal('2')*b_m_z)
   C = A**2 + Decimal('4')
   D = Decimal('2')*A*B + Decimal('4')*L[0]
   E = B**2 + L[0]**2 - L[1]**2
   bx = (-D - Dsqrt(D**2 - Decimal('4')*C*E)) / (Decimal('2')*C)
   by = Dsqrt(Decimal('3')) * bx
   bz = Dsqrt(L[1]**2 - Decimal('4')*bx**2 - Decimal('4')*L[0]*bx - L[0]**2)
   if b_m_z < Pmz:
       bz = -bz
   theta_b = Decimal('90') - \
       Ddegrees(Datan2(Dsqrt(bx**2 + by**2) - L[0], bz))


   # --- Leg C ---
   k = Dsqrt(n[0]**2 + Decimal('3')*n[1]**2 + Decimal('4')*n[2]
             ** 2 - Decimal('2')*Dsqrt(Decimal('3'))*n[0]*n[1])
   c_m_x = (L[3]/k)*(-n[2])
   c_m_y = (L[3]/k)*(Dsqrt(Decimal('3'))*n[2])
   c_m_z = Pz + (L[3]/k)*(-Dsqrt(Decimal('3'))*n[1] + n[0])
   A = -(c_m_x - Dsqrt(Decimal('3'))*c_m_y + Decimal('2')*L[0]) / c_m_z
   B = (c_m_x**2 + c_m_y**2 + c_m_z**2 +
        L[1]**2 - L[2]**2 - L[0]**2) / (Decimal('2')*c_m_z)
   C = A**2 + Decimal('4')
   D = Decimal('2')*A*B + Decimal('4')*L[0]
   E = B**2 + L[0]**2 - L[1]**2
   cx = (-D - Dsqrt(D**2 - Decimal('4')*C*E)) / (Decimal('2')*C)
   cy = -Dsqrt(Decimal('3')) * cx
   cz = Dsqrt(L[1]**2 - Decimal('4')*cx**2 - Decimal('4')*L[0]*cx - L[0]**2)
   if c_m_z < Pmz:
       cz = -cz
   theta_c = Decimal('90') - \
       Ddegrees(Datan2(Dsqrt(cx**2 + cy**2) - L[0], cz))


   return [theta_a, theta_b, theta_c]




def map_xyz_to_normal(x, y, z):
   gain = Decimal('5.0')
   x = Decimal(str(x))
   y = Decimal(str(y))
   z = Decimal(str(z))
   nx = gain * x
   ny = gain * y
   nz = Decimal('1')
   norm = Dsqrt(nx**2 + ny**2 + nz**2)
   return [nx/norm, ny/norm, nz/norm]




def kinema_fwd(theta_a, theta_b, theta_c):
   # Convert angles to radians
   theta_a = Dradians(theta_a)
   theta_b = Dradians(theta_b)
   theta_c = Dradians(theta_c)


   # Calculate joint positions for each leg
   # Leg A (along x-axis)
   a_ax = L[0] + L[1] * Dsin(theta_a)
   a_az = L[1] * Dcos(theta_a)


   # Leg B (120 degrees rotated)
   a_bx = Decimal('-0.5') * (L[0] + L[1] * Dsin(theta_b))
   a_bz = L[1] * Dcos(theta_b)
   a_by = Dsqrt(Decimal('3'))/Decimal('2') * (L[0] + L[1] * Dsin(theta_b))


   # Leg C (240 degrees rotated)
   a_cx = Decimal('-0.5') * (L[0] + L[1] * Dsin(theta_c))
   a_cz = L[1] * Dcos(theta_c)
   a_cy = -Dsqrt(Decimal('3'))/Decimal('2') * (L[0] + L[1] * Dsin(theta_c))


   # Calculate platform connection points
   # Leg A platform point (along x-axis)
   p_ax = a_ax + L[2] * Dsin(Datan2(a_ax - L[0], a_az))
   p_az = a_az + L[2] * Dcos(Datan2(a_ax - L[0], a_az))


   # Leg B platform point
   leg_b_angle = Datan2(Dsqrt(a_bx**2 + a_by**2) - L[0], a_bz)
   denom_b = Dsqrt(a_bx**2 + a_by**2)
   p_bx = a_bx + L[2] * Dsin(leg_b_angle) * (a_bx/denom_b)
   p_by = a_by + L[2] * Dsin(leg_b_angle) * (a_by/denom_b)
   p_bz = a_bz + L[2] * Dcos(leg_b_angle)


   # Leg C platform point
   leg_c_angle = Datan2(Dsqrt(a_cx**2 + a_cy**2) - L[0], a_cz)
   denom_c = Dsqrt(a_cx**2 + a_cy**2)
   p_cx = a_cx + L[2] * Dsin(leg_c_angle) * (a_cx/denom_c)
   p_cy = a_cy + L[2] * Dsin(leg_c_angle) * (a_cy/denom_c)
   p_cz = a_cz + L[2] * Dcos(leg_c_angle)


   # The platform is an equilateral triangle, so the center is the average of the three points
   x = (p_ax + p_bx + p_cx) / Decimal('3')
   y = (p_by + p_cy) / Decimal('3')  # p_ay is 0 since leg A is along x-axis
   z = (p_az + p_bz + p_cz) / Decimal('3')


   # Calculate normal vector from platform orientation
   # Vectors from p_a to p_b and p_a to p_c
   v_ab = [p_bx - p_ax, p_by, p_bz - p_az]
   v_ac = [p_cx - p_ax, p_cy, p_cz - p_az]


   # Cross product to get normal vector
   nx = v_ab[1] * v_ac[2] - v_ab[2] * v_ac[1]
   ny = v_ab[2] * v_ac[0] - v_ab[0] * v_ac[2]
   nz = v_ab[0] * v_ac[1] - v_ab[1] * v_ac[0]


   # Normalize
   norm = Dsqrt(nx**2 + ny**2 + nz**2)
   nx /= norm
   ny /= norm
   nz /= norm


   # Map normal vector back to xyz coordinates (inverse of map_xyz_to_normal)
   gain = Decimal('5.0')
   orig_x = nx * norm / gain
   orig_y = ny * norm / gain


   # --- Z offset correction ---
   # Calculate the z value for zero angles (home position)
   theta_zero = Decimal('0')
   a_ax0 = L[0] + L[1] * Dsin(Dradians(theta_zero))
   a_az0 = L[1] * Dcos(Dradians(theta_zero))
   p_ax0 = a_ax0 + L[2] * Dsin(Datan2(a_ax0 - L[0], a_az0))
   p_az0 = a_az0 + L[2] * Dcos(Datan2(a_ax0 - L[0], a_az0))

   a_bx0 = Decimal('-0.5') * (L[0] + L[1] * Dsin(Dradians(theta_zero)))
   a_bz0 = L[1] * Dcos(Dradians(theta_zero))
   a_by0 = Dsqrt(Decimal('3'))/Decimal('2') * (L[0] + L[1] * Dsin(Dradians(theta_zero)))
   leg_b_angle0 = Datan2(Dsqrt(a_bx0**2 + a_by0**2) - L[0], a_bz0)
   denom_b0 = Dsqrt(a_bx0**2 + a_by0**2)
   p_bx0 = a_bx0 + L[2] * Dsin(leg_b_angle0) * (a_bx0/denom_b0)
   p_by0 = a_by0 + L[2] * Dsin(leg_b_angle0) * (a_by0/denom_b0)
   p_bz0 = a_bz0 + L[2] * Dcos(leg_b_angle0)

   a_cx0 = Decimal('-0.5') * (L[0] + L[1] * Dsin(Dradians(theta_zero)))
   a_cz0 = L[1] * Dcos(Dradians(theta_zero))
   a_cy0 = -Dsqrt(Decimal('3'))/Decimal('2') * (L[0] + L[1] * Dsin(Dradians(theta_zero)))
   leg_c_angle0 = Datan2(Dsqrt(a_cx0**2 + a_cy0**2) - L[0], a_cz0)
   denom_c0 = Dsqrt(a_cx0**2 + a_cy0**2)
   p_cx0 = a_cx0 + L[2] * Dsin(leg_c_angle0) * (a_cx0/denom_c0)
   p_cy0 = a_cy0 + L[2] * Dsin(leg_c_angle0) * (a_cy0/denom_c0)
   p_cz0 = a_cz0 + L[2] * Dcos(leg_c_angle0)

   z_offset = (p_az0 + p_bz0 + p_cz0) / Decimal('3')
   z -= z_offset

   return float(orig_x), float(orig_y), float(z)




# --- Test Example ---
if __name__ == "__main__":
   # Test over a grid of x, y values (meters)
   Pz = Decimal('0.0632')  # Platform height
   # Finer grid: -0.02 to 0.02 in steps of 0.002
   step = Decimal('0.002')
   x_range = [Decimal('-0.02') + i * step for i in range(21)]
   y_range = [Decimal('-0.02') + i * step for i in range(21)]
   z = Pz  # Use platform height for z


   print("x\ty\tz\tThetaA\tThetaB\tThetaC\tFwd_x\tFwd_y\tFwd_z\tErr_x\tErr_y\tErr_z")
   for x in x_range:
       for y in y_range:
           n = map_xyz_to_normal(x, y, z)
           thetas = kinema_inv(n, Pz)
           orig_x, orig_y, fwd_z = kinema_fwd(thetas[0], thetas[1], thetas[2])
           err_x = abs(orig_x - float(x))
           err_y = abs(orig_y - float(y))
           err_z = abs(fwd_z - float(z))
           print(
               f"{float(x):.4f}\t{float(y):.4f}\t{float(z):.4f}\t{float(thetas[0]):.2f}\t{float(thetas[1]):.2f}\t{float(thetas[2]):.2f}\t{orig_x:.4f}\t{orig_y:.4f}\t{fwd_z:.4f}\t{err_x:.4e}\t{err_y:.4e}\t{err_z:.4e}")
