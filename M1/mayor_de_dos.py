def mayor_de_dos(a,b):
    if a > b:
        return str(a) + " es mayor"
    elif a < b:
        return str(b) + " es mayor"
    else:
        return "ambos numeros son iguales"
    


print(mayor_de_dos(4,2))
print(mayor_de_dos(2,6))
print(mayor_de_dos(6,6))