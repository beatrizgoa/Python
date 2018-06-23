import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import mean_squared_error, accuracy_score
from sklearn.ensemble import RandomForestRegressor
from src.load_save_files import *


def read_data(path = '../assets/'):
    print('......leyendo datos')
    train = pd.read_csv(path+'trainining_modified_dummies.csv',delimiter=';', sep='delimiter')
    # train['date_tag'] = pd.to_datetime(train['date_tag'])
    test = pd.read_csv(path+'testing_modified_dummies.csv')

    feature_cols = ['tag_id', 'post_id', 'product_id', 'user_id', 'color', 'date_tag', 'product_brand', 'date_joined', 'country']
    x = train[feature_cols]
    y = train.click_count

    print('x head:', '\n', x.head(), '\n')

    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1)

    return x_train, x_test, y_train, y_test




def train_predict_regression(x_train, x_test, y_train):
    print('........ regresion logistica')
    regresion = LogisticRegression()
    regresion.fit(x_train, y_train)
    pred = regresion.predict(x_test)

    return pred



def train_decission_tree(x_train, x_test, y_train):
    print('...... decision tree')
    tree = DecisionTreeClassifier()
    tree.fit(x_train,y_train)
    y_pred = tree.predict(x_test)

    return y_pred


def find_features(X, y, features):
    forest = RandomForestRegressor()
    forest.fit(X, y)
    print(list(zip(forest.feature_importances_, features)))
    return forest



def metrics(y_test, y_pred):
    print('...... calculando metrica')

    RMS = mean_squared_error(y_test, y_pred)
    accuracy = accuracy_score(y_test, y_pred)

    return RMS, accuracy




if __name__ == '__main__':
    x_train, x_test, y_train, y_test = read_data()

    #  y_pred_regression = train_predict_regression(x_train, x_test, y_train)

    # y_pred_tree = train_decission_tree(x_train,x_test,y_train)

    # print(y_pred_tree.shape)
    # result_reg, accuracy_reg = metrics(y_test, y_pred_regression)
    # result_tree, accuracy_tree = metrics(y_test, y_pred_tree)

    # print('Regression results:', result_reg, accuracy_reg)
    # print('Dec. Tree results;', result_tree, accuracy_tree)

    features = ['post_id',  'product_id',  'user_id',  'date_tag',  'color', 'product_brand']

    forest = find_features(x_train[features], y_train, features)
    pred = forest.predict(x_test[features])
    print(mean_squared_error(y_test, pred))




## Podemos mirar en el test las fechas, si son de ahora, intentando quitar los posto viejos que tienen muy pocos likes, que tambine habia muy pocos usuarios. Pero si en el test hay fechas de todos, no
# MUestra el histograma de los likes
# Hacer una grafica en funcnion de los likes
