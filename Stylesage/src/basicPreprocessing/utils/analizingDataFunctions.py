# EN este fichero hay funciones que se van a utilizar para eralizar el analisis de los datos
from numpy import arange
from src.visualizations import visualization

def checkNulls(data, remove = False):
    # with this function, the null values are cheked and remove if is desired

    # Vamos a ver los null que hay
    null = data.isnull().sum()
    aux = 0

    for i in null.values:
        if i != 0:
            aux = 1
            continue

    if aux == 1:
        print('The database has null values:', '\n', null, '\n')

    if remove == True:
        data.dropna(axis = 0, inplace = True)

    return 0



def dataDescription(database, column):

    # Vshow description
    description = database.describe()
    print('description of the ', column, '\n', description, '\n')

    return 0



def dataShape(data):

    # To know the sape of the dataset
    data_shape = data.shape
    return 0


def removeDuplicated(data):
    # Remove duplicated rows
    return data.drop_duplicates(keep='first', inplace=True)




def dateAnalyzing(users_data, train_data):

    ## VIsualize teain and users dates
    print('USERS: max date:,', users_data.date_joined.min(), 'min date:', users_data.date_joined.max(), 'number of unique dates', len(users_data['date_joined'].unique()))
    print('TRAIN: max date:,', train_data.date_tag.min(), 'min date:', train_data.date_tag.max(), 'number of unique dates', len(train_data['date_tag'].unique()))

    visualization.twoGroupedSubplot(users_data.groupby('date_joined').user_id.count(), train_data.groupby('date_tag').tag_id.count() ,  data1_label = 'numer of users', data2_label ='number tag id' )

    return 0



def grouping(database, param):
    # funtion to group by click count data

    group = database.groupby(param).click_count.count()# .plot(kind='bar')

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

    visualization.twoSimpleSubplot(data1 = x, data2 = [arange(0, 22, step=2), intervalos_valores], data1_xticks = [arange(5), ('0-10', '10-20', '20-50', '50-100', '>1000')],data2_xticks= arange(22, step=2),data1_label = 'click counts', data2_label ='click counts')




def uniqueTrainTestDates(train, test):
    # Vamos a ver si son las mismas fechas las de train que las de test, en la publicacion tag_id
    unique_date_train = train['date_tag'].unique()
    unique_date_test = test['date_tag'].unique()

    # Sabemos si tienen la misma longitud
    print('longitud', len(unique_date_train) == len(unique_date_test))

    print(unique_date_test,unique_date_train)

