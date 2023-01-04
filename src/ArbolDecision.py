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
    for i in x:
        x_array.append(i[0])

    for j in y:
        y_array.append(j[0])

    # Converting string labels into numbers.
    le = preprocessing.LabelEncoder()
    x_encoded = le.fit_transform(x_array)
    y_encoded = le.fit_transform(y_array)

    print("x_encoded: ", x_encoded)
    print("y_encoded: ", y_encoded)

    # Combinig attributes into single listof tuples
    features=list(zip(x_encoded))

    # fit the model
    clf = DecisionTreeClassifier().fit(features, y_encoded)
    plot_tree(clf, filled=True)
    plt.savefig("./static/images/arbol.png") 
    # plt.show()
    print(titulo)
    return {'informacion': "Informacion"}
    

def arbolDecision_func2(x_name, y_name, datos):
    x = datos[x_name].values.reshape(-1,1)
    y = datos[y_name].values.reshape(-1,1)
    # Creating labelEncoder
    le = preprocessing.LabelEncoder()

    # Converting string labels into numbers.
    outlook_encoded=le.fit_transform(x)
    label=le.fit_transform(y)

    print ("outlook:  ",outlook_encoded)

    # Combinig attributes into single listof tuples
    features=list(zip(outlook_encoded))
    print (features)

    # fit the model
    clf = DecisionTreeClassifier().fit(features, label)
    plot_tree(clf, filled=True)
    plt.show()

