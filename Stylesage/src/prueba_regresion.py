from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import mean_squared_error, accuracy_score
from sklearn.ensemble import RandomForestRegressor
from src.utils.load_save_files import *
from sklearn.model_selection import cross_val_score


def randomForest(x_train, y, x_test):

    # Define the possible number of trees
    trees = [2,5,10,20,30,40,50,100,150]
    scores = []

    # Foor loop to generate random forest regression modesl with the different estimators
    for tree in trees:
        forest = RandomForestRegressor(n_estimators=tree)
        scores.append(cross_val_score(forest, x_train, y, cv=5, scoring='neg_mean_squared_error').mean())

    #Get the best number of trees
    best_tree = trees[scores.index(min(scores))]
    print(best_tree, scores)

    # Train with the best number of trees and predict
    forest = RandomForestRegressor(n_estimators=best_tree)
    forest.fit(x_train, y)

    y_pred = forest.predict(x_test)

    return y_pred






def read_split_data(path = '../assets/'):
    print('..... reading data')
    train = pd.read_csv(path+'trainining_modified_dummies.csv',delimiter=';', sep='delimiter')
    # train['date_tag'] = pd.to_datetime(train['date_tag'])
    test = pd.read_csv(path+'testing_modified_dummies.csv')

    feature_cols = ['tag_id', 'post_id', 'product_id', 'user_id', 'color', 'date_tag', 'product_brand', 'date_joined', 'country']
    x = train[feature_cols]
    y = train.click_count
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1)


    return x_train, x_test, y_train, y_test


def train_predict_regression(x_train, x_test, y_train):
    print('........ logistic_regression')
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
    print('...... calculing the results')

    RMS = mean_squared_error(y_test, y_pred)
    accuracy = accuracy_score(y_test, y_pred)

    return RMS, accuracy


def savePredictionCSV(y_pred, x_test):
    df_results = pd.DataFrame(x_test['tag_id'])
    df_results['click_count'] = y_pred

    saveCSV(df_results, 'results')



if __name__ == '__main__':
    x_train,  y_train, x_test = readData()

    #  y_pred_regression = train_predict_regression(x_train, x_test, y_train)

    # y_pred_tree = train_decission_tree(x_train,x_test,y_train)

    # print(y_pred_tree.shape)
    # result_reg, accuracy_reg = metrics(y_test, y_pred_regression)
    # result_tree, accuracy_tree = metrics(y_test, y_pred_tree)

    # print('Regression results:', result_reg, accuracy_reg)
    # print('Dec. Tree results;', result_tree, accuracy_tree)

    features = ['post_id',  'product_id',  'user_id',  'date_tag',  'color', 'product_brand']

    y_pred = randomForest(x_train,y_train,x_test)

    savePredictionCSV(y_pred, x_test)
    # forest = find_features(x_train[features], y_train, features)
    # pred = forest.predict(x_test[features])
    # print(mean_squared_error(y_test, pred))




