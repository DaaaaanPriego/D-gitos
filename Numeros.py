Nombres = []

for z in range (3):
    atributos = []
    Sujeto = input(f"Ingresa el nombre {z + 1}:" )
    atributos.append(Sujeto )
    
    apellidoP = input(f"Ingresa el apellido paterno {z + 1}")
    atributos.append(apellidoP )
    
    apellidoM = input(f"Ingresa el apellido materno {z + 1}")
    atributos.append(apellidoM )
    
    Edad = input(f"Ingresa la edad {z + 1}")
    atributos.append(Edad )
    
    Nombres.append(atributos)
    print(Nombres)
    
if len(Nombres) == 3:
    print("Los nombres ingresados son:")
    for y in range(len(Nombres)):
      for x in range(len(atributos)):
        print(f"Sujeto{Nombres[y] [x]}:")
        
else:
    print("No se han ingresado suficientes nombres")
    
