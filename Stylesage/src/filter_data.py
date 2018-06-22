# En este archivo de python filtro los row datos

from src.load_save_files import *
from src.categorical_to_numerical import *
from src.merge_datasets import *

if __name__ == '__main__':
    # primero obtenemos los row data
    train_data, test_data, users_data, products_data = read_data()

    # Pasamos las variables no númericas que nos interesen a variables numericas
    products_data['brand_name'] = dummies_labelEncoder(products_data.brand_name)
    users_data['country'] = dummies_labelEncoder(users_data.country)

    # Convertimos las fechas de tiempo
    users_data['date_joined'] = time_to_ordinal(users_data['date_joined'])
    train_data['date_tag'] = time_to_ordinal(train_data['date_tag'])
    test_data['date_tag'] = time_to_ordinal(test_data['date_tag'])

    # Ahora vamos a añadir las variables de #brand_name, country, date_joined a los archivos de train y test
    add_datasets(train_data, users_data, products_data)
    add_datasets(test_data, users_data, products_data)

