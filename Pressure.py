print("bar:1")
print("k pa:2")
print("pascal:3")
print("psi:4")
print("atm:5")
print("torr:6")

n1=int(input("enter the number of current unit: "))
n2=int(input("enter the number of the unit you want to convert to: "))
v1=float(input("enter the value:"))

if n1==1 and n2==2:
k=v1*100
print("pressure in kpa:",k)
elif n1==1 and n2==3:
k=v1*100000
print("pressure in pa:",k)
elif n1==1 and n2==4:
k=v1*14.5038
print("pressure in psi:",k)
elif n1==1 and n2==5:
k=v1*0.986923
print("pressure in atm:",k)
elif n1==1 and n2==6:
k=v1*750.062
print("pressure in torr:",k)

elif n1==2 and n2==1:
k=v1*0.01
print("pressure in bar:",k)
elif n1==2 and n2==3:
k=v1*1000
print("pressure in pa:",k)
elif n1==2 and n2==4:
k=v1*0.145038
print("pressure in psi:",k)
elif n1==2 and n2==5:
k=v1*0.00986923
print("pressure in atm:",k)
elif n1==2 and n2==6:
k=v1*7.50062
print("pressure in torr:",k)

elif n1==3 and n2==1:
k=v1*1e-5
print("pressure in bar:",k)
elif n1==3 and n2==2:
k=v1*0.001
print("pressure in kpa:",k)
elif n1==3 and n2==4:
k=v1*0.000145038
print("pressure in psi:",k)
elif n1==3 and n2==5:
k=v1*9.8692e-6
print("pressure in atm:",k)
elif n1==3 and n2==6:
k=v1*0.007500592001184

print("pressure in torr:",k)

elif n1==4 and n2==1:
k=v1*0.068947344713529895577
print("pressure in bar:",k)
elif n1==4 and n2==2:
k=v1*6.8947344713529892246
print("pressure in kpa:",k)
elif n1==4 and n2==3:
k=v1*6894.7344713529892033
print("pressure in pa:",k)
elif n1==4 and n2==5:
k=v1*0.06804573867607194293
print("pressure in atm:",k)
elif n1==4 and n2==6:
k=v1*51.714761401980837263
print("pressure in torr:",k)

elif n1==5 and n2==1:
k=v1*1.0132466461424456394
print("pressure in bar:",k)
elif n1==5 and n2==2:
k=v1*101.32466461424456838
print("pressure in kpa:",k)
elif n1==5 and n2==3:
k=v1*101324.66461424456793
print("pressure in pa:",k)
elif n1==5 and n2==5:
k=v1*14.695900132281069617
print("pressure in psi:",k)
elif n1==5 and n2==6:

k=v1*759.99748451996879339
print("pressure in torr:",k)

elif n1==6 and n2==1:
k=v1*0.0013332192710295341729
print("pressure in bar:",k)
elif n1==6 and n2==2:
k=v1*0.1333219271029534303
print("pressure in kpa:",k)
elif n1==6 and n2==3:
k=v1*133.32192710295342408
print("pressure in pa:",k)
elif n1==6 and n2==5:
k=v1*0.019336710697316409485
print("pressure in psi:",k)
elif n1==6 and n2==6:
k=v1*0.001315785118213209275
print("pressure in atm:",k)

else:
print("Invalid input, Please select correct units.")
