print("Use:- \n 1 To calculate Temperature \n 2 To calculate Pressure \n 3 To calculate Volume \n 4 To calculate No. of moles")

print("Note :- Enter the Temperature in K, Pressure in Pa and Volume in m³")

a = int(input("Enter the Quantity need to Calculate:\t"))

R = 8.314

if a==1 :

    b = float(input("Enter value of Pressure:"))

    c = float(input("Enter value of Volume:"))

    n = float(input("Enter no. of moles:"))

    d = (b*c)/(R*n)

    print("The Value of Temperature is:",d,"K")

elif a==2 :

    b = float(input("Enter value of Volume:"))

    c = float(input("Enter value of Temperature:"))

    n = float(input("Enter no. of moles:"))

    d = n*R*c/b

    print("The value of pressure is:",d,"Pa")

elif a==3:

    b = float(input("Enter the value of Pressure:"))

    c = float(input("Enter value of Temperature:"))

    n = float(input("Enter no. of moles:"))

    d = n*R*c/b

    print("The value of Volume is:",d,"m³")

elif a==4 :

    b = float(input("Enter value of Pressure:"))

    c = float(input("Enter value of Temperature:"))

    n = float(input("Enter value of Volume:"))

    d = b*n/R*c

    print("The Number of Moles are:",d,"mols")

else:

    print("Please select the Numbers between 1 to 4")
