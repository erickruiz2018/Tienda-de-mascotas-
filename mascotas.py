def ingresar_mascota():
    raza = input("Ingrese la raza de la mascota: ")
    while True:
        try:
            precio = int(input("Ingrese el precio: "))
            break
        except ValueError:
            print("Error: el precio debe ser un número entero.")
    
    while True:
        tipo_pago = input("Ingrese el tipo de pago (contado o crédito): ")
        if tipo_pago.lower() == "contado" or tipo_pago.lower() == "crédito":
            break
        else:
            print("Error: el tipo de pago debe ser 'contado' o 'crédito'.")

    return raza, precio, tipo_pago.lower()

def mostrar_mascotas_vendidas(mascotas):
    print("Lista de mascotas vendidas:")
    for mascota in mascotas:
        raza, precio, tipo_pago = mascota
        print("Raza: {}, Precio: {}, Tipo de pago: {}".format(raza, precio, tipo_pago))

def guardar_mascotas_en_archivo(mascotas):
    try:
        with open("mascotas.txt", "w") as archivo:
            for mascota in mascotas:
                raza, precio, tipo_pago = mascota
                archivo.write("{},{},{}\n".format(raza, precio, tipo_pago))
        print("Datos de mascotas guardados correctamente.")
    except IOError:
        print("Error al guardar los datos de mascotas en el archivo.")

def cargar_mascotas_desde_archivo():
    mascotas = []
    try:
        with open("mascotas.txt", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                raza = datos[0]
                precio = int(datos[1])
                tipo_pago = datos[2]
                mascotas.append((raza, precio, tipo_pago))
    except IOError:
        print("Error al cargar los datos de mascotas desde el archivo.")
    
    return mascotas

def main():
    mascotas_vendidas = cargar_mascotas_desde_archivo()
    
    while True:
        print("\n------ Menú ------")
        print("1. Ingresar mascota")
        print("2. Mostrar lista de mascotas vendidas")
        print("3. Guardar datos de mascotas en archivo")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            mascota = ingresar_mascota()
            mascotas_vendidas.append(mascota)
            print("Mascota ingresada correctamente.")
        elif opcion == "2":
            mostrar_mascotas_vendidas(mascotas_vendidas)
        elif opcion == "3":
            guardar_mascotas_en_archivo(mascotas_vendidas)
        elif opcion == "4":
            print("¡Gracias por utilizar el programa!")
            break
        else:
            print("Error: opción inválida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()
