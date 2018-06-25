# EN este fichero hay funciones que se van a utilizar para eralizar el analisis de los datos
from matplotlib import pyplot as plt
from numpy import arange

def checkNulls(data, remove = False):
    # Con esta funcion chekeamos si es nulo algún valor

    # Vamos a ver los null que hay
    null = data.isnull().sum()
    aux = 0

    for i in null.values:
        if i != 0:
            print('The database has null values:', '\n', null, '\n')

    if remove == True:
        data.dropna(axis = 0, inplace = True)

    return 0



def dataDescription(database, column):
    # MOstramos la descripcion de la database con la/las columnas que se pasen

    # Vemos la descripcion
    description = database.describe()
    print('description of the ', column, '\n', description, '\n')

    return 0



def data_shape(train_data, test_data, users_data, products_data):

    # Para ver la cantidad de datos que hay

    # vamos con el tamaño de los datasets
    train_shape = train_data.shape
    test_shape = test_data.shape
    user_shape = users_data.shape
    products_shape = products_data.shape


    return 0


def removeDuplicated(data):
    # Remove duplicated rows
    return data.drop_duplicates(keep='first', inplace=True)




def dateAnalyzing(users_data, train_data):

    ## VIsualize teain and users dates
    print('USERS: max date:,', users_data.date_joined.min(), 'min date:', users_data.date_joined.max(), 'number of unique dates', len(users_data['date_joined'].unique()))
    print('TRAIN: max date:,', train_data.date_tag.min(), 'min date:', train_data.date_tag.max(), 'number of unique dates', len(train_data['date_tag'].unique()))

    # show users by date
    plt.figure()
    plt.subplot(211)
    users_date_joined = users_data.groupby('date_joined').user_id.count().plot(kind='bar')
    plt.ylabel('number of users')
    plt.subplot(212)
    train_date_tag = train_data.groupby('date_tag').tag_id.count().plot(kind='bar')
    plt.ylabel('number of tags_id')
    plt.show()

    return 0



def grouping(database, param):
    # funtion to group by click count data

    # plt.figure()
    group = database.groupby(param).click_count.count()# .plot(kind='bar')
    # plt.show()

    return group






def countClickIntervals(database):
    # EN esta funcion vamos a analizar la cantidad de click counts que hay

    lenght = database.shape[0]

    # Se calculan los clicks en funcion de los intervalos
    first = len(database[(database.click_count >=0) & (database.click_count < 10)])
    second = len(database[(database.click_count >=10) & (database.click_count < 20)])
    third = len(database[(database.click_count >=20) & (database.click_count < 50)])
    fouth = len(database[(database.click_count >=50) & (database.click_count < 1000)])
    fifth = len(database[(database.click_count >=1000)])

    # Se muestra al usuario
    print('first interval has:', first, first/lenght*100,'%')
    print('second interval has:', second, second/lenght*100,'%')
    print('third interval has:', third, third/lenght*100,'%')
    print('fouth interval has:', fouth, fouth/lenght*100,'%')
    print('fifth interval has:', fifth, fifth/lenght*100,'%')

    # Nos aseguramos que tienen el mismo numero de likes y no nos hemos dejado ninguno
    assert (first+second+third+fouth+fifth == lenght)

    x = [first, second, third, fouth, fifth]

    # Analizamos el primero y segundo intervalo mas en detalle
    intervalos_valores = []
    for i in range(0,22,2):
            intervalos_valores.append(len(database[(database.click_count >=i) & (database.click_count < (i+2))]))


    # PLot distribution samples

    plt.figure(1)
    plt.plot(x)
    plt.xticks(arange(5), ('0-10', '10-20', '20-50', '50-100', '>1000'))
    plt.xlabel('click counts')


    plt.figure(2)
    plt.plot(arange(0, 22, step=2),intervalos_valores)
    plt.xticks(arange(22, step=2))
    plt.xlabel('click counts')

    plt.show()

    return 0



def uniqueTrainTestDates(train, test):
    # Vamos a ver si son las mismas fechas las de train que las de test, en la publicacion tag_id
    unique_date_train = train['date_tag'].unique()
    unique_date_test = test['date_tag'].unique()

    # Sabemos si tienen la misma longitud
    print('longitud', len(unique_date_train) == len(unique_date_test))

    print(unique_date_test,unique_date_train)

