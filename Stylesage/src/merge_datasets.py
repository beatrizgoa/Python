


def add_datasets(train_test_data, users_data, products_data):
    # En esta funcion Cojemos el train test, y segun el producto y usuario, anadimos la marca del produto, la fecha de union del usuario y el pais

    product_list = []
    country_list = []
    user_joined_list = []

    for index, row in train_test_data.iterrows():

        p_id = row['product_id']
        u_id = row['user_id']


        row_product = products_data.loc[products_data['product_id'] == p_id]
        row_user = users_data.loc[users_data['user_id'] == u_id]
        try:
            product_list.append(row_product['brand_name'].values[0])
            country_list.append(row_user['country'].values[0])
            user_joined_list.append(row_user['date_joined'].values[0])
        except:
            print('hola')

    train_test_data.loc[:,'product_brand'] = product_list
    train_test_data.loc[:,'country'] = country_list
    train_test_data.loc[:,'date_joined'] = user_joined_list

    return train_test_data
