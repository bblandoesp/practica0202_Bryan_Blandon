f = input ("Frase:")
l = input ("Letra:")
contador = 0
for i in range (len(f)):
    if f[i] == l:
        contador += 1
print ("la letra se repite", contador, "veces")