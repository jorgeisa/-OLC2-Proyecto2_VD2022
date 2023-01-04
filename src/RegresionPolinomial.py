import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score

from matplotlib import pyplot as plot

def polinomial_func(x_name, y_name, titulo, datos, degree, prediccionX):
    # step 1
    x = datos[x_name].values.reshape(-1,1)
    y = datos[y_name].values.reshape(-1,1)
    plot.scatter(x,y)

    
    # step 2
    poly = PolynomialFeatures(degree = int(degree))
    x_poly = poly.fit_transform(x)
    # step 3
    model = LinearRegression().fit(x_poly, y)
    # step 4
    y_pred = model.predict(x_poly)
    rmse = np.sqrt(mean_squared_error(y,y_pred))
    r2 = r2_score(y,y_pred)
    
    # step 5
    x_new_min = 0.0
    x_new_max = 30.0

    X_NEW = np.linspace(x_new_min, x_new_max, 50)
    X_NEW = X_NEW[:, np.newaxis]

    X_NEW_TRANSF = poly.fit_transform(X_NEW)
    y_pred = model.predict(X_NEW_TRANSF)

    plot.plot(X_NEW, y_pred, color='coral', linewidth=3)
    plot.grid()
    # plot.xlim(x_new_min, x_new_max)
    # plot.ylim(0,1000)


    

    

    prediccionFinal = "-"
    # Realizando la produccion en X
    if prediccionX != "":
        prediccion = model.predict(poly.fit_transform([[float(prediccionX)]]))
        prediccionFinal = str(prediccion[0])

    plot.xlabel(str(x_name), fontsize=13)
    plot.ylabel(str(y_name), fontsize=13)
    plot.title(titulo + "\n" + "[RMSE: " + str(rmse) + "], [R2: " + str(r2) + "]")
    plot.savefig("./static/images/linealPolinomial.png") 
    plot.clf()
    plot.cla()
    return {'RMSE': str(rmse), 'R2': str(r2), 'Prediccion': prediccionFinal}