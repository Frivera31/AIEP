ventas=[] #es para almacenar una lista (en este caso vacia)
 
 #usar un ciclo para ingresar las ventas de la semana 
for i in range(7): #el rango es de 0 a 6 (7 dias de la semana)
        venta= float(input(f"Ingrese las venta del dia {i+1}:")) #agregar el valor a la lista
        ventas.append(venta) #agregar el valor a la lista

    #procesar los datos 
total_ventas=sum(ventas) #sumar todas las ventas

print(total_ventas) #imprimir el total de ventas


