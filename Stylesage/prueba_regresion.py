import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import mean_squared_error, accuracy_score

def read_data(path = './Exercise/'):
    print('......leyendo datos')
    train = pd.read_csv(path+'train.csv',delimiter=';', sep='delimiter')
    train['date_tag'] = pd.to_datetime(train['date_tag'])
    test = pd.read_csv(path+'test.csv')

    print(train.head())

    x = train[['tag_id', 'post_id']]#, 'product_id', 'user_id', 'color']]
    y = train['click_count']

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


def metrics(y_test, y_pred):
    print('...... calculando metrica')

    RMS = mean_squared_error(y_test, y_pred)
    accuracy = accuracy_score(y_test, y_pred)

    return RMS, accuracy




if __name__ == '__main__':
    x_train, x_test, y_train, y_test = read_data()

    y_pred_regression = train_predict_regression(x_train, x_test, y_train)
    y_pred_tree = train_decission_tree(x_train,x_test,y_train)
    result_reg, accuracy_reg = metrics(y_train, y_pred_regression)
    result_tree, accuracy_tree = metrics(y_train, y_pred_tree)

    print('Regression results:', result_reg, accuracy_reg)
    print('Dec. Tree results;', result_tree, accuracy_tree)



## Podemos mirar en el test las fechas, si son de ahora, intentando quitar los posto viejos que tienen muy pocos likes, que tambine habia muy pocos usuarios. Pero si en el test hay fechas de todos, no
# MUestra el histograma de los likes
# Hacer una grafica en funcnion de los likes
