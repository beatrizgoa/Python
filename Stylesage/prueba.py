import pandas as pd

path = './Exercise/'

train_data = pd.read_csv(path+"train.csv",delimiter=';', sep='delimiter')
print('-----train data ----')
print(train_data.head(), '\n')

test_data = pd.read_csv(path+"test.csv",delimiter=';', sep='delimiter')
print('-----test data ----')
print(test_data.head(), '\n')

users_data = pd.read_csv(path+"users.csv",delimiter=';', sep='delimiter')
print('-----users data ----')
print(users_data.head(), '\n')

products_data = pd.read_csv(path+"products.csv",delimiter=';', sep='delimiter')
print('-----products data ----')
print(products_data.head(), '\n')


# Vamos a ver los null que hay
train_null = train_data.isnull().sum()
test_null = test_data.isnull().sum()
user_null = users_data.isnull().sum()
product_null = products_data.isnull().sum()


# vamos con el tamaño de los datasets
train_shape = train_data.shape
test_shape = test_data.shape
user_shape = users_data.shape
products_shape = products_data.shape

# comprobamos si los id en productos son unicos y si los id de usuarios son unicos o se repiten
user_id_describe = users_data['user_id'].describe()
print('---User data - user_id describe','\n', user_id_describe, '\n')

products_id_describe = products_data['product_id'].describe()
print('---Product data - product_id describe','\n', products_id_describe, '\n')

train_tag_id_describe = train_data['tag_id'].describe()
print('---Train data - train_id describe','\n', train_tag_id_describe, '\n')



print('hola')
