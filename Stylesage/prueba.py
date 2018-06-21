import pandas as pd
from matplotlib import pyplot as plt



def read_data():

    # Leemos los datos y mostramos la cabecera para examinarlos

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



def read_modified_db():

    # En esta funcion leemos los archivos de train y test modificados

    path = './Exercise/'

    train_data = pd.read_csv(path+"training_modified.csv",delimiter=';', sep='delimiter')
    print('-----train data ----')
    print(train_data.head(), '\n')

    test_data = pd.read_csv(path+"testing_modified.csv",delimiter=';', sep='delimiter')
    print('-----test data ----')
    print(test_data.head(), '\n')

    return train_data, test_data



def check_nulls(train_data, test_data, users_data, products_data):

    # Con esta funcion chekeamos si es nulo algún valor

    # Vamos a ver los null que hay
    train_null = train_data.isnull().sum()
    test_null = test_data.isnull().sum()
    user_null = users_data.isnull().sum()
    product_null = products_data.isnull().sum()

    # Se obtiene que es nulo en la descripcion del producto (solo)

    print('train: ', train_null, '\n', 'test: ', test_null, '\n', 'user: ', user_null, '\n', 'product: ', product_null)

    return 0



def data_shape(train_data, test_data, users_data, products_data):

    # Para ver la cantidad de datos que hay

    # vamos con el tamaño de los datasets
    train_shape = train_data.shape
    test_shape = test_data.shape
    user_shape = users_data.shape
    products_shape = products_data.shape

    return 0


def data_description(train_data, test_data, users_data, products_data):

    # MOstramos la descripcion de los databases

    # Vemos la descripcion
    user_id_describe = users_data['user_id'].describe()
    print('---User data - user_id describe','\n', user_id_describe, '\n')

    products_id_describe = products_data['product_id'].describe()
    print('---Product data - product_id describe','\n', products_id_describe, '\n')

    train_tag_id_describe = train_data[['tag_id','post_id', 'product_id', 'user_id', 'date_tag', 'color']].describe()
    print('---Train data - train_id describe','\n', train_tag_id_describe, '\n')

    return 0


def duplicidades(data, column):
    # vamos a ver las duplicidades
    duplicated = data[column].duplicated().sum()
    print(duplicated)

    return 0


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


def agrupamos(database, param):
    # Funcion para agrupar en funcion de los clicks count

    plt.figure()
    database.groupby(param).click_count.count().plot(kind='bar')
    plt.show()

    return 0


def buscamos_correlacion(input_data):

    # Se busca correlacion en el entrenamiento
    correlation = input_data.corr()
    print(correlation)

    return 0


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




def count_click_intervals(database):

    lenght = database.shape[0]

    first = len(database[(train_mod.click_count >=0) & (train_mod.click_count < 10)])
    second = len(database[(train_mod.click_count >=10) & (train_mod.click_count < 20)])
    third = len(database[(train_mod.click_count >=20) & (train_mod.click_count < 50)])
    fouth = len(database[(train_mod.click_count >=50) & (train_mod.click_count < 1000)])
    fifth = len(database[(train_mod.click_count >=1000)])

    print('first interval has:', first, first/lenght*100,'%')
    print('second interval has:', second, second/lenght*100,'%')
    print('third interval has:', third, third/lenght*100,'%')
    print('fouth interval has:', fouth, fouth/lenght*100,'%')
    print('fifth interval has:', fifth, fifth/lenght*100,'%')

    assert (first+second+third+fouth+fifth == lenght)
    return 0

def convert_to_dummies(columna):

    return pd.get_dummies(columna)

if __name__ == '__main__':
    train_data, test_data, users_data, products_data = read_data()
    train_mod, test_mod = read_modified_db()


    # buscamos_correlacion(train_data, test_data, users_data, products_data)

    # Creamos los nuevos datasets mezclados
    # new_training = add_datasets(train_data,  users_data, products_data)
    # new_testing =  add_datasets(test_data, users_data, products_data)

    # Los guardamos en csv
    # new_testing.to_csv('./Exercise/testing_modified.csv', sep=';')
    # new_training.to_csv('./Exercise/training_modified.csv', sep=';')

    # Con los nuevos datasets mezclados vamos a ver si hay algun valor nulo:
    # check_nulls(train_data, test_data, users_data, products_data)

    # Duplicidades:
    # duplicidades(train_data, 'tag_id')
    # duplicidades(users_data, 'user_id')
    # duplicidades(products_data, 'product_id')

    # agrupamos
    # agrupamos(train_mod, 'product_brand')

    print((train_mod == 2).astype(int).sum(axis=0))

    print(len(test_mod['product_brand'].unique()))

    # COntamos los intervalos de clicks que hay
    count_click_intervals(train_mod)

    # country_dummies = onvert_to_dummies(columna):

    print('hola')
