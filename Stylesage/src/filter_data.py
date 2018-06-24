# En este archivo de python filtro los row datos y se selecionan las features para la psoterios classificacion

from src.utils.load_save_files import *
from src.utils.categorical_to_numerical import *
from src.utils.analizing_data_functions import *
from src.utils.removeOutliers import removeOutliers
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor


def find_features(X, y, features):
    print('calculing features scores .... ')
    forest = RandomForestRegressor()
    forest.fit(X, y)
    print(sorted(list(zip(forest.feature_importances_, features))))
    return forest


if __name__ == '__main__':
    # Read dat
    # train_data, test_data, users_data, products_data = read_data()

    # From categorical variables to numeric variables
    # products_data['brand_name'] = dummies_labelEncoder(products_data.brand_name)
    # users_data['country'] = dummies_labelEncoder(users_data.country)

    # dates to ordinal numbers
    # users_data['date_joined'] = time_to_ordinal(users_data['date_joined'])
    # train_data['date_tag'] = time_to_ordinal(train_data['date_tag'])
    # test_data['date_tag'] = time_to_ordinal(test_data['date_tag'])

    # Add info from users data and products to test and train data
    # add_datasets(train_data, users_data, products_data)
    # add_datasets(test_data, users_data, products_data)

    train_data, test_data = read_modified_db()

    # correlacion among variables
    plt.matshow(train_data[['tag_id',  'post_id',  'product_id',  'user_id',  'date_tag',  'color', 'click_count', 'product_brand',  'country',  'date_joined' ]].corr())
    plt.legend()
    plt.xticks(arange(10), ('tag_id',  'post_id',  'product_id',  'user_id',  'date_tag',  'color', 'click_count', 'product_brand',  'country',  'date_joined'))
    plt.yticks(arange(10), ('tag_id',  'post_id',  'product_id',  'user_id',  'date_tag',  'color', 'click_count', 'product_brand',  'country',  'date_joined'))
    plt.show()

    """ Correlation:
        date of the user joininh and the user id
        id_tag and date post
        d_tag and id_post
        """

    # Show depending on click count: brand, country, color and date id
    plt.figure()
    group_brand = grouping(train_data,'product_brand')
    group_country = grouping(train_data,'country')
    group_color = grouping(train_data, 'color')
    group_date = grouping(train_data, 'date_tag')

    plt.subplot(221)
    plt.plot(group_brand)
    plt.xlabel('product brand')

    plt.subplot(222)
    group_country.plot(kind='bar')
    plt.xlabel('country')

    plt.subplot(223)
    group_color.plot(kind='bar')
    plt.xlabel('color')

    plt.subplot(224)
    plt.plot(group_date)
    plt.xlabel('date tag')
    plt.show()

    # Calculate the number uniques rands
    print('La cantidad de marcas unicas es:', len(train_data['product_brand'].unique()))
    # Calculate the number of unique posts
    print('La cantidad de id post unicas es:',len(train_data['post_id'].unique()))

    sns.pairplot(pd.DataFrame(train_data), y_vars='click_count', x_vars=['product_brand', 'product_id', 'user_id', ])
    plt.show()
    
    # It could be considered as outliers the data whose click count is bigger than 5000, and they are removed
    train_data = removeOutliers(train_data)

    # Random forest to calcuate the importance of the features
    features = ['post_id',  'product_id',  'user_id',  'date_tag',  'color', 'product_brand'] # faltan tag_id, country, user_data joined
    # forest = find_features(train_data[features], train_data, features)

    # Como el id del tag se repite en la correlacion, se puede quitar, ademas que es un valor unico, es como enumerar el train
    # A partir de la correlacion y de random forest tambien podemos quitar user_data_joined

