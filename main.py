import random
import csv
from scipy.stats import gmean

#Lista de clientes (puede ser cualquier identificador de cliente, aquí uso números para simplicidad)
clientes = [f"Cliente {i}" for i in range(1, 11)]

#Función para generar saldos aleatorios
def generar_saldos_aleatorios(clientes):
    saldos = {}
    for cliente in clientes:
        saldo = round(random.uniform(1000, 5000))
        saldos[cliente] = saldo
    return saldos


#Función para clasificar saldos
def clasificar_saldos(saldos):
    #Se crea un diccionario para clasificar los saldos en tres categorías: baja, media y alta
    clasificacion = {'Categoría Baja': [], 'Categoría Media': [], 'Categoría Alta': []}
    #Se itera sobre cada cliente y su saldo en el diccionario de saldos
    for cliente, saldo in saldos.items():
        #Si el saldo es menor a 2000, se clasifica como 'Bajo' y se agrega al diccionario de clasificación
        if saldo < 2000:
            clasificacion['Categoría Baja'].append((cliente, saldo))
        #Si el saldo está entre 2000 y 4000 inclusive, se clasifica como 'Medio' y se agrega al diccionario de clasificación
        elif 2000 <= saldo <= 4000:
            clasificacion['Categoría Media'].append((cliente, saldo))
        #Si el saldo es mayor a 4000, se clasifica como 'Alto' y se agrega al diccionario de clasificación
        else:
            clasificacion['Categoría Alta'].append((cliente, saldo))
    return clasificacion


# Función para calcular estadísticas
def calcular_estadisticas(saldos):
    saldos_lista = list(saldos.values())
    saldo_mas_alto = max(saldos_lista)
    saldo_mas_bajo = min(saldos_lista)
    cliente_mas_alto = [cliente for cliente, saldo in saldos.items() if saldo == saldo_mas_alto][0]
    cliente_mas_bajo = [cliente for cliente, saldo in saldos.items() if saldo == saldo_mas_bajo][0]
    saldo_promedio = round(sum(saldos_lista) / len(saldos_lista), 2)
    media_geometrica = round(gmean(saldos_lista), 2)
    return saldo_mas_alto, cliente_mas_alto, saldo_mas_bajo, cliente_mas_bajo, saldo_promedio, media_geometrica


# Generar y asignar saldos
saldos = generar_saldos_aleatorios(clientes)

# Clasificar saldos
clasificacion = clasificar_saldos(saldos)

# Calcular estadísticas
saldo_mas_alto, cliente_mas_alto, saldo_mas_bajo, cliente_mas_bajo, saldo_promedio, media_geometrica = calcular_estadisticas(
    saldos)


def mostrar_saldos():
    print("\nSaldos de los clientes:")
    for cliente, saldo in saldos.items():
        print(f"{cliente}: ${saldo}")


def mostrar_clasificacion():
    print("\nClasificación de saldos:")
    for categoria, clientes_saldos in clasificacion.items():
        print(f"{categoria}:")
        for cliente, saldo in clientes_saldos:
            print(f"  {cliente}: ${saldo}")


def mostrar_estadisticas():
    print("\nEstadisticas de saldos:")
    print("------------------------------------")
    print(f"# Saldo más alto:    ${saldo_mas_alto:<15} (Cliente: {cliente_mas_alto}) #")
    print("------------------------------------")
    print(f"# Saldo más bajo:    ${saldo_mas_bajo:<15} (Cliente: {cliente_mas_bajo}) #")
    print("------------------------------------")
    print(f"# Saldo promedio:    ${saldo_promedio:<15} #")
    print("------------------------------------")
    print(f"# Media geométrica:  ${media_geometrica:<15} #")
    print("------------------------------------")


# Guardar resultados en un archivo CSV
def guardar_resultados_csv():
    with open('saldos_clientes.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Cliente", "Saldo"])
        for cliente, saldo in saldos.items():
            writer.writerow([cliente, saldo])

        writer.writerow([])
        writer.writerow(["Clasificacion", "Cliente", "Saldo"])
        for categoria, clientes_saldos in clasificacion.items():
            for cliente, saldo in clientes_saldos:
                writer.writerow([categoria, cliente, saldo])

        writer.writerow([])
        writer.writerow(["Estadistica", "Valor", "Cliente"])
        writer.writerow(["Saldo mas alto", saldo_mas_alto, cliente_mas_alto])
        writer.writerow(["Saldo mas bajo", saldo_mas_bajo, cliente_mas_bajo])
        writer.writerow(["Saldo promedio", saldo_promedio])
        writer.writerow(["Media geometrica", media_geometrica])


# Mensaje de bienvenida
print("********************************************************")
print("Bienvenido al programa de gestión de saldos de clientes.")

while True:
    print("\nMenú:")
    print("1. Mostrar saldos de clientes")
    print("2. Mostrar clasificación de saldos")
    print("3. Mostrar estadísticas de saldos")
    print("4. Guardar resultados en un archivo CSV")
    print("5. Salir del programa")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        mostrar_saldos()
    elif opcion == "2":
        mostrar_clasificacion()
    elif opcion == "3":
        mostrar_estadisticas()
    elif opcion == "4":
        guardar_resultados_csv()
        print("\nResultados guardados en 'saldos_clientes.csv'.")
    elif opcion == "5":
        print("\nGracias por usar el programa. ¡Adiós!")
        break
    else:
        print("\nOpción no válida. Por favor, seleccione una opción del 1 al 5.")
