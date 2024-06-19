import os.path
import json
import datetime

Venta = []
Archivo = 'Ordenes.json'

Pizzas = {
  "peperoni": {"pequeña": 5000, "mediana": 8000, "familiar": 10000},
  "mediterranea": {"pequeña": 6000, "mediana": 9000, "familiar": 12000},
  "vegetariana": {"pequeña": 5500, "mediana": 8500, "familiar": 12000},
}

def Orden():
  NombreCliente = input("Por favor ingrese su Nombre: ").lower()
  JornadaCliente = input("Por favor ingrese su jornada\nDiurno\nVespertino\nAdministrativo\n").lower()
  PizzaCliente = input("Por favor ingrese la Pizza que desea\nPeperoni\nMediterranea\nVegetariana: ").lower()
  TamañoPizza = input(f"Por favor ingrese el tamaño de la pizza de {PizzaCliente} tenemos \npequeña\nmediana\nfamiliar:\n").lower()

  if PizzaCliente in Pizzas and TamañoPizza in Pizzas[PizzaCliente]:
    precio = Pizzas[PizzaCliente][TamañoPizza]
    
    if JornadaCliente == "diurno":
      print(f"Por ser de la modalidad {JornadaCliente} posee un descuento del 15%")
      descuento = precio * 0.15
      precioPagar = precio - descuento
    elif JornadaCliente == "vespertino":
      print(f"Por ser de la modalidad {JornadaCliente} posee un descuento del 10%")
      descuento = precio * 0.10
      precioPagar = precio - descuento
    elif JornadaCliente == "administrativo":
      print(f"Por ser de la modalidad {JornadaCliente} posee un descuento del 0%")
      precioPagar = precio

    DatosVenta = {
      "Nombre Cliente": NombreCliente,
      "Pizza Ordenada": PizzaCliente,
      "Tamaño Pizza": TamañoPizza,
      "Jornada Cliente": JornadaCliente,
      "Costo a Pagar": precioPagar,
      "Fecha": datetime.datetime.now().isoformat() # Añadiendo la fecha de la venta
    }

    Venta.append(DatosVenta)
  else:
    print("Tu Pizza o tamaño no está en el menú")

def buscar_ventas_cliente(NombreClienteBuscar):
  ventas_cliente = [venta for venta in Venta if venta["Nombre Cliente"] == NombreClienteBuscar.lower()]
  
  if ventas_cliente:
    print(f"Las ventas del cliente {NombreClienteBuscar} son las siguientes:\n")
    for venta in ventas_cliente:
      print(f"Pizza Ordenada: {venta['Pizza Ordenada']}, Tamaño: {venta['Tamaño Pizza']}, Jornada: {venta['Jornada Cliente']}, Costo: {venta['Costo a Pagar']}")
  else:
    print("No se encontró el cliente.")

def guardar_ventas():
  with open(Archivo, 'w') as archivo:
    json.dump(Venta, archivo)
  print("Se guardo Correctamente.")

def Descargar_Ventas():
  with open(Archivo, 'r') as archivo:
    print


def cargar_ventas():
  global Venta
  if os.path.exists(Archivo):
    with open(Archivo, 'r') as archivo:
      Venta = json.load(archivo)
    print(f"Las ventas han sido cargadas desde {Archivo}.")
  else:
    print(f"No se encontró el archivo {Archivo}.")
    
    
    
    
def generar_boleta():
  if not Venta:
    print("No hay ventas para generar boleta.")
    return
  
  NombreClienteBuscar = input("Ingrese el nombre del cliente para generar la boleta: ").lower()
  ventas_cliente = [venta for venta in Venta if venta["Nombre Cliente"] == NombreClienteBuscar]
  
  if ventas_cliente:
    print(f"Generando boleta para {NombreClienteBuscar}:\n")
    for venta in ventas_cliente:
      print(f"Pizza Ordenada: {venta['Pizza Ordenada']}, Tamaño: {venta['Tamaño Pizza']}, Jornada: {venta['Jornada Cliente']}, Costo: {venta['Costo a Pagar']}, Fecha: {venta['Fecha']}")
    total = sum(venta['Costo a Pagar'] for venta in ventas_cliente)
    print(f"\nTotal a pagar: {total} pesos.")
  else:
    print("No se encontraron ventas para el cliente.")









while True:
  try:
    print("-------------------------------------------------")
    print("Bienvenidos a la Pizzas Duoc.\n")
    print("1. Registrar una venta.")
    print("2. Mostrar todas las ventas.")
    print("3. Buscar ventas por cliente.")
    print("4. Guardar las ventas en un archivo.")
    print("5. Cargar las ventas desde un archivo.")
    print("6. Generar Boleta")
    print("7. Salir del programa.")
    print("-------------------------------------------------\n")
    opcion = int(input("¿Donde quiere ir? "))

    if opcion == 1:
      Orden()
    elif opcion == 2:
      if Venta:
        for venta in Venta:
          print(venta)
      else:
        print("No hay ventas registradas.")
    elif opcion == 3:
      NombreClienteBuscar = input("Ingrese el nombre del cliente que quiere buscar las ventas: ").lower()
      buscar_ventas_cliente(NombreClienteBuscar)
    elif opcion == 4:
      guardar_ventas()
    elif opcion == 5:
      cargar_ventas()
    elif opcion == 6:
      generar_boleta()
    elif opcion == 7:
      print("Saliendo del programa.")
      break
    else:
      print("Opción no válida, por favor intente de nuevo.")
  except Exception:
    print(f"Error")

