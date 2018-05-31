# In this python exercise, a single variable regressor is built

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt


def load_data_and_split():

    # read the txt file and obtain the data and its labels.
    txt = np.loadtxt('data_singlevar_regr.txt', delimiter=',')
    X,y = txt[:,:-1], txt[:,-1]

    # the data is split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    return X_train, X_test, y_train, y_test


def single_regresion_train_test(X_train, X_test, y_train):

    # The classifier object is defined
    single_regression = LinearRegression()

    # the classifier is trained
    single_regression.fit(X=X_train, y=y_train)

    # the classifier tests with the trained model
    y_pred = single_regression.predict(X_test)

    return y_pred

if __name__ == '__main__':

    # get train and test substets of data
    X_train, X_test, y_train, y_test = load_data_and_split()

    # train and test the regression
    y_pred = single_regresion_train_test(X_train, X_test, y_train)


    # plot the data
    plt.scatter(X_test, y_test, color='green')
    plt.plot(X_test, y_pred, color='black', linewidth=4)
    plt.xticks(())
    plt.yticks(())
    plt.show()






