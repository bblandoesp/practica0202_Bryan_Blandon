x = input ("Contraseña a guardar:")
y = input ("Contraseña:")
if y.upper () == x.upper ():
    print ("Contraseña correcta")
elif y.upper () != x.upper ():
    print ("contraseña incorrecta")