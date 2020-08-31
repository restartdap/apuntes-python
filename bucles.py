# Uso de bucle For y operador In
print("Aplicacion Asignaturas")

asignaturas = ("español", "matematicas", "fisica", "quimica", "biologia")

print("Aplicacion de Asignaturas")

for asignatura in asignaturas:
    print(asignatura)

asignatura = str(input("Digite la asignatura deseada: ")).lower()

print(asignatura)

if asignatura in asignaturas:
    print("Se ha seleccionado correctamente:", asignatura)
else:
    print("No se encontro la siguiente asignatura:", asignatura)

# Imprime numeros en una sola linea
print("Aplicacion del conteo")
for numero in range(0, 10):
    print(numero, end="")

# Uso de break, continue y else
print("Aplicacion de operaciones en bucles")
for nombre in ["Pedro", "Rafael", "Juan", "Pepe"]:
    if nombre == "Rafael":
        print("Ey, compartimos nombre!")
        continue
    elif nombre != "Juan":
        print("Hola," + nombre)
    else:
        print("El nombre es juan")
        # break ya no tomará en cuenta a la sentencia else
        break

    print("Iteracion")
else:
    print("Hola Mundo")