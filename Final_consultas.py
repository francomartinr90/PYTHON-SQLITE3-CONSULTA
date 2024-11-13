import sqlite3 #SE IMPORTA EL MODULO SQLITE3 PARA TRABAJAR CON BDD

print("\n/// LA BASE DE DATOS SE ESTA CARGANDO ///")

def conectar_db(): #FUNCION PARA CONECTAR A LA BASE DE DATOS CON EL NOMBRE PERSONAS_BDD.DB
    return sqlite3.connect('personas_bdd.db')

print("\n/// LA BASE DE DATOS SE CARGO CON EXITO. BIENVENIDO AL SISTEMA v0.1///")
input("Presione una tecla para continuar...")

def mostrar_menu(): #FUNCION PARA MOSTRAR UN MENU POR EL CUAL NAVEGAR 
    print("\n/// MENU DE DEMOSTRACION /// SELECCION UNA OPCION DEL MENU [1, 2, 3, 4, 5]")
    print("1. Ver todas las personas ordenadas por apellido")
    print("2. Buscar persona por DNI")
    print("3. Filtrar por lugar de residencia")
    print("4. Ver personas ordenadas por fecha de nacimiento")
    print("5. Salir")

def mostrar_persona(persona): #FUNCION QUE RECIBE LOS DATOS DE UNA PERSONA (COMPLETOS) PARA MOSTRARLOS EN UN FORMATO LEGIBLE
    print(f"\nDNI: {persona[0]}")
    print(f"Nombre completo: {persona[1]} {persona[2]}")
    print(f"Email: {persona[3]}")
    print(f"Fecha de nacimiento: {persona[4]}")
    print(f"Lugar de residencia: {persona[5]}")
    print("-" * 40)

def ver_todas(): #FUNCION PARA OBTENER TODOS  LOS DATOS DE LA BDD PARA LUEGO SER UTILIZADA POR LA FUNCION MOSTRAR_PERSONA
    with conectar_db() as conexion:
        cursor = conexion.cursor() #CREACION DE UN CURSOR
        cursor.execute("SELECT * FROM personas_bdd ORDER BY Apellido") #SELECCIONA *(TODAS) LAS PERSONAS Y LAS ORDENA POR APELLIDO
        personas = cursor.fetchall()
        
        print("\n=== LISTADO DE PERSONAS ===")
        for persona in personas:
            mostrar_persona(persona)

def buscar_por_dni(): #FUINCION PARA FILTRAR POR DNI
    dni = input("\nIngresá el DNI a buscar: ")
    with conectar_db() as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM personas_bdd WHERE DNI = ?", (dni,)) #SELECCIONA TODAS DONDE DNI SEA EL FILTRO 
        persona = cursor.fetchone()
        
        if persona:
            print("\n=== PERSONA ENCONTRADA ===")
            mostrar_persona(persona)
        else:
            print("\n¡No se encontró ninguna persona con ese DNI!")

def filtrar_por_ciudad(): #FUNCION PARA FILTRAR POR NOMBRE DE CIUDAD DE RESIDENCIA
    lugar = input("\nIngresá el lugar de residencia a buscar: ")
    with conectar_db() as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM personas_bdd WHERE Lugar_residencia LIKE ?", (f"%{lugar}%",)) #SELECIONA TODAS DESDE LA BDD DONDE LUGAR_RESIDENCIA SEA EL FILTRO CON LOS PARAMETROS LIKE PARA QUE NO HAGA DIFERENCIAS DE TIPEO
        personas = cursor.fetchall()
        
        if personas:
            print(f"\n=== PERSONAS EN {lugar.upper()} ===")
            for persona in personas:
                mostrar_persona(persona)
        else:
            print(f"\nNo se encontraron personas en {lugar}")

def ordenar_por_fecha(): #FUNCION PARA ORDENAR POR FECHA
    with conectar_db() as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM personas_bdd ORDER BY Fecha_nacimiento") #SELECCIONA TODAS DESDE BDD PARA ORDENARLAS POR FECHA DE NACMIENTO
        personas = cursor.fetchall()
        
        print("\n=== PERSONAS ORDENADAS POR FECHA DE NACIMIENTO ===")
        for persona in personas:
            mostrar_persona(persona)

def main(): #FUNCION QUE JUNTA TODAS LAS DEMAS PARA LUEGO NAVEGARLAS POR UN MENU
    while True:
        mostrar_menu()
        opcion = input("\nSELECCIONE UNA OPCION DEL MENU: ")
        
        if opcion == "1":
            ver_todas()
        elif opcion == "2":
            buscar_por_dni()
        elif opcion == "3":
            filtrar_por_ciudad()
        elif opcion == "4":
            ordenar_por_fecha()
        elif opcion == "5":
            print("\n/// GRACIAS POR UTILIZAR EL SISTEMA. HASTA LUEGO. ///")
            break
        else:
            print("\n/// OPCION NO VALIDA. SELECCIONE UNA OPCION DEL MENU ///")
        
        input("\nPresioná Enter para continuar...")

if __name__ == "__main__":
    main()