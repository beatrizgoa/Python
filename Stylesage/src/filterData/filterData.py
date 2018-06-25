# filtering data

from src.filterData.utils.categoricalToNumerical import *
from src.basicPreprocessing.utils.analizingDataFunctions import grouping
from src.filterData.utils.removeOutliers import removeOutliers
from src.filterData.utils.mergeDatasets import addDatasers
from src.filterData.utils.normalize import normalization
from sklearn.ensemble import RandomForestRegressor
from src.visualizations.visualization import *
from src.loadSave.loadData import readTrainTestData



def filterData(train_data, test_data, users_data, products_data):

    # From categorical variables to numeric variables
    #  products_data['brand_name'] = dummiesLabelEncoder(products_data.brand_name)
    # users_data['country'] = dummiesLabelEncoder(users_data.country)

    # dates to ordinal numbers
    # users_data['date_joined'] = timeToOrdinal(users_data['date_joined'])
    # train_data['date_tag'] = timeToOrdinal(train_data['date_tag'])
    # test_data['date_tag'] = timeToOrdinal(test_data['date_tag'])

    # Add info from users data and products to test and train data
    # addDatasers(train_data, users_data, products_data)
    # addDatasers(test_data, users_data, products_data)


    correlation_columns = ['tag_id',  'post_id',  'product_id',  'user_id',  'date_tag',  'color', 'click_count', 'product_brand',  'country',  'date_joined']
    # plot_correlation(train_data[correlation_columns], xticks=correlation_columns, yticks=correlation_columns)

    """ Correlation:
        date of the user joininh and the user id
        id_tag and date post
        d_tag and id_post
        """

    # Show depending on click count: brand, country, color and date id
    # group_brand = grouping(train_data,'product_brand')
    #  group_country = grouping(train_data,'country')
    #group_color = grouping(train_data, 'color')
    # group_date = grouping(train_data, 'date_tag')

    # show group by data
    # groupBySubplots(group_brand, group_country, group_color, group_date)

    train_data,y, test_data = readTrainTestData()

    # Calculate the number uniques rands
    print('Number of unique brands:', len(train_data['product_brand'].unique()))
    # Calculate the number of unique posts
    print('Number of unique id posts',len(train_data['post_id'].unique()))


    # plotSns(pd.DataFrame(train_data), y_vars='click_count', x_vars=['product_brand', 'product_id', 'user_id'])

    # It could be considered as outliers the data whose click count is bigger than 5000, and they are removed
    train_data = removeOutliers(train_data)

    train_norm, test_norm = normalization(train_data, test_data)


    return train_data, test_norm

