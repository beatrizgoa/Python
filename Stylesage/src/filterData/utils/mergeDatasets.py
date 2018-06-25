
def addDatasers(train_test_data, users_data, products_data):
    # add data from the users and products dataser to the train or test data
    # empty lists
    product_list = []
    country_list = []
    user_joined_list = []

    # loop to get data from the train/test db
    for index, row in train_test_data.iterrows():

        # get ids
        p_id = row['product_id']
        u_id = row['user_id']

        # get rows of each ids
        row_product = products_data.loc[products_data['product_id'] == p_id]
        row_user = users_data.loc[users_data['user_id'] == u_id]

        # cocatene the obtained data
        product_list.append(row_product['brand_name'].values[0])
        country_list.append(row_user['country'].values[0])
        user_joined_list.append(row_user['date_joined'].values[0])


    # save new lists in the train/test subsets
    train_test_data.loc[:,'product_brand'] = product_list
    train_test_data.loc[:,'country'] = country_list
    train_test_data.loc[:,'date_joined'] = user_joined_list

    return train_test_data
