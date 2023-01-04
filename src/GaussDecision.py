import matplotlib.pyplot as plt
# Import LabelEncoder
from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB


def gaussDecision_func(x_name1, x_name2, y_name, datos):
    x1 = datos[x_name1].values.reshape(-1,1)
    x2 = datos[x_name2].values.reshape(-1,1)
    y = datos[y_name].values.reshape(-1,1)
    x1_array = []
    x1_unicos = []
    x2_array = []
    x2_unicos = []
    y_array = []
    y_unicos = []
    for i in x1:
        x1_array.append(i[0])
        if i[0] not in x1_unicos:
            x1_unicos.append(i[0])

    for j in x2:
        x2_array.append(j[0])
        if j[0] not in x2_unicos:
            x2_unicos.append(j[0])

    for k in y:
        y_array.append(k[0])
        if k[0] not in y_unicos:
            y_unicos.append(k[0])

    # Converting string labels into numbers.
    le = preprocessing.LabelEncoder()
    x1_encoded = le.fit_transform(x1_array)
    x2_encoded = le.fit_transform(x2_array)
    y_encoded = le.fit_transform(y_array)

    y_encoded_unicos = []
    for i in y_encoded:
        if i not in y_encoded_unicos:
            y_encoded_unicos.append(i)
    
    x1_encoded_unicos = []
    for i in x1_encoded:
        if i not in x1_encoded_unicos:
            x1_encoded_unicos.append(i)

    x2_encoded_unicos = []
    for i in x2_encoded:
        if i not in x2_encoded_unicos:
            x2_encoded_unicos.append(i)


    informacionPx1 = "Columna x1: " + str(x1_unicos) + "\n" + "Columna x1 encoded: " + str(x1_encoded_unicos) + "\n\n"
    informacionPx2 = "Columna x2: " + str(x2_unicos) + "\n" + "Columna x2 encoded: " + str(x2_encoded_unicos) + "\n\n"
    informacionClasifica = "Columna y: " + str(y_unicos) + "\n" + "Columna y encoded: " + str(y_encoded_unicos) + "\n\n"

    informacionFinal = informacionPx1 + informacionPx2 + informacionClasifica

    # Combinig attributes into single listof tuples
    features=list(zip(x1_encoded, x2_encoded))

    model = GaussianNB()
    model.fit(features, y_encoded)

    # Predict Output
    predicted = model.predict([[0,27]]) 

    informacionGeneral = "\n" + informacionFinal + "\nValor a predecir: [0,27]\n" + "Prediccion: " + str(predicted)
    # plt.show()
    return {'prediccion': informacionGeneral}