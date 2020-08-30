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