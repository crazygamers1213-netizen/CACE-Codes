import numpy as np

print("Enter the value of Pressure in Pa and value of Volume in m^3")

E = int(input("Enter 1 for pressure , 2 for volume"))



a = 0.3694

b = 0.00002961

R = 8.314



if E==1 :

    a = 0.3694

    b = 0.00002961

    R = 8.314

    v = float(input("Enter the value of Volume :"))

    t = float(input("Enter the value of Temperature :"))

    P = ((R*t)/(v-b))-(a/(v*(v+b)))

    print("The Value of Pressure is:",P,"Pa") 

elif E==2:

    P = float(input("Enter the value of Pressure:"))

    t = float(input("Enter the value of Temperature:"))

    a2 = -R*t

    a3 = a-P*b*b-R*t*b

    a4 = -a*b

    coeff = [P,a2,a3,a4]

    roots = np.roots(coeff)

    if roots[0]>0:

        print("The value of Volume is:",roots[0],"m^3")

    elif roots[1]>0:

        print("The value of Volume is:",roots[1],"m^3")

    elif roots[2]>0:

        print("The value of Volume is:",roots[2],"m^3")

    else:

        print("Please enter the appropriate values")

else:

    print("Please enter the integer 1 or 2 ")
