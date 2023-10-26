na = input ("nombre del alumno:")
nombre = na.lower ()
s = input ("Hombre o mujer:")
sexo = s.lower ()
if (nombre <= "m" and sexo == "mujer") or (nombre >= "n" and sexo == "hombre"):
    print ("¡Gryffindor!")
else:
    print ("¡Slytheryn!")