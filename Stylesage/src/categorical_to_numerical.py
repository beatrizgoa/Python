# FUnciones para pasar de variables categoricas (segun el tipo de dato) a variables numéricas

import pandas as pd
import datetime as dt
from sklearn import preprocessing


def dummies_labelEncoder(columna):
    # columna tiene que tener el formato base_de_Datos.categorical_columna
    le = preprocessing.LabelEncoder()

    return le.fit_transform(columna)




def time_to_ordinal(to_convert):
    # el formato de to_convert tiene que ser: basededatos['columna_fecha']
    # EJM: data_df['Date'] = pd.to_datetime(data_df['Date'])

    to_convert = pd.to_datetime(to_convert)
    to_convert = to_convert.map(dt.datetime.toordinal)
    return to_convert
