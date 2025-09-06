# Trabajo de programación en Python - Examen Final
### Autor: Nicolás Solís
###  Asignatura: Programación en Python


Se necesita un algoritmo para demostrar el funcionamiento de una máquina de venta de productos, que debe cumplir con los siguientes requerimientos:

1) La máquina expendedora debe mostrar un menú con 15 productos. Los cuales se deben representar con la estructura: 

        Identificador – Nombre del producto – Precio – Cantidad disponible

2) El nombre del producto, la cantidad y el precio deben estar almacenados en sus respectivas variables.

3) Al iniciar el sistema, debe mostrar el catálogo con los 15 productos cargados previamente, luego solicitar al cliente que seleccione un producto y la cantidad que necesita comprar de ese producto en particular.

4) Se debe validar que el producto seleccionado se encuentre dentro de los productos existentes, si el producto no existe se debe informar al cliente e indicar que seleccione un producto existente.

5) Se debe validar que la cantidad ingresada se encuentre dentro de la cantidad disponible, de no ser así, se debe entregar un mensaje que indique esta condición y pedir nuevamente el ingreso de la cantidad.

6) Cuando se genera una compra, se debe descontar la cantidad comprada del catálogo de productos.

7) Cuando se realice la selección del producto y cantidad, se debe consultar al cliente si desea seguir comprando, es importante validar esta entrada para evitar ingresos erróneos.

8) Si el cliente decide seguir comprando se debe acumular el monto hasta que decida pagar por la compra.

9) Deben existir dos formas de pago: crédito y débito.

10) La opción de pago a crédito tiene un descuento al monto total del 3%.

11) Finalmente cuando el cliente decide pagar, debe mostrar el siguiente detalle:

        Nombre del cliente
        Producto – Cantidad – Valor del producto acumulado
        Cantidad de productos comprados
        Monto Final
        Monto final con descuento (si corresponde)


12) Al finalizar la compra y entregar el resumen, debe volver al catálogo con la cantidad de productos actualizado. 