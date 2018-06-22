# A parir de los datasets de train o test, le anadimos las columnas de usesrs y product data para tenerlo toodo junto


def add_datasets(train_test_data, users_data, products_data):
    # En esta funcion Cojemos el train test, y segun el producto y usuario, anadimos la marca del produto, la fecha de union del usuario y el pais

    # Se crean las listas vacias
    product_list = []
    country_list = []
    user_joined_list = []

    # Un bucle que recorre el dataser principal
    for index, row in train_test_data.iterrows():

        # se obtiene el id tanto de producto como de usuario
        p_id = row['product_id']
        u_id = row['user_id']

        # Se obtiene la fila donde est'cada id (son unicas)
        row_product = products_data.loc[products_data['product_id'] == p_id]
        row_user = users_data.loc[users_data['user_id'] == u_id]

        # Cojemos el valor de la fila que corresponde y se concatena en la lista
        try:
            product_list.append(row_product['brand_name'].values[0])
            country_list.append(row_user['country'].values[0])
            user_joined_list.append(row_user['date_joined'].values[0])

        except:
            print('hola')

    # Las nuevas listas es guardan en fichero original como una nueva columna (cada una)
    train_test_data.loc[:,'product_brand'] = product_list
    train_test_data.loc[:,'country'] = country_list
    train_test_data.loc[:,'date_joined'] = user_joined_list

    return train_test_data
