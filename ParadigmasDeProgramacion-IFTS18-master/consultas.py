import csv

#Funcion que devuelve en forma de lista el archivo csv. 
#Valida en caso de que no exista el archivo o le falten campos.
def AskTable():
    cantidaDeCampos = 5
    datosDeVentas = []

    try:
        with open("examen.csv") as archivo:
            archivo_csv = csv.reader(archivo)
            dato = next(archivo_csv, None)
            while dato:
                datosDeVentas.append(dato)
                dato = next(archivo_csv, None)
        for linea in datosDeVentas:
            if len(linea) != cantidaDeCampos:
                datosDeVentas = [["El archivo csv no contiene todos los campos."]]
                break
    except:
        datosDeVentas.append(["El archivo csv no existe."])
    return datosDeVentas

#Función que retorna el indice donde se encuentra el titulo (osea de la primera fila del archivo)
def dataPosition(titulo):
	dato = AskTable()
	posicion = dato[0].index(titulo)
	return posicion

#Retorna una lista de los datos mas cercanos al dato especificado por el usuario.
def tableFullData(searchData, datosDeVenta, posicionDelDato):
    listaDatos = []
    for linea in datosDeVenta[:1]:
        listaDatos.append(linea)
        
    for linea in datosDeVenta[1:]:
        if searchData in linea[posicionDelDato] and linea[posicionDelDato] not in listaDatos:
            listaDatos.append(linea)
    return listaDatos

#Función que retorna una lista de los mejores clientes.
def bestClients(datosDeVenta, posicionDeCliente, posicionDePrecio):
    listaClientes = []
    tabla = []
    
    for linea in datosDeVenta[1:]:
        if linea[posicionDeCliente] not in listaClientes:
            listaClientes.append(linea[posicionDeCliente])

    for cliente in listaClientes:
        precio = 0
        for linea in datosDeVenta[1:]:
            if linea[posicionDeCliente] == cliente:
                precio = precio + float(linea[posicionDePrecio])
            nuevaLista = [cliente, round(precio, 2)]
        tabla.append(nuevaLista)
    return tabla

#Función que retorna una lista de los productos mas vendidos
def mostSaleProducts(datosDeVenta, posicionDeProducto, posicionDeCantidad):
    listaProductos = []
    tabla = []

    for linea in datosDeVenta[1:]:
        if linea[posicionDeProducto] not in listaProductos:
            listaProductos.append(linea[posicionDeProducto])
    
    for producto in listaProductos:
        cantidad = 0
        for linea in datosDeVenta[1:]:
            if linea[posicionDeProducto] == producto:
                cantidad = cantidad + int(linea[posicionDeCantidad])
            nuevaLista = [producto, cantidad]
        tabla.append(nuevaLista)
    return tabla

#Función que ordena de mayor a menor la lista.
def orderTable(tabla, posicionDeColumna1, posicionDeColumna2):
    lista = []
    listaOrdenada = []
    tablaAMostrar = [[posicionDeColumna1, posicionDeColumna2]]
    posicion = tablaAMostrar[0].index(posicionDeColumna2)

    for linea in tabla:
        lista.append(linea[posicion])
    
    lista.sort()
 
    for i in reversed(lista):
        listaOrdenada.append(i)

    for i in listaOrdenada:
        for linea in tabla:
            for dato in linea:
                if dato == i:
                    tablaAMostrar.append(linea)
    return tablaAMostrar

#Validaciones para las columnas CODIGO, CANTIDAD y PRODUCTO
def validation(datoDeVenta):
    positionCode = datoDeVenta[0].index('CODIGO')
    positionCount = datoDeVenta[0].index('CANTIDAD')
    positionPrice = datoDeVenta[0].index('PRECIO')
    error = []
    cont = 0
    row = 1
    for line in datoDeVenta[1:]:
        cont = 0
        if len(line[positionCode]) != 6:
            error.append(['COLUMNA: Error fila {} no posee 6 caracteres'.format(row)])
        if line[positionCount].count('.') == 1:
            error.append(['CANTIDAD: Error fila {} posee un numero flotante'.format(row)])
        if line[positionPrice].count('.') == 0:
            error.append(['CANTIDAD: Error fila {} posee un numero entero'.format(row)])
        while cont < len(line[positionCode]):
            if cont < 3:
                if line[positionCode][cont].isdigit():
                    error.append(['CODIGO: Error fila {} posee en los primeros 3 caracteres.'.format(row)])
            elif cont >=3 and cont < 6:
                if line[positionCode][cont].isdigit() == False:
                    error.append(['CODIGO: Error fila {} posee letras en los ultimos 3 caracteres.'.format(row)])
            cont = cont + 1
        row = row + 1

    return error