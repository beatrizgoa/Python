from src.categorical_to_numerical import *
from src.load_save_files import *
from src.merge_datasets import *
from src.find_outliers import *
from src.analizing_data_functions import *








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
