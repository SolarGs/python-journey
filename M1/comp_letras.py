primera = input("ingrese una palabra: ")
segunda = input("ingrese una 2da palabra: ")
lar_primera = len(primera)
lar_segunda = len(segunda)

print(primera,"tiene",lar_primera,"caracteres y",segunda,"tiene",lar_segunda,"caracteres")

if lar_primera - lar_segunda < 0:
    print("la palabra ",segunda,"es mas larga")
elif lar_primera - lar_segunda == 0:
    print("ambas palabras tienen la misma cantidad de caracteres")
else:
    print("la palabra",primera,"es mas larga")