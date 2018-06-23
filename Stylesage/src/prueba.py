from matplotlib import pyplot as plt
from src.categorical_to_numerical import *
from src.load_save_files import *
from src.merge_datasets import *
from numpy import arange
from src.find_outliers import *
import numpy as np

def check_nulls(data):
    # Con esta funcion chekeamos si es nulo algún valor

    # Vamos a ver los null que hay
    null = data.isnull().sum()
    aux = 0
    for i in null.values:
        if i != 0:
            aux = 1
            continue

    if aux == 0:
        print('No hay ningun nulo en el dataset')

    else:
        print('Tu base de datos tiene valores nulos:', '\n', null, '\n')

    return 0



def data_shape(train_data, test_data, users_data, products_data):

    # Para ver la cantidad de datos que hay

    # vamos con el tamaño de los datasets
    train_shape = train_data.shape
    test_shape = test_data.shape
    user_shape = users_data.shape
    products_shape = products_data.shape

    return 0


def data_description(database, column):
    # MOstramos la descripcion de la database con la/las columnas que se pasen

    # Vemos la descripcion
    description = database.describe()
    print('description of the ', column, '\n', description, '\n')

    return 0




def duplicidades(data, column):
    # vamos a ver las duplicidades para una columna especifica en la base de datos data
    duplicated = data[column].duplicated().sum()

    if duplicated == 0:
        print(column, 'column of your data is not duplicated')
    else:
        print(column, 'column of your data is duplicated')

    return 0



def analizamos_fechas(users_data, train_data):

    ## Vamos a ver las fechas de los test
    print('USUARIOS: Fecha maxima:,', users_data.date_joined.min(), 'Fecha minima:', users_data.date_joined.max(), 'cantidad de fechas unicas', len(users_data['date_joined'].unique()))
    print('TRAIN: Fecha maxima:,', train_data.date_tag.min(), 'Fecha minima:', train_data.date_tag.max(), 'cantidad de fechas unicas', len(train_data['date_tag'].unique()))

    # Vamos a mostrar: los usuarios por fecha
    # prirmero tenemos quee contar los usuarios en cada fecha
    plt.figure()
    plt.subplot(211)
    users_date_joined = users_data.groupby('date_joined').user_id.count().plot(kind='bar')
    plt.ylabel('number of users')
    plt.subplot(212)
    train_date_tag = train_data.groupby('date_tag').tag_id.count().plot(kind='bar')
    plt.ylabel('number of tags_id')
    plt.show()

    return 0



def agrupamos(database, param):
    # Funcion para agrupar en funcion de los clicks count
    # Se muestra en un diagrama de barras

    # plt.figure()
    agrupamos = database.groupby(param).click_count.count()# .plot(kind='bar')
    # plt.show()

    return agrupamos



def buscamos_correlacion(input_data):
    # Se busca correlacion en el dataset que se pase
    correlation = input_data.corr()
    print(correlation)

    return 0




def count_click_intervals(database):
    # EN esta funcion vamos a analizar la cantidad de click counts que hay

    lenght = database.shape[0]

    # Se calculan los clicks en funcion de los intervalos
    first = len(database[(database.click_count >=0) & (database.click_count < 10)])
    second = len(database[(database.click_count >=10) & (database.click_count < 20)])
    third = len(database[(database.click_count >=20) & (database.click_count < 50)])
    fouth = len(database[(database.click_count >=50) & (database.click_count < 1000)])
    fifth = len(database[(database.click_count >=1000)])

    # Se muestra al usuario
    print('first interval has:', first, first/lenght*100,'%')
    print('second interval has:', second, second/lenght*100,'%')
    print('third interval has:', third, third/lenght*100,'%')
    print('fouth interval has:', fouth, fouth/lenght*100,'%')
    print('fifth interval has:', fifth, fifth/lenght*100,'%')

    # Nos aseguramos que tienen el mismo numero de likes y no nos hemos dejado ninguno
    assert (first+second+third+fouth+fifth == lenght)

    x = [first, second, third, fouth, fifth]

    # Analizamos el primero y segundo intervalo mas en detalle
    intervalos_valores = []
    for i in range(0,22,2):
            intervalos_valores.append(len(database[(database.click_count >=i) & (database.click_count < (i+2))]))


    # Mostramos las distribuciones de muestras

    plt.figure(1)
    plt.plot(x)
    plt.xticks(arange(5), ('0-10', '10-20', '20-50', '50-100', '>1000'))
    plt.xlabel('click counts')


    plt.figure(2)
    plt.plot(arange(0, 22, step=2),intervalos_valores)
    plt.xticks(arange(22, step=2))
    plt.xlabel('click counts')

    plt.show()

    return 0



def unique_train_test_dates(train, test):
    # Vamos a ver si son las mismas fechas las de train que las de test, en la publicacion tag_id
    unique_date_train = train['date_tag'].unique()
    unique_date_test = test['date_tag'].unique()

    # Sabemos si tienen la misma longitud
    print('longitud', len(unique_date_train) == len(unique_date_test))

    print(unique_date_test,unique_date_train)





if __name__ == '__main__':
    train_data, test_data, users_data, products_data = read_data()

    data_description(train_data, 'click_count')

    # train_mod, test_mod = read_modified_db()

    # buscamos_correlacion(train_data, test_data, users_data, products_data)

    # Creamos los nuevos datasets mezclados
    # new_training = add_datasets(train_data,  users_data, products_data)
    # new_testing =  add_datasets(test_data, users_data, products_data)

    # Los guardamos en csv
    # new_testing.to_csv('./Exercise/testing_modified.csv', sep=';')
    # new_training.to_csv('./Exercise/training_modified.csv', sep=';')


    # Duplicidades:
    # duplicidades(train_data, 'tag_id')
    # duplicidades(users_data, 'user_id')
    # duplicidades(products_data, 'product_id')

    # agrupamos
    # agrupamos(train_mod, 'product_brand')

    # COntamos los intervalos de clicks que hay
    # count_click_intervals(train_data)

    # train_mod['product_brand'] = dummies_labelEncoder(train_mod.product_brand)
    # train_mod['country'] = dummies_labelEncoder(train_mod.country)

    # print(train_mod.head)

    # buscamos correlacion
    # print(train_mod[['product_brand','country', 'date_tag', 'date_joined']].describe())


    # Convertimos las variables categoricas:
    # products_data['brand_name'] = dummies_labelEncoder(products_data.brand_name)
    # users_data['country'] = dummies_labelEncoder(users_data.country)

    # COnvertimos las fechas de tiempo
    # users_data['date_joined'] = time_to_ordinal(users_data['date_joined'])

    # Vamos a probar a pasarle sklearn directamente a los dos de train y test, a ver si salen igual, sino, a mano
    # train_data['date_tag'] = time_to_ordinal(train_data['date_tag'])
    # test_data['date_tag'] = time_to_ordinal(test_data['date_tag'])

    # save_new_subset(products_data, 'products_data_dummies')
    # save_new_subset(users_data,'user_data_dummies')

    # save_new_subset(train_data, 'train_data_dummies')
    # save_new_subset(test_data, 'test_data_dummies')


    # Ahora metemos en el conjunto de train y test la marca de productos, el pais de usuario y su fecha de union
    # add_datasets(train_data, users_data, products_data)
    # add_datasets(test_data, users_data, products_data)

    # Guardamos los nuevos train, test en csv
    # save_new_subset(train_data,'trainining_modified_dummies')
    # save_new_subset(test_data,'testing_modified_dummies')

    # analizamos_fechas(users_data, train_data)

    check_nulls(products_data)

    print('hola')
