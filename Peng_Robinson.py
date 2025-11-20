import numpy as np

print("Enter the value of pressure in pascal")

p=float(input())

print("Enter the value of temperature in kelvin")

T=float(input())

print("Enter the mole fraction of propane")

x=float(input())

print("Enter the mole fraction of n-butane")

y=float(input())

print("Enter the mole fraction of n-pentane")

z=float(input())

a=(x*1.0228)+(y*1.5045)+(z*2.0717)

b=(x*0.0000562)+(y*0.0000724)+(z*0.00009021)

R=8.314

coefficients = [p,(b*p)-(R*T), -((3*(b**2)*p)+(2*b*R*T)+a), ((b**3)*p)+((b**2)*R*T)-(a*b)]

roots = np.roots(coefficients)

if roots[0]>0:

    print("Molar Volume is",roots[0],"L")

elif roots[1]>0:

    print("Molar Volume is",roots[1],"L")

elif roots[2]>0:

    print("Molar Volume is",roots[2],"L")

else:

    print("invalid input")

