# En este archivo de python filtro los row datos

from src.load_save_files import *
from src.categorical_to_numerical import *
from src.merge_datasets import *
from matplotlib import pyplot as plt
from src.prueba import *

if __name__ == '__main__':
    # primero obtenemos los row data
    # train_data, test_data, users_data, products_data = read_data()

    # Pasamos las variables no númericas que nos interesen a variables numericas
    # products_data['brand_name'] = dummies_labelEncoder(products_data.brand_name)
    # users_data['country'] = dummies_labelEncoder(users_data.country)

    # Convertimos las fechas de tiempo
    # users_data['date_joined'] = time_to_ordinal(users_data['date_joined'])
    # train_data['date_tag'] = time_to_ordinal(train_data['date_tag'])
    # test_data['date_tag'] = time_to_ordinal(test_data['date_tag'])

    # Este proceso es lento
    # Ahora vamos a añadir las variables de #brand_name, country, date_joined a los archivos de train y test
    # add_datasets(train_data, users_data, products_data)
    # add_datasets(test_data, users_data, products_data)

    train, test = read_modified_db()

    # correlacion entre variables
    plt.matshow(train[['tag_id',  'post_id',  'product_id',  'user_id',  'date_tag',  'color', 'click_count', 'product_brand',  'country',  'date_joined' ]].corr())
    plt.legend()
    plt.xticks(arange(10), ('tag_id',  'post_id',  'product_id',  'user_id',  'date_tag',  'color', 'click_count', 'product_brand',  'country',  'date_joined'))
    plt.yticks(arange(10), ('tag_id',  'post_id',  'product_id',  'user_id',  'date_tag',  'color', 'click_count', 'product_brand',  'country',  'date_joined'))
    plt.show()

    """ CORRELACION:
        fecha que se unio el usuario con el id del usuario
        El id_tag con la fecha del post
        El id_tag con el id_post
        """

    # Mostramos en funcion de los likes: la marca, el pais, el color y el date id
    plt.figure()
    group_brand = agrupamos(train,'product_brand')
    group_country = agrupamos(train,'country')
    group_color = agrupamos(train, 'color')
    group_date = agrupamos(train, 'date_tag')

    plt.subplot(221)
    plt.plot(group_brand)
    plt.xlabel('product brand')

    plt.subplot(222)
    group_country.plot(kind='bar')
    plt.xlabel('country')

    plt.subplot(223)
    group_color.plot(kind='bar')
    plt.xlabel('color')

    plt.subplot(224)
    plt.plot(group_date)
    plt.xlabel('date tag')

    plt.show()
