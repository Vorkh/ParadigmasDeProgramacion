Documentación del HoneyBee INC.

Como se utiliza el programa:
	Una vez entremos al sitio estaremos parados en la pantalla de inicio, desde ahí tendremos acceso a la barra de navegación, en la cual vamos a poder adentrarnos en las diferentes utilidades:
	1- En la barra de navegación encontramos “Lista Completa”, en la que podremos ver todas las compras realizadas y cada uno de los clientes.
	2- Luego tendremos la utilidad “Productos por Cliente” en la que podremos buscar el nombre de un cliente (Con solo ingresar 3 letras nos dará a elegir nombres que posean las mismas o podremos ingresar el nombre completo si a si se deseara), y esto nos permitirá ver todas las compras que realizo el cliente.
	3- Seguido podremos ver la solapa de “Clientes por Producto”, nos permite elegir determinado producto y nos dirá que clientes lo han comprado.
	4- Luego podremos ver “Productos más Vendidos”, mostrará un top de productos que sean los que tengan la mayor cantidad de compras.
	5- Y la última solapa nos muestra a los “Mejores Clientes”, brindándonos una informe de los productos que compro y la cantidad total gastada.

Archivo CSV:
	Para leer este archivo se creó una función, llamada “AskTable” que recorre el archivo, lo mete en una string y lo presenta en forma una matriz.

Funciones Utilizadas:
	--AskTable Esta función es la que utilizamos para leer el archivo.csv.

--dataPosition Al ingresar el título de x Columna devuelve el índice.

--searchData Busca un dato específico.

--tableFullData Se muestra por completo la tabla y todo su contenido.

--orderTable Ordena los datos ingresados en la tabla en base a producto y cantidad (de mayor a menor.

--mostSaleProducts Nos informa los productos más vendidos

orderTablePrice Ordena de mayor a menor los datos en la tabla con el nombre del Cliente a través del precio el Precio.

--bestClients Muestra los mejores clientes.

--validations Aquí se presentan todas las validaciones.