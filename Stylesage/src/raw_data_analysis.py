# En este archivo de python se va a analizar los datasets proporcionados

from src.load_save_files import *
from src.prueba import *

if __name__ == '__main__':

    # Cargamos los datasets y mostramos las cabeceras
    train_data, test_data, users_data, products_data = read_data()

    """ VARIABLES NUMERICAS Y CATEGORICAS
        En train y test tenemos todas las variables numericas menos la fecha
        En users tenemos data_joined y country como variables no numéricas
        En producto solo product_id es variable numérica
    """

    # Vamos a ver la cantidad de datos que tenemos en cada fichero
    data_shape(train_data, test_data, users_data, products_data)

    """ TAMANO DE NUESTROS FICHEROS 
        Train: 416147
        Test: 46239
        Usuario: 68819
        Producto: 309961
    """

    # Nuestros usuarios, productos y tag son unicos:
    duplicidades(train_data, 'tag_id')   # obtenemos: tag_id column of your data is not duplicated
    duplicidades(users_data, 'user_id') # obtenemos: user_id column of your data is not duplicated
    duplicidades(products_data, 'product_id') # product_id column of your data is not duplicated


    # Vamos a buscar valores nulos:
    check_nulls(train_data) # NO hay valores nulos
    check_nulls(test_data) # No hay valores nulos
    check_nulls(users_data) # No hay valores nulos
    check_nulls(products_data) # product_info: 443 valores nulos y description: 81381 valores nulos


    # Vamos a ver la descripcion de el numero de clicks en el entrenamiento
    data_description(train_data, 'click_count')

    # Vamos a ver la distribucion de los clicks counts
    count_click_intervals(train_data) # La mayoria de los post solo tienen 1 click, lugo le sigue los que tienen 0 clicks
    # Por ahora no podemos decir que hay outliers


    # Vamos a ver el rango de fechas de los productos, tags y usuarios
    analizamos_fechas(users_data, train_data)

    """
    USUARIOS: Fecha maxima:, 2016-01-21 Fecha minima: 2017-06-30 cantidad de fechas unicas 522
    TRAIN: Fecha maxima:, 2017-04-23 Fecha minima: 2017-06-19 cantidad de fechas unicas 58
    
    Los usuarios crecen con el tiempo. Es en las ultimas fechas cuando mas usuarios se regristran    
    """

    # cuantos usuarios unicos hay en el entrenamiento subset?
    print('La cantidad de usuarios unicos es:', len(train_data['user_id'].unique()))





