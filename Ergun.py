import numpy as np

print("Ergun Equation")

print("Enter the required data")

P = float(input("Enter the Pressure Drop in Pascal : "))

L = float(input("Enter the Length of Packed Bed :"))

dp = float(input("Enter the diameter of the particle in meters :"))

U = float(input("Enter the Viscosity in Pa.s :"))

u = float(input("Enter the Superficial Velocity in m/s :"))

d = float(input("Enter the Density in kg/m^3 :"))

a1 = (P*dp)/L

a2 = -(150*U*u)/dp

a3 = ((300*U*u)/dp)+(1.75*d*u*u)

a4 = (-(150*U*u)/dp)-1.75*d*u*u

coeff = [a1,a2,a3,a4]

roots = np.roots(coeff)

if roots[0]>0:

    print("The Void Fraction =",roots[0])

elif roots[1]>0:

    print("The Void Fraction =",roots[1])

elif roots[2]>0:

    print("The Void Fraction =",roots[2])

else:

print("Please enter the correct values")
