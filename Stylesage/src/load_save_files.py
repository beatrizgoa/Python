# Cargamos datasets en csv format y guardamos data en archivos csv
import pandas as pd


def read_data():

    # Leemos los datos y mostramos la cabecera para examinarlos

    path = '../assets/'

    # train data
    train_data = pd.read_csv(path+"train.csv",delimiter=';', sep='delimiter')
    print('-----train data ----')
    print(train_data.head(), '\n')

    #test data
    test_data = pd.read_csv(path+"test.csv",delimiter=';', sep='delimiter')
    print('-----test data ----')
    print(test_data.head(), '\n')

    # users data
    users_data = pd.read_csv(path+"users.csv",delimiter=';', sep='delimiter')
    print('-----users data ----')
    print(users_data.head(), '\n')

    #product data
    products_data = pd.read_csv(path+"products.csv",delimiter=';', sep='delimiter')
    print('-----products data ----')
    print(products_data.head(), '\n')

    return train_data, test_data, users_data, products_data





def read_modified_db():

    # En esta funcion leemos los archivos de train y test modificados

    path = '../assets/'

    train_data = pd.read_csv(path+"trainining_modified_dummies.csv",delimiter=';', sep='delimiter')
    print('-----train data ----')
    print(train_data.head(), '\n')

    test_data = pd.read_csv(path+"testing_modified_dummies.csv",delimiter=';', sep='delimiter')
    print('-----test data ----')
    print(test_data.head(), '\n')

    # print(train_data[['product_brand','country', 'date_tag', 'date_joined']].describe())

    return train_data, test_data




def save_new_subset(subset,name):
    # a partir de subset (lo que queremos guardar) y del nombre que le queremos dar (name), creamos un csv nuevo que se guarda en assets
    subset.to_csv('../assets/' +name+ '.csv', sep=';')
    return 0
