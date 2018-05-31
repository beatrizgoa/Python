# In this python file, the housing proces is stimated using a Support Vector Regressor

from sklearn.datasets import load_boston
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR

def load_split_data():

    # Load data
    data = load_boston()

    # Shuffle it
    X, y = shuffle(data.data, data.target, random_state = 7)

    # split into train and test subsets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    return X_train, X_test, y_train, y_test


def super_vector_repgressor_classifier(X_train, X_test, y_train):

    # Create the classifier object
    svr_classifier = SVR(kernel = 'linear', C=0.1, epsilon=0.1)

    #fit the model
    svr_classifier.fit(X = X_train, y = y_train)

    #predict
    y_pred=svr_classifier.predict(X_test)

    return y_pred

if __name__ == '__main__':

    # Load and split data
    X_train, X_test, y_train, y_test = load_split_data()

    # Fit and predict the data with SVR model
    y_pred = super_vector_repgressor_classifier(X_train, X_test, y_train)
