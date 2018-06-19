import pandas as pd
from matplotlib import pyplot as plt



def read_data():
    path = './Exercise/'

    train_data = pd.read_csv(path+"train.csv",delimiter=';', sep='delimiter')
    print('-----train data ----')
    print(train_data.head(), '\n')

    test_data = pd.read_csv(path+"test.csv",delimiter=';', sep='delimiter')
    print('-----test data ----')
    print(test_data.head(), '\n')

    users_data = pd.read_csv(path+"users.csv",delimiter=';', sep='delimiter')
    print('-----users data ----')
    print(users_data.head(), '\n')

    products_data = pd.read_csv(path+"products.csv",delimiter=';', sep='delimiter')
    print('-----products data ----')
    print(products_data.head(), '\n')

    return train_data, test_data, users_data, products_data




def check_nulls(train_data, test_data, users_data, products_data):

    # Vamos a ver los null que hay
    train_null = train_data.isnull().sum()
    test_null = test_data.isnull().sum()
    user_null = users_data.isnull().sum()
    product_null = products_data.isnull().sum()

    return 0



def data_shape(train_data, test_data, users_data, products_data):

    # vamos con el tamaño de los datasets
    train_shape = train_data.shape
    test_shape = test_data.shape
    user_shape = users_data.shape
    products_shape = products_data.shape

    return 0


def data_description(train_data, test_data, users_data, products_data):

    # Vemos la descripcion
    user_id_describe = users_data['user_id'].describe()
    print('---User data - user_id describe','\n', user_id_describe, '\n')

    products_id_describe = products_data['product_id'].describe()
    print('---Product data - product_id describe','\n', products_id_describe, '\n')

    train_tag_id_describe = train_data[['tag_id','post_id', 'product_id', 'user_id', 'date_tag', 'color']].describe()
    print('---Train data - train_id describe','\n', train_tag_id_describe, '\n')

    return 0


def duplicidades(train_data, test_data, users_data, products_data):
    # vamos a ver las duplicidades
    duplicated = users_data['country'].duplicated().sum()
    print(duplicated)


def analizamos_fechas(train_data, test_data, users_data, products_data):

    ## Vamos a ver las fechas de los test
    print(users_data.date_joined.min())

    # Vamos a mostrar: los usuarios por fecha
    # prirmero tenemos quee contar los usuarios en cada fecha
    users_date_joined = users_data.groupby('date_joined').user_id.count()# .plot(kind='bar')
    print(users_date_joined.min())
    #plt.show()

    # Vamos a mostrar en el subset de train por fecha
    train_date_tag = train_data.groupby('date_tag').count()
    #print('PRINT TRAIN DATE TAG:','\n', train_date_tag)

    duplicated_train = train_data.duplicated()
    #print(duplicated_train.sum()) # el resultado es 0

    return 0


def agrupamos(train_data, test_data, users_data, products_data):

    train_post_id = train_data.groupby('post_id').count()
    print('PRINT TRAIN post id:','\n', train_post_id)

    ##  Vamos a ver los likes en funcion de las demas variables
    likes_tag_id = train_data.groupby('click_count').tag_id.count()

    plt.figure()
    users_date_joined = train_data.groupby('user_id').click_count.count().plot(kind='bar')
    plt.show()

    return 0


def buscamos_correlacion(train_data, test_data, users_data, products_data):

    correlation_train = train_data.corr()
    print(correlation_train)

    return 0


def add_datasets(train_data, test_data, users_data, products_data):

    product_list = []
    country_list = []
    user_joined_list = []

    for index, row in train_data.iterrows():

        p_id = row['product_id']
        u_id = row['user_id']

        row_product = products_data.loc[products_data['product_id'] == p_id]
        row_user = users_data.loc[users_data['user_id'] == u_id]

        product_list.append(row_product['brand_name'])
        country_list.append(row_user['country'])
        user_joined_list.append(row_user['date_joined'])

    train_data['product_brand'] = product_list
    train_data['country'] = country_list
    train_data['date_joined'] = user_joined_list

    return train_data

if __name__ == '__main__':
    train_data, test_data, users_data, products_data = read_data()
    # buscamos_correlacion(train_data, test_data, users_data, products_data)

    add_datasets(train_data, test_data, users_data, products_data)


    print('hola')
