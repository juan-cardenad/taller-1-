import random
#Variables
#inputs
nombre_producto1 = input("Ingrese el nombre del producto 1: ")
precio_producto1 = float(input("Ingrese el precio del producto 1: "))

#decisiones
if (precio_producto1 < 0):
    print("ERROR: El precio del producto no puede ser menor o igual a 0")
else:
    preguntarsitienedescuento_producto1 = input("el producto 1 tiene descuento?: ")
    if preguntarsitienedescuento_producto1.lower() == "si":
     porcenjedescuento_producto1 = float(input("Ingrese el porcentaje de descuento del producto 1 %: " ))
    cantidad_producto1 = input("Ingrese la cantidad del producto 1: ")
    cantidad_producto1 = int(cantidad_producto1)
    if(cantidad_producto1 < 0):
        print("ERROR: La cantidad del producto no puede ser menor o igual a 0")
    else:
        #operadores (en este caso multiplicacion)
        if preguntarsitienedescuento_producto1.lower() == "si":
            descuento_producto1 = precio_producto1 - (precio_producto1 * porcenjedescuento_producto1 /100 )
            total_producto1 = descuento_producto1 * cantidad_producto1
        else :
         total_producto1 = precio_producto1 * cantidad_producto1

        #Variables
        nombre_producto2 = input("Ingrese el nombre del producto 2: ")
        precio_producto2 = float(input("Ingrese el precio del producto 2: "))
        if (precio_producto2 < 0):
            print("ERROR: El precio del producto no puede ser menor o igual a 0")
        else:
            preguntarsitienedescuento_producto2 = input("el producto 2 tiene descuento?: ")
            if preguntarsitienedescuento_producto2.lower() == "si":
             porcenjedescuento_producto2 = float(input("Ingrese el porcentaje de descuento del producto 2 %: "))
            cantidad_producto2 = input("Ingrese la cantidad del producto 2: ")
            cantidad_producto2 = int(cantidad_producto2)
            if(cantidad_producto2 < 0):
                print("ERROR: La cantidad del producto no puede ser menor o igual a 0")
            else:
                #operadores (en este caso multiplicacion)
                if preguntarsitienedescuento_producto2.lower() == "si":
                    descuento_producto2 = precio_producto2 - (precio_producto2 * porcenjedescuento_producto2 / 100)
                    total_producto2 = descuento_producto2 * cantidad_producto2
                else:

                 total_producto2 = precio_producto2 * cantidad_producto2
                #Hay muchas formas de hacer las mismas operaciones
                #total_compra = (precio_producto1 * cantidad_producto1) + (precio_producto2 * cantidad_producto2)
                #total_compra = total_producto1 + (precio_producto2 * cantidad_producto2)
                total_compra = total_producto1 + total_producto2
                esvip = input("eres cliente vip ? :")
                if esvip.lower() == "si":
                    metodopago = input("ingrese el metodo de pago, cuotas o de contado : ")
                    if metodopago.lower() == "cuotas":
                     cuantas = int(input("a cuantas cuotas desea pagar ? : "))
                     pagoacuotas = total_compra / cuantas
                     if esvip.lower() == "si":
                         print(f"debera pagar {cuantas} cuotas de: {pagoacuotas}")
                #output
                #print(...): esto es una instruccion que le estamos indicando al programa

                if preguntarsitienedescuento_producto1.lower() == "si":
                     print("¡El producto 1 tiene descuento!")
                if preguntarsitienedescuento_producto2.lower() == "si":
                     print("¡El producto 2 tiene descuento!")


                print(f"El total de la compra es: {total_compra}")
                print("¡participa en un sorteo para ganarte el 90% de tu compra! ")
                rifa = int(input("Ingresa un numero entre 1 y 10 para participar : "))
                rifanumero = random.randint(1,10)
                premio = total_compra - (total_compra * 90 /100)
                ahorro = total_compra - premio
                if rifa == rifanumero :
                    print("felicidades has ganado el 90% de tu compra")
                    print(f"el total es : {total_compra}, te has ahorrado {ahorro} en tu compra ")
                    print(f"ahora deberas pagar : {premio} ")
                else :
                    print("no has acertado el numero :(")
                    print("feliz dia")







