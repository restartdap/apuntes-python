# Condicional con operador logico
print("Aplicacion Saludar")

def fSaludar(nombre):
    if nombre == "Rafael" or nombre == "rafael":
        print("Hola Rafael, te llamas como el desarrollador de esta aplicacion :D")
    else:
        print("Hola ", nombre)

nombre = str(input("Digite su nombre: "))
fSaludar(nombre)

print("---------------")

# Condicionales multiples
print("Aplicacion Mayor de Edad")

edad = int(input("Digite su edad: "))

if edad >= 0 and edad < 18:
    print("Es menor de edad")
elif edad >= 18 and edad < 150:
    print("Es mayor de edad")
else:
    print("Su edad no es correcta")

print("---------------")

# Concatenacion de operadores de comparacion
print("Aplicacion Salarios de empleados")

salEmpleado = float(input("Digite el salario del empleado: "))
salGerente = float(input("Digite el salario del gerente: "))
salPresidente = float(input("Digite el salario del presidente: "))

if salEmpleado < salGerente < salPresidente:
    print("Wea Correcta")
else:
    print("Wea Incorrecta")

print("---------------")