# En este archivo de python filtro los row datos y se selecionan las features para la psoterios classificacion

from src.load_save_files import *
from src.categorical_to_numerical import *
from src.merge_datasets import *
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from src.analizing_data_functions import *
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor


def find_features(X, y, features):
    print('calculing features scores .... ')
    forest = RandomForestRegressor()
    forest.fit(X, y)
    print(sorted(list(zip(forest.feature_importances_, features))))
    return forest


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

    train_data, test_data = read_modified_db()

    # correlacion entre variables
    plt.matshow(train_data[['tag_id',  'post_id',  'product_id',  'user_id',  'date_tag',  'color', 'click_count', 'product_brand',  'country',  'date_joined' ]].corr())
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
    group_brand = agrupamos(train_data,'product_brand')
    group_country = agrupamos(train_data,'country')
    group_color = agrupamos(train_data, 'color')
    group_date = agrupamos(train_data, 'date_tag')

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

    # La cantidad de marcas en el entrenamiento
    print('La cantidad de marcas unicas es:', len(train_data['product_brand'].unique()))
    # La cantidad de id_tag unicos
    print('La cantidad de id post unicas es:',len(train_data['post_id'].unique()))

    sns.pairplot(pd.DataFrame(train_data), y_vars='click_count', x_vars=['product_brand', 'product_id', 'user_id', ])
    plt.show()
    # A partir de la grafica se podrian considerar como outliers los tag id cuyos num de clicks estan por encima de 5000

    # Random forest para ver las features mas importantes
    features = ['post_id',  'product_id',  'user_id',  'date_tag',  'color', 'product_brand'] # faltan tag_id, country, user_data joined
    # forest = find_features(train_data[features], train_data, features)

    # Como el id del tag se repite en la correlacion, se puede quitar, ademas que es un valor unico, es como enumerar el train
    # A partir de la correlacion y de random forest tambien podemos quitar user_data_joined
