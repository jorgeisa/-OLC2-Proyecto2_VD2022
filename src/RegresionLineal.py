
import numpy as np
from sklearn.linear_model import LinearRegression

from sklearn.metrics import mean_squared_error, r2_score

from matplotlib import pyplot as plot

def lineal_func(x_name, y_name, titulo, datos, prediccionX):
    x = datos[x_name].values.reshape(-1,1)
    y = datos[y_name].values.reshape(-1,1)
    plot.scatter(x,y)
    model = LinearRegression()
    model.fit(x,y)
    y_pred =model.predict(x)

    rmse = np.sqrt(mean_squared_error(y, y_pred))
    r2 = r2_score(y,y_pred)
    

    prediccionFinal = "-"
    # Realizando la produccion en X
    if prediccionX != "":
        nuevo_x = np.array([float(prediccionX)])
        prediccion = model.predict(nuevo_x.reshape(-1,1))
        prediccionFinal = str(prediccion[0])

    plot.plot(x,y_pred, color='r', linewidth=3)
    plot.grid()
    plot.xlabel(str(x_name), fontsize=13)
    plot.ylabel(str(y_name), fontsize=13)
    plot.title(titulo + "\n" + "[RMSE: " + str(rmse) + "], [R2: " + str(r2) + "]")
    # Guardar imagen y limpiar
    plot.savefig("./static/images/linealPolinomial.png") 
    plot.clf()
    plot.cla()
    
    return {'RMSE': str(rmse), 'R2': str(r2), 'Prediccion': prediccionFinal}