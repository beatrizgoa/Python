from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score


def randomForest(x_train, y, x_test):
    print('.....working random forest')
    # Define the possible number of trees
    trees = [2,5,10,20,30,]#40,50,100,150]
    scores = []

    # Foor loop to generate random forest regression modesl with the different estimators
    for tree in trees:
        print('tree', tree)
        forest = RandomForestRegressor(n_estimators=tree)
        scores.append(cross_val_score(forest, x_train, y, cv=3, scoring='neg_mean_squared_error').mean())

    #Get the best number of trees
    best_tree = trees[scores.index(max(scores))]
    print('best tree', best_tree, scores)

    # Train with the best number of trees and predict
    forest = RandomForestRegressor(n_estimators=best_tree)
    forest.fit(x_train, y)

    y_pred = forest.predict(x_test)

    return y_pred



def optimVariables(X, y, features):
    forest = RandomForestRegressor()
    forest.fit(X, y)
    feat_score = zip(forest.feature_importances_, features)
    return forest, feat_score



def trainPredict(train, test):

    # Get the importance of variables
    features = ['tag_id', 'post_id',  'product_id',  'user_id',  'date_tag',  'color', 'product_brand']
    x = train[features]
    y = train['click_count']
    test = test[features]

    forest, feat_score = optimVariables(train[features], y, features)
    print('FEAT SCORE', list(feat_score))

    features= ['tag_id', 'post_id',  'product_id',  'user_id', 'product_brand']

    y_pred = randomForest(x[features], y, test[features])

    return y_pred
