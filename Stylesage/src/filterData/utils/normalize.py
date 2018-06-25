from sklearn import preprocessing



def normalization(train, test):
    # normalize values
    columns = ['tag_id', 'post_id', 'product_id', 'user_id', 'product_brand']

    # create and train the object. Transform the values
    scaler = preprocessing.MinMaxScaler()
    train_scaled = scaler.fit_transform(train[columns].values)
    test_scaled = scaler.transform(test[columns].values)

    # asociate each scaled data to its corresponing column of the dataframe
    train.loc[:,'tag_id'] = train_scaled[:,0]
    train.loc[:,'post_id'] = train_scaled[:,1]
    train.loc[:,'product_id'] = train_scaled[:,2]
    train.loc[:,'user_id'] = train_scaled[:,3]
    train.loc[:,'product_brand'] = train_scaled[:,4]


    test.loc[:,'tag_id'] = test_scaled[:,0]
    test.loc[:,'post_id'] = test_scaled[:,1]
    test.loc[:,'product_id'] = test_scaled[:,2]
    test.loc[:,'user_id'] = test_scaled[:,3]
    test.loc[:,'product_brand'] = test_scaled[:,4]


    return train, test
