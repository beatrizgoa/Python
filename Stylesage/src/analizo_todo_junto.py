# En este fichero de python, analizo la correlacion y esas cosas cuando no queda variables categoricas en el train y esta unido con lo que interesa de users y producto

import pandas as pd
from src.prueba import buscamos_correlacion



def read_data(path = './', name='train.csv'):
    data = pd.read_csv(path + name, delimiter=';', sep='delimiter')

    return data



if __name__ == '__main__':
    train = read_data('../assets/', 'trainining_modified_dummies.csv')

    buscamos_correlacion(train)
