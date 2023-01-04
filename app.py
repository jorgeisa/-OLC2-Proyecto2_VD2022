from flask_wtf import FlaskForm
from flask_codemirror.fields import CodeMirrorField
from wtforms.fields import SubmitField
from flask_codemirror import CodeMirror

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

import pandas as pd

# Imports Regresion Lineal
from src.RegresionLineal import lineal_func
from src.RegresionPolinomial import polinomial_func


SECRET_KEY = 'secret!'
CODEMIRROR_THEME = 'liquibyte'
CODEMIRROR_ADDONS = (('display','autorefresh'),)
CODEMIRROR_LANGUAGES = ['javascript', 'python', 'sql']

app = Flask(__name__)
# Carpeta de subida
app.config['UPLOAD_FOLDER'] = './ArchivosSub'

app.config.from_object(__name__)
codemirror = CodeMirror(app)

# Variables Globales
analyzer = ""
data_error = []
table_simbol = ""
report_ast = ""


class CODEMIRROR_MY_FORM(FlaskForm):
    source_code = CodeMirrorField(
        language = 'python', 
        config = {
            'lineNumbers'    : 'true', 
            'identWhithTabs' : 'true',
            'electricChars'  : 'true',
            'autocorrect'    : 'true'
            })
    submit = SubmitField('Submit')

@app.route('/')
def Home():
    return render_template('Home.html')
    
@app.route('/analisis', methods = ['GET', 'POST'])
def index():
    source_form = CODEMIRROR_MY_FORM()
    out = ""
    text = source_form.source_code.data
    # variables globales
    global analyzer
    global data_error
    global table_simbol
    if text != None:
        try:
            analyzer = "Obtener el arbol"
            data_error = []
            out = "Salida"
            
        except Exception as e:
            out = f"WARNING!!! ({e})"
            data_error = None
    else:
        out = ""
    return render_template('index.html', source_form=source_form, out=out, data_error=data_error)

@app.route('/Reporte')
def Reporte():
    return render_template('Reporte.html')

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


if __name__ == "__main__":
    app.run(debug=True)
