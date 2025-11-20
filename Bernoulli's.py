import math

d = 800

D1 = float(input("Enter Diameter at inlet in meters: "))

D2 = float(input("Enter Diameter at outlet in meters: "))

V1 = float(input("Enter Velocity at inlet in m/s: "))

Z1 = float(input("Enter Elevation at inlet in meters: "))

Z2 = float(input("Enter Elevation at inlet in meters: "))

delta_Z = Z1-Z2

P1 = float(input("Enter Pressure at inlet stream in Pa: "))

A1 = (math.pi/4)*D1*D1

A2 = (math.pi/4)*D2*D2

V2 = (A1*V1/A2)

V12 = V1*V1

V22 = V2*V2

delta_V = V12-V22

g = 9.81

P2 = P1+d*g*delta_Z+((delta_V*d)/2)

print("The pressure at Outlet =",P2,"Pa")
