import matplotlib.pyplot as plt
import numpy as np
from sklearn.tree import DecisionTreeClassifier, plot_tree

# Import LabelEncoder
from sklearn import preprocessing


def arbolDecision_func(x_name, y_name, titulo, datos):
    x = datos[x_name].values.reshape(-1,1)
    y = datos[y_name].values.reshape(-1,1)
    x_array = []
    y_array = []

    # Convirtiendo a listas las columnas
    for i in x:
        x_array.append(i[0])

    for j in y:
        y_array.append(j[0])

    # Codificando los datos de las listas
    le = preprocessing.LabelEncoder()
    x_encoded = le.fit_transform(x_array)
    y_encoded = le.fit_transform(y_array)

    # Combinando atributos de listas
    features=list(zip(x_encoded))

    # fit the model
    clf = DecisionTreeClassifier().fit(features, y_encoded)
    plot_tree(clf, filled=True)
    plt.savefig("./static/images/arbol.png") 
    # plt.show()
    return {'informacion': "Informacion"}

