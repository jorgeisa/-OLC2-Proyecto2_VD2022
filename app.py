from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

import pandas as pd

# Imports Regresion Lineal
from src.RegresionLineal import lineal_func
from src.RegresionPolinomial import polinomial_func
from src.ArbolDecision import arbolDecision_func
from src.GaussDecision import gaussDecision_func


app = Flask(__name__)
# Carpeta de subida
app.config['UPLOAD_FOLDER'] = './ArchivosSub'

app.config.from_object(__name__)

@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/RegresionLinealPoli')
def CargarArchivo():
    global linealHeader
    global linealTable
    global linealFilas
    global linealGrafica
    global linealPrediccion
    return render_template('RegresionLinealPoli.html', linealHeader=linealHeader, linealTable=linealTable, count=linealFilas, linealGrafica=linealGrafica, linealPrediccion=linealPrediccion)


dataLineal = "" # CSV Pandas
linealHeader = []
linealTable = []
linealFilas = 0
linealGrafica = ""
linealPrediccion = ""
@app.route("/archivoLinealPoli", methods=['POST'])
def uploadLineal():
    global dataLineal
    global linealHeader
    global linealTable
    global linealFilas
    global linealGrafica
    global linealPrediccion
    dataLineal = ""
    linealHeader = []
    linealTable = []
    linealFilas = 0
    linealGrafica = ""
    linealPrediccion = ""
    if request.method == 'POST':
        # obtenemos el archivo del input "archivo"
        f = request.files['archivo']
        filename = secure_filename(f.filename)

        # Guardamos el archivo en el directorio "Archivos PDF"
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # Guardamos el path
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        # Obtenemos la tabla usando pandas
        # Leer CSV
        dataLineal = pd.read_csv(str(path))

        # Obtener num. filas y columnas
        linealFilas = len(dataLineal.axes[0])
        num_columnas = len(dataLineal.axes[1])

        # Llenar array de header
        for header in dataLineal.columns.values:
            linealHeader.append(str(header))

        # Llenar array de tabla
        for i in range (linealFilas):
            filaArchivo = []
            for j in range(num_columnas):
                filaArchivo.append(str(dataLineal.iloc[i].values[j]))
            linealTable.append(filaArchivo) 

    return render_template('RegresionLinealPoli.html', linealHeader=linealHeader, linealTable=linealTable, count=linealFilas, linealGrafica=linealGrafica, linealPrediccion=linealPrediccion)

@app.route("/graficaLinealPoli", methods=['POST'])
def graficarLineal():
    global dataLineal
    global linealHeader
    global linealTable
    global linealFilas
    global linealGrafica
    global linealPrediccion
    linealGrafica = "./static/images/linealPolinomial.png"

    if request.method == 'POST':
        try:
            x_name = request.form['inputIndependiente']
            y_name = request.form['inputDependiente']
            opcion_algoritmo = request.form['inputRadio']
            prediccionPuntoX = request.form['inputPrediccion']
            if str(opcion_algoritmo) == "option1":
                # Lineal
                titulo = "Grafica Lineal"
                datos = lineal_func(str(x_name), str(y_name), titulo, dataLineal, str(prediccionPuntoX))
                print(datos)
                linealPrediccion = str(datos['Prediccion'])
            else:
                gradoPolinomial = request.form['inputGrado']
                # Polinomial
                titulo = "Grafica Polinomial"
                datos = polinomial_func(str(x_name), str(y_name), titulo, dataLineal, str(gradoPolinomial) , str(prediccionPuntoX))
                linealPrediccion = str(datos['Prediccion'])
                
        except:
            print("Error")
            linealGrafica = ""
            linealPrediccion = ""
    
    return render_template('RegresionLinealPoli.html', linealHeader=linealHeader, linealTable=linealTable, count=linealFilas, linealGrafica=linealGrafica, linealPrediccion=linealPrediccion)

dataArbol = "" # CSV Pandas
arbolHeader = []
arbolTable = []
arbolFilas = 0
arbolGrafica = ""
arbolPrediccion = "Informacion"

@app.route('/paginaArbol')
def paginaArbol():
    global arbolHeader
    global arbolTable
    global arbolFilas
    global arbolGrafica
    global arbolPrediccion
    return render_template('ArbolGaussClasificacion.html', arbolHeader=arbolHeader, arbolTable=arbolTable, count=arbolFilas, arbolGrafica=arbolGrafica, arbolPrediccion=arbolPrediccion)

@app.route("/archivoArbol", methods=['POST'])
def archivoArbol():
    global dataArbol
    global arbolHeader
    global arbolTable
    global arbolFilas
    global arbolGrafica
    global arbolPrediccion
    dataArbol = ""
    arbolHeader = []
    arbolTable = []
    arbolFilas = 0
    arbolGrafica = ""
    arbolPrediccion = "Informacion"
    if request.method == 'POST':
        # obtenemos el archivo del input "archivo"
        f = request.files['archivo']
        filename = secure_filename(f.filename)

        # Guardamos el archivo en el directorio "Archivos PDF"
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # Guardamos el path
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        # Obtenemos la tabla usando pandas
        # Leer CSV
        dataArbol = pd.read_csv(str(path))

        # Obtener num. filas y columnas
        arbolFilas = len(dataArbol.axes[0])
        num_columnas = len(dataArbol.axes[1])

        # Llenar array de header
        for header in dataArbol.columns.values:
            arbolHeader.append(str(header))

        # Llenar array de tabla
        for i in range (arbolFilas):
            filaArchivo = []
            for j in range(num_columnas):
                filaArchivo.append(str(dataArbol.iloc[i].values[j]))
            arbolTable.append(filaArchivo) 
    return render_template('ArbolGaussClasificacion.html', arbolHeader=arbolHeader, arbolTable=arbolTable, count=arbolFilas, arbolGrafica=arbolGrafica, arbolPrediccion=arbolPrediccion)

@app.route("/graficaArbol", methods=['POST'])
def graficaArbol():
    
    global dataArbol
    global arbolHeader
    global arbolTable
    global arbolFilas
    global arbolGrafica
    global arbolPrediccion
    arbolGrafica = "./static/images/arbol.png"

    if request.method == 'POST':
        try:
            x_name = request.form['inputOpciones']
            y_name = request.form['inputClasificaciones']
            
            # Lineal
            titulo = "Grafica Arbol"
            datos = arbolDecision_func(str(x_name), str(y_name), titulo, dataArbol)
            print(datos)
            # linealPrediccion = str(datos['Prediccion'])    
        except:
            print("Error")
            arbolGrafica = ""
            arbolPrediccion = "Informacion"
    return render_template('ArbolGaussClasificacion.html', arbolHeader=arbolHeader, arbolTable=arbolTable, count=arbolFilas, arbolGrafica=arbolGrafica, arbolPrediccion=arbolPrediccion)

@app.route("/graficaGauss", methods=['POST'])
def graficaGauss():
    
    global dataArbol
    global arbolHeader
    global arbolTable
    global arbolFilas
    global arbolGrafica
    global arbolPrediccion

    if request.method == 'POST':
        try:
            x_name1 = request.form['inputOpciones1']
            x_name2 = request.form['inputOpciones2']
            
            y_name = request.form['inputClasificaciones']
            
            # Gauss
            datos = gaussDecision_func(str(x_name1), str(x_name2), str(y_name), dataArbol)
            
            arbolPrediccion = str(datos['prediccion'])    
        except:
            print("Error")
            arbolGrafica = ""
            arbolPrediccion = "Informacion"
    return render_template('ArbolGaussClasificacion.html', arbolHeader=arbolHeader, arbolTable=arbolTable, count=arbolFilas, arbolGrafica=arbolGrafica, arbolPrediccion=arbolPrediccion)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
