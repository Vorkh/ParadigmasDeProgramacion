#!/usr/bin/env python
import csv
import consultas
from datetime import datetime
from flask import Flask, render_template, redirect, url_for, flash, session
from flask_bootstrap import Bootstrap
# from flask_moment import Moment
from flask_script import Manager
from forms import ClienteForm, ProductoForm

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
# moment = Moment(app)

app.config['SECRET_KEY'] = 'un string que funcione como llave'

@app.route('/')
def index():
    return render_template('index.html', fecha_actual=datetime.utcnow())

@app.route('/productosmasvendidos')
def productosMasVendidos():
    datosDeVentas = consultas.AskTable()
    if len(datosDeVentas) == 1:
        return render_template('errores.html', lista=datosDeVentas)
    posicionDeProducto = consultas.dataPosition('PRODUCTO')
    posicionDeCantidad = consultas.dataPosition('CANTIDAD')
    posicionDePrecio = consultas.dataPosition('PRECIO')
    posicionDeCodigo = consultas.dataPosition('CODIGO')
    validaciones = consultas.validation(datosDeVentas)
    if len(validaciones):
        return render_template('errores.html', lista=validaciones)
    else:
        sumaDeProductos = consultas.mostSaleProducts(datosDeVentas, posicionDeProducto, posicionDeCantidad)
        tablaCompleta = consultas.orderTable(sumaDeProductos, 'PRODUCTO', 'CANTIDAD')
        return render_template('productos_mas_vendidos.html', tabla=tablaCompleta)

@app.route('/mejoresclientes')
def mejoresCliente():
    datosDeVentas = consultas.AskTable()
    if len(datosDeVentas) == 1:
        return render_template('errores.html', lista=datosDeVentas)
    posicionDeCliente = consultas.dataPosition('CLIENTE')
    posicionDePrecio = consultas.dataPosition('PRECIO')
    posicionDeCantidad = consultas.dataPosition('CANTIDAD')
    posicionDeCodigo = consultas.dataPosition('CODIGO')
    validaciones = consultas.validation(datosDeVentas)
    if len(validaciones):
        return render_template('errores.html', lista=validaciones)
    else:
        sumaDePrecios = consultas.bestClients(datosDeVentas, posicionDeCliente, posicionDePrecio)
        tablaCompleta = consultas.orderTable(sumaDePrecios, 'CLIENTE', 'PRECIO')
        return render_template('mejores-clientes.html', tabla=tablaCompleta)

@app.route('/clientesxproducto', methods=['GET', 'POST'])
def formBusquedaProducto():
    formulario = ProductoForm()
    datosDeVentas = consultas.AskTable()
    if len(datosDeVentas) == 1:
        return render_template('errores.html', lista=datosDeVentas)
    posicionDeCliente = consultas.dataPosition('CLIENTE')
    posicionDePrecio = consultas.dataPosition('PRECIO')
    posicionDeCantidad = consultas.dataPosition('CANTIDAD')
    posicionDeCodigo = consultas.dataPosition('CODIGO')
    validaciones = consultas.validation(datosDeVentas)
    if len(validaciones):
        return render_template('errores.html', lista=validaciones)
    if formulario.validate_on_submit():
        datoIngresado = formulario.producto.data
        producto = datoIngresado.upper()
        dataPosition = consultas.dataPosition('PRODUCTO')
        listaDeProductos = consultas.tableFullData(producto, datosDeVentas, dataPosition)
        return render_template('formulario_buscar_producto.html', form=formulario, buscarProducto=producto, lista=listaDeProductos)
        if len(listaDeProductos):
            listaDeProductos = None
        else:
            return redirect(url_for('tablaClientesPorProducto', producto=producto))
    return render_template('formulario_buscar_producto.html', form=formulario)

@app.route('/productosxcliente', methods=['GET', 'POST'])
def formBusquedaCliente():
    formulario = ClienteForm()
    datosDeVentas = consultas.AskTable()
    if len(datosDeVentas) == 1:
        return render_template('errores.html', lista=datosDeVentas)
    posicionDePrecio = consultas.dataPosition('PRECIO')
    posicionDeCodigo = consultas.dataPosition('CODIGO')
    posicionDeCantidad = consultas.dataPosition('CANTIDAD')
    posicionDeCliente = consultas.dataPosition('CLIENTE')
    validaciones = consultas.validation(datosDeVentas)
    if len(validaciones):
        return render_template('errores.html', lista=validaciones)
    if formulario.validate_on_submit():
        datoIngresado = formulario.cliente.data
        cliente = datoIngresado.upper()
        dataPosition = consultas.dataPosition('CLIENTE')
        listaDeClientes = consultas.tableFullData(cliente, datosDeVentas, dataPosition)  
        return render_template('formulario_buscar_cliente.html', form=formulario, buscarCliente=cliente, lista=listaDeClientes)
        if len(listaDeClientes) == 0:
            listaDeClientes = None
        else:
            return redirect(url_for('tablaProductoPorCliente', cliente=cliente))
    return render_template('formulario_buscar_cliente.html', form=formulario)

@app.errorhandler(404)
def no_encontrado(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def error_interno(e):
    return render_template('500.html'), 500

if __name__ == "__main__":
    # app.run(host='0.0.0.0', debug=True)
    manager.run()
