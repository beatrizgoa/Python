# En este archivo de python se va a analizar los datasets proporcionados

from src.utils.load_save_files import *
from src.utils.analizing_data_functions import *
import seaborn as sns





if __name__ == '__main__':

    # Load dataser
    train_data, test_data, users_data, products_data = read_data()

    """ Numeric and categorical values
        train and test: all numerical data but date tag
        users categorical: data_joined and country
        products: just product_id is an ordinal variable
    """

    # how many data are
    data_shape(train_data, test_data, users_data, products_data)

    """ CSV shape 
        Train: 416147
        Test: 46239
        Usuario: 68819
        Producto: 309961
    """

    # Users, products and tag are unique:
    removeDuplicated(train_data)   # obtenemos: tag_id column of your data is not duplicated
    removeDuplicated(users_data) # obtenemos: user_id column of your data is not duplicated
    removeDuplicated(products_data) #

    # Null values
    checkNulls(train_data, remove= False) # No null values
    checkNulls(test_data, remove= False) # No null values
    checkNulls(users_data, remove= False) # No null values
    checkNulls(products_data, remove= False) # product_info: 443 null values and description: 81381 null values


    # cluck count description
    data_description(train_data, 'click_count')

    # click count distribution
    count_click_intervals(train_data) # Most of tag id have only 1 click, then 0 clicks
    # It is not possible detecting outliers by the moment

    # analize the data tange in users and train
    dateAnalyzing(users_data, train_data)

    """
    USUARIOS: maxim date:, 2016-01-21 minim date: 2017-06-30 unique dates 522
    TRAIN: maxim date:, 2017-04-23 minim date:: 2017-06-19 unique dates 58
    
    Number of users increases with the time. las few dates i where the number of new users is widely higher     
    """

    # Msample distribution
    g = sns.pairplot(train_data[['tag_id',  'post_id',  'product_id',  'user_id', 'click_count']], diag_kind="kde", markers='+')
    plt.show()

    # cHow many unique users are in the training subset?
    print('The number of unique users are:', len(train_data['user_id'].unique()))





