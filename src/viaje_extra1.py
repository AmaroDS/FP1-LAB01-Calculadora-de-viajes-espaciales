distancia = int(input("Dime la distancia:"))

if distancia < 150000:
    print("No hay paradas")
else:
    for i in range(150000, distancia+1, 150000):
        print(f"Parada en el {i} km")