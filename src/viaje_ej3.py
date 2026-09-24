edad = int(input("Cuantos años tienes:"))
nivel_fisico = int(input("¿Cual es tu nivel físico?:"))

while not(1<= nivel_fisico <=10):
    nivel_fisico = int(input("Entre 1 y 10:"))


if edad < 18:
    print("Debes ser mayor de edad")
elif nivel_fisico < 5:
    print("Debes estar en mejor forma.")
else:
    print("¡Listo para despegar!")