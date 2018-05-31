# Ejercicio de la pagina 266 del libro de artificial intelligence with python
# Se va a usar el dataset de sklearn que se llama fecth_20newsgroups

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB


if __name__ == '__main__':

    # primero definimos las categorias:
    # El nombre de las categorías es el nombre que le dan en el dataset de sklearn

    categorias = {'talk.politics.misc': 'Politics', 'rec.autos': 'Autos', 'rec.sport.hockey': 'Hockey', 'sci.electronics': 'Electronics', 'sci.med': 'Medicine'}

    # obtenemos el subset de entrenamiento de la libreria de sklearn
    # Aqui vemos porque las categorias van en un diccionario y de esa manera

    training_data = fetch_20newsgroups(subset='train', categories=categorias.keys(), shuffle=True, random_state=5)

    test = ['You need to be careful with cars when you are driving on slippery roads',
                        'A lot of devices can be operated wirelessly',
                        'Players need to be careful when they are close to goal posts',
                        'Political debates help us understand the perspectives of both sides']


    # la frecuencia de ocurrencia del término en la colección de documentos, es una medida numerica que expresa cuan relevante es una palabra para un documento en una coleccion.
    # Each unique word in our dictionary will correspond to a feature (descriptive feature).
    # Con el count vector se saca el vector de caracteristicas por palabra usando bag of words
    count_vectorizer = CountVectorizer() # Se define el objeto
    train_tc = count_vectorizer.fit_transform(training_data.data) # se entrena, y te devuelve la transformada
    test_tc = count_vectorizer.transform(test)


    # Se hace lo mismo para calcular la trasnsformada de  la frecuencia inversa del documento
    # we can even reduce the weightage of more common words like (the, is, an etc.) which occurs in all document. This is called as TF-IDF i.e Term Frequency times inverse document frequency.
    t_inversa = TfidfTransformer()
    train_ti = t_inversa.fit_transform(train_tc)  # Entrenamos con los resultados transformados del count vectorizer
    test_ti = t_inversa.transform(test_tc)


    # Ahora se define el clasificador, se entrena y se testea
    # Se usa como clasificador Multinomial bayes
    naives = MultinomialNB()
    naives_trained = naives.fit(train_ti,training_data.target)
    y_pred = naives.predict(test_ti)

    print(training_data.target_names[0])
    print('\n \n \n')


    for sent, category in zip(test, y_pred):
        print('sent:', sent, '\\\\\\', 'category:', category)
        print('\nInput:', sent, '\nPredicted category:', categorias[training_data.target_names[category]])
        print('\n \n')
