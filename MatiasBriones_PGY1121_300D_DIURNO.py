import random
valor = random.randint(1500, 3500)
vehiculos = []
emision_contaminantes = 1500
anotaciones_vigentes = 2000
multas = 3000
opcion = 0 
opc = 0
nombre =input("Ingrese su nombre: ")
while opc != 4:
    menu = {"1)":"Grabar","2)":"Buscar","3)":"Imprimir certificados","4)":"Salir"}
    for x ,y in menu.items():
        print(x,y)
    print("Ingrese una opcion")
    opc = int(input(">> "))

    if opc == 1:
        while True:
            tipo = input("Ingrese Tipo de vehiculo (o ingrese x para salir)>> ")
            if tipo.lower() == 'x':
                break
            patente = input("Ingrese Patente de vehiculo >> ")
            marca = str(input("Ingrese marca del vehiculo >> "))
            if len(marca) < 2 and len(marca) > 15:
                print("Marca no valida intente nuevamente")
                break
            precio = int(input("Ingrese el precio del vehiculo >> "))
            if precio < 5000000:
                print("Precio no valido intente nuevamente")
                break
            multas_monto = input("Ingrese el monto de la multa >> ")
            multas_fecha = input("Ingrese la fecha de la multa (en formato dia/mes/año) >> ")
            fecha_reg = input("Ingrese la fecha del registro (en formato dia/mes/año) >> ")
            nombre_dueño = input("Ingrese el nombre del dueño del vehiculo >> ")
            vehiculo = {'TIPO': tipo,'PATENTE':patente,'MARCA':marca,'PRECIO':precio,'MULTAS MONTO':multas_monto,'MULTAS FECHA':multas_fecha,'FECHA REGISTRO':fecha_reg,'NOMBRE DUEÑO':nombre_dueño}
            vehiculos.append(vehiculo)


    elif opc == 2:
        patente_buscar = input("Ingrese la patente del vehiculo: ")
        encontrado = False

        for vehiculo in vehiculos:
            if vehiculo['PATENTE'] == patente_buscar:
                encontrado = True
                print("TIPO: ", vehiculo['TIPO'])
                print("PATENTE: ", vehiculo['PATENTE'])
                print("MARCA: ", vehiculo['MARCA'])
                print("PRECIO: ", vehiculo['PRECIO'])
                print("MONTO MULTAS: ", vehiculo['MULTAS MONTO'])
                print("FECHA MULTAS: ", vehiculo['MULTAS FECHA'])
                print("FECHA REGISTRO: ", vehiculo['FECHA REGISTRO'])
                print("NOMBRE DEL DUEÑO: ", vehiculo['NOMBRE DUEÑO'])
                break

        if not encontrado:
            print("No se encontraron ningun vehiculo con patente", patente_buscar)

    

    elif opc == 3:
        while opcion != 4:
            print("--------IMPRIMIR CERTIFICADOS--------")
            print("1) Certificado de emision contaminantes")
            print("2) Certificado de anotaciones vigentes")
            print("3) Certificado de multas")
            print("4) Salir")
            print("-------------------------------------")

            print("Ingrese una opcion")
            opcion = int(input(">> "))
            if opcion == 1:
                patente_buscar = input("Ingrese la patente del vehiculo para imprimir el certificado: ")
                encontrado = False
                for vehiculo in vehiculos:
                    if vehiculo['PATENTE'] == patente_buscar:
                        encontrado = True
                        print("----CERTIFICADO EMISION CONTAMINANTES----")
                        print("PATENTE: ", vehiculo['PATENTE'])
                        print("DUEÑO ACTUAL: ",vehiculo['NOMBRE DUEÑO'])
                        print("Precio certificado: ", valor)
                        print("-----------------------------------------")
                if not encontrado:
                    print("No se encontraron ningun vehiculo con patente", patente_buscar)
            elif opcion == 2:
                patente_buscar = input("Ingrese la patente del vehiculo para imprimir el certificado: ")
                encontrado = False
                for vehiculo in vehiculos:
                    if vehiculo['PATENTE'] == patente_buscar:
                        encontrado = True
                        print("----CERTIFICADO DE ANOTACIONES VIGENTES----")
                        print("PATENTE: ", vehiculo['PATENTE'])
                        print("DUEÑO ACTUAL: ",vehiculo['NOMBRE DUEÑO'])
                        print("Precio certificado: ", valor)
                        print("-------------------------------------------")
                if not encontrado:
                    print("No se encontraron ningun vehiculo con patente", patente_buscar)
            elif opcion == 3:
                patente_buscar = input("Ingrese la patente del vehiculo para imprimir el certificado: ")
                encontrado = False
                for vehiculo in vehiculos:
                    if vehiculo['PATENTE'] == patente_buscar:
                        encontrado = True
                        print("----CERTIFICADO DE MULTAS----")
                        print("PATENTE: ", vehiculo['PATENTE'])
                        print("DUEÑO ACTUAL: ",vehiculo['NOMBRE DUEÑO'])
                        print("Precio certificado: ", valor)
                        print("-----------------------------")
                if not encontrado:
                    print("No se encontraron ningun vehiculo con patente", patente_buscar)
            elif opcion == 4:
                break
            else:
                print("ingrese una opcion valida")
    elif opc == 4:
        print("Adios", nombre, ",muchas gracias")
    
    else:
        print("Opcion no valida")

