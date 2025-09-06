"""
Programa: Máquina de venta de productos (con interfaz por consola)

Descripción:
    Este archivo es un Script interactivo que muestra un catálogo de productos, 
    permite seleccionar productos y cantidades, mantiene un carrito por ID,
    actualiza stock en tiempo real y calcula el total. Usa 'tabulate' para
    mostrar tablas en consola.

Requisitos:
    Python 3.9+ (usa 'dict' con tipado genérico) y librería 'tabulate'.
    pip install tabulate

Uso:
    Ejecutar el módulo en la consola. Se ejecuta en bucle hasta que el usuario
    interrumpa por teclado (Ctrl+C). El flujo (1)solicita nombre del cliente, (2)permite
    seleccionar productos (ingresar 0 para finalizar), (3)muestra resumen y aplica
    descuento si se elige pagar con crédito.
"""

from typing import Optional, Tuple, Dict
from tabulate import tabulate  # pip install tabulate

# Catálogo inicial de productos
productos: Dict[int, Dict[str, int]] = {
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


def mostrar_productos() -> None:
    """
    Muestra en consola el catálogo de productos usando 'tabulate'.

    Formato mostrado: ID, Nombre, Precio (CLP), Cantidad Disponible.

    Efectos secundarios:
        - Imprime la tabla en stdout.
    """
    filas = [
        (pid, info["nombre"], info["precio"], info["cantidad"])
        for pid, info in productos.items()
    ]
    print(tabulate(filas, headers=["ID", "Nombre", "Precio (CLP)", "Cantidad Disponible"], tablefmt="pretty"))
    print("\n")


def seleccionar_productos() -> Optional[Tuple[int, int]]:
    """
    Interactúa con usuario para seleccionar el ID de producto y la cantidad.

    Validaciones:
        - ID = 0 finaliza selección (return None).
        - El ID debe existir en el diccionario productos (catálogo).
        - La cantidad debe ser un entero > 0 y <= stock disponible.

    Retorna:
        - (id_producto, cantidad) si usuario selecciona un producto válido.
        - None si el usuario ingresa 0 para finalizar.

    Manejo de errores:
        - Captura ValueError para entradas no numéricas y solicita reintento.
        - Captura genérica para errores inesperados y los muestra al usuario.
    """
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
            # Entrada que no puede convertirse a entero
            print("Entrada inválida. Por favor ingrese números válidos.")
        except Exception as e:
            # Captura cualquier excepción imprevista para evitar cierre abrupto
            print(f"Ocurrió un error inesperado: {e}")


def manejar_compra() -> None:
    """
    Flujo principal de compra para un cliente.

    Pasos:
        1. Solicita nombre del cliente.
        2. Muestra catálogo y permite seleccionar productos repetidamente.
        3. Mantiene un carrito indexado por ID para evitar duplicados.
        4. Actualiza el stock inmediatamente al agregar al carrito.
        5. Al finalizar, muestra resumen con cantidades y montos.
        6. Permite seleccionar método de pago y aplica descuento si corresponde.

    Efectos secundarios:
        - Modifica el diccionario global 'productos' (reduce cantidades disponibles).
        - Imprime interacciones y resumen en stdout.
    """
    nombre_cliente = input("Para comenzar, por favor ingrese su nombre: ")
    total_acumulado = 0
    # carrito por id producto: evita duplicados y mantiene cantidades y subtotal por ítem
    carrito: Dict[int, Dict[str, object]] = {}

    while True:
        mostrar_productos()
        seleccion = seleccionar_productos()
        if seleccion is None:
            # Usuario indicó que desea finalizar selección
            break

        id_producto, cantidad = seleccion
        producto = productos[id_producto]
        subtotal = producto['precio'] * cantidad
        total_acumulado += subtotal

        # Acumular en carrito por ID (evita duplicados)
        if id_producto in carrito:
            carrito[id_producto]['cantidad'] += cantidad
            carrito[id_producto]['subtotal'] += subtotal
        else:
            carrito[id_producto] = {
                "nombre": producto['nombre'],
                "cantidad": cantidad,
                "subtotal": subtotal
            }

        # Actualizar stock inmediatamente para reflejar disponibilidad real
        productos[id_producto]['cantidad'] -= cantidad

        seguir_comprando = input("¿Desea continuar comprando? (s/n): ").strip().lower()
        if seguir_comprando != 's':
            break

    if total_acumulado > 0:
        print("_" * 20)
        print("\nResumen de su compra:\n")
        print(f"Cliente: {nombre_cliente}")
        # Preparar lista para tabulate: Producto, Cantidad, Valor Acumulado (subtotal)
        productos_comprados = [
            (info['nombre'], info['cantidad'], info['subtotal'])
            for info in carrito.values()
        ]
        print(tabulate(productos_comprados, headers=["Producto", "Cantidad", "Valor Acumulado"], tablefmt="pretty"))
        total_cantidad = sum(info['cantidad'] for info in carrito.values())
        print(f"Cantidad total de productos comprados: {total_cantidad}")
        print(f"Monto Final: {total_acumulado} CLP")

        # Selección de método pago: se mantiene la convención original (1: Débito, 2: Crédito)
        metodo_pago = input("Seleccione método de pago (1: Débito, 2: Crédito): ").strip()
        if metodo_pago == '2':
            # Según el código original, el pago con crédito aplica un 3% de descuento
            descuento = total_acumulado * 0.03  # 3% de descuento crédito
            monto_final_descuento = total_acumulado - descuento
            print(f"Monto final con descuento (3% por pago a crédito): {monto_final_descuento:.2f} CLP")
        else:
            print("No se aplican descuentos para pago con débito.")

    print("Gracias por su compra. Volviendo al catálogo...\n")


# Ejecución del programa en bucle principal
if __name__ == "__main__":
    try:
        while True:
            manejar_compra()
    except KeyboardInterrupt:
        # Manejo amigable de Ctrl+C para salir del programa
        print("\nGracias por su visita.")
