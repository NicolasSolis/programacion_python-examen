# Programa de máquina de venta de productos

from tabulate import tabulate #pip install tabulate
# https://pypi.org/project/tabulate/

productos = {
    1: {"nombre": "Agua Mineral", "precio": 800, "cantidad": 20},
    2: {"nombre": "Agua Saborizada", "precio": 1000, "cantidad": 12},
    3: {"nombre": "Bebida Cola", "precio": 1000, "cantidad": 15},
    4: {"nombre": "Bebida Naranja", "precio": 1200, "cantidad": 10},
    5: {"nombre": "Té Helado", "precio": 1300, "cantidad": 14},
    6: {"nombre": "Café Frío", "precio": 1500, "cantidad": 8},
    7: {"nombre": "Jugo de Naranja", "precio": 1300, "cantidad": 10},
    8: {"nombre": "Bebida Energética", "precio": 1500, "cantidad": 9},
    9: {"nombre": "Bebida Deportiva", "precio": 1400, "cantidad": 11},
    10: {"nombre": "Leche Chocolate", "precio": 1600, "cantidad": 7},
    11: {"nombre": "Papas Fritas", "precio": 700, "cantidad": 18},
    12: {"nombre": "Barra Chocolate", "precio": 1200, "cantidad": 16},
    13: {"nombre": "Galletas", "precio": 800, "cantidad": 20},
    14: {"nombre": "Frutos Secos", "precio": 1500, "cantidad": 6},
    15: {"nombre": "Yogurt", "precio": 1200, "cantidad": 10},
}


# Función que muestra los productos, usa tabulate para formato
def mostrar_productos():
    filas = [
        (pid, info["nombre"], info["precio"], info["cantidad"])
        for pid, info in productos.items()
    ]
    print(tabulate(filas, headers=["ID", "Nombre", "Precio (CLP)", "Cantidad Disponible"], tablefmt="pretty"))
    print("\n")


# Función para seleccionar un producto, cantidad y validar entradas
def seleccionar_productos():
    while True:
        try:
            id_producto = int(input("Por favor, ingrese ID del producto que desea comprar (ingrese 0 para finalizar): "))
            if id_producto == 0:
                return None
            if id_producto not in productos:
                print("Producto no existe. Por favor seleccione un producto existente.")
                continue
            
            cantidad = int(input(f"Por favor, ingrese la cantidad de {productos[id_producto]['nombre']} que desea comprar: "))
            if cantidad <= 0:
                print("La cantidad debe ser mayor a cero. Intente nuevamente.")
                continue
            if cantidad > productos[id_producto]['cantidad']:
                print(f"Cantidad no disponible. Solo quedan {productos[id_producto]['cantidad']} unidades.")
                continue
            
            return id_producto, cantidad

        except ValueError:
            print("Entrada inválida. Por favor ingrese números válidos.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")


# Función principal manejo de compra
def manejar_compra():
    nombre_cliente = input("Para comenzar, por favor ingrese su nombre: ")
    total_acumulado = 0
    carrito = {} # carrito por id producto, no lista, no duplicados (correccion bug v1)

    while True:
        mostrar_productos()
        seleccion = seleccionar_productos()
        if seleccion is None:
            break

        id_producto, cantidad = seleccion
        producto = productos[id_producto]
        subtotal = producto['precio'] * cantidad
        total_acumulado += subtotal

        # Acumular en carrito por ID (correccion bug v1: evita duplicados y mantiene cantidades)
        if id_producto in carrito:
            carrito[id_producto]['cantidad'] += cantidad
            carrito[id_producto]['subtotal'] += subtotal
        else:
            carrito[id_producto] = {
                "nombre": producto['nombre'],
                "cantidad": cantidad,
                "subtotal": subtotal
            }

        # Actualización de cantidad disponible al momento de la selección
        productos[id_producto]['cantidad'] -= cantidad

        seguir_comprando = input("¿Desea continuar comprando? (s/n): ").strip().lower()
        if seguir_comprando != 's':
            break

    if total_acumulado > 0:
        print("_" * 20)
        print("\nResumen de su compra:\n")
        print(f"Cliente: {nombre_cliente}")
        # carrito a lista para tabulate
        productos_comprados = [
            (info['nombre'], info['cantidad'], info['subtotal'])
            for info in carrito.values()
        ]
        print(tabulate(productos_comprados, headers=["Producto", "Cantidad", "Valor Acumulado"], tablefmt="pretty"))
        total_cantidad = sum(info['cantidad'] for info in carrito.values())
        print(f"Cantidad total de productos comprados: {total_cantidad}")
        print(f"Monto Final: {total_acumulado} CLP")
        
        # Selección de método pago
        metodo_pago = input("Seleccione método de pago (1: Débito, 2: Crédito): ").strip()
        if metodo_pago == '2':
            descuento = total_acumulado * 0.03 # 3% de descuento crédito
            monto_final_descuento = total_acumulado - descuento
            print(f"Monto final con descuento (3% por pago a crédito): {monto_final_descuento:.2f} CLP")
        else:
            print("No se aplican descuentos para pago con débito.")

    print("Gracias por su compra. Volviendo al catálogo...\n")

# Ejecución del programa, bucle principal
if __name__ == "__main__":
    while True:
        manejar_compra()
