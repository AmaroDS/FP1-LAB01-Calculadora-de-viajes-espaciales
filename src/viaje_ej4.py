distancia_marte = 225000000

for i in range(10000,50001,10000):
    tiempo = (distancia_marte/i)/24
    print(f"Velocidad {i} km/h -> Tiempo: {tiempo} días")
