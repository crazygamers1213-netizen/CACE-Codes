print("Select 1 for Deg. Celsius")
print("Select 2 for Kelvin")
print("Select 3 for Fahrenheit")
a = int(input("Enter the number of existing unit:"))
b = int(input("Enter the number of unit need to convert:"))
v = float(input("Enter the Value of Temperature:"))
if a==1 and b==2:
    k=v+273.15
    print("Temperature in Kelvin:",k)
elif a==1 and b==3:
    f=v*9/5+32
    print("Temperature in Fahrenheit :",f)
elif a==2 and b==1:
    c=v-273.15
    print("Temperature in Celsius:",c)
elif a==2 and b==3:
    f=(v-273.15)*9/5+32
    print("Temperature in Fahrenheit",f)
elif a==3 and b==1:
    c=(v-32)*5/9
    print("Temperature in Celsius:",c)
elif a==3 and b==2:
    k=(v-32)*5/9+273.15
    print("Temperature in Kelvin:",k)
else:
    print("Invalid input\nPlease Enter correct units")
