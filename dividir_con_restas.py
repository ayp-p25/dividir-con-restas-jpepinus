"""
Juan Pablo Castillo Haros 
"""

# Declaraciones
dividendo = float(input("Introduze el dividendo:")) 
divisor = float(input("Introduze el divisor:"))
contador = 0
residuo = dividendo  

#Entradas
if divisor == 0:
    print("Error: El divisor no puede ser cero.")
else:
    while True:
        if divisor <= dividendo:
            dividendo = dividendo - divisor  
            contador += 1
        else:
            residuo = dividendo  
            break

# Salidas
print("El cociente es:", contador ,"y el Residuo es:", residuo)
