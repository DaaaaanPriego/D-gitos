Digitos = []

for i in range (3):
    digito = input(f"Ingresa el dígito {i + 1}:" )
    Digitos.append(digito)
    
if len(Digitos) == 3:
    print("Los dígitos ingresados son:")
    for digito in Digitos:
        print(digito)
        
else:
    print("No se han ingresado suficientes dígitos")
    
