# convert categorical data to numeric data

import pandas as pd
import datetime as dt
from sklearn import preprocessing


def dummiesLabelEncoder(to_convert):
    # to convert should de = Datos.categorical_columna
    # convert to numerical

    le = preprocessing.LabelEncoder()

    return le.fit_transform(to_convert)




def timeToOrdinal(to_convert):
    # to_convert = basededatos['columna_fecha']
    # EJM: data_df['Date'] = pd.to_datetime(data_df['Date'])
    #Convert dates to ordinal data

    to_convert = pd.to_datetime(to_convert)
    to_convert = to_convert.map(dt.datetime.toordinal)
    return to_convert
