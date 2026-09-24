pregunta = "s"
while  pregunta == "s":
    distancia_km = int(input("Dame la distancia:"))  # distancia Tierra - Luna
    velocidad_kmh = int(input("Dime la velocidad:"))
    tiempo_horas = distancia_km / velocidad_kmh
    tiempo_dias = tiempo_horas / 24
    print(f"Tardarías {tiempo_dias} días en llegar.")
    pregunta = input("¿Quieres hacer otra simulación? (s/n)")
