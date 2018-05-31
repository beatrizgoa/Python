#ejercicio página 250 del libro de inteligencia artificial

from nltk.tokenize import sent_tokenize, word_tokenize, WordPunctTokenizer
import numpy as np
from nltk.corpus import brown


def text2token(text):
    # Esta funcion pasa de texto a tokens

    sentence_tokens = sent_tokenize(text)
    word_tokens = word_tokenize(text)
    word_punt_tokens = WordPunctTokenizer().tokenize(text)

    return [sentence_tokens, word_tokens, word_punt_tokens]


def text2chunks(text, N):
    # Esta funcion divide el text en chunks de N palabras

    text = text.split(' ')
    chunk_list = []
    aux_list = []
    iter = 0
    for word in text:
            iter +=1
            if iter <= N:
                aux_list.append(word)
            else:
                iter = 1
                chunk_list.append(aux_list)
                aux_list = []
                aux_list.append(word)

    if iter != 0:
        chunk_list.append(aux_list)

    return chunk_list


if __name__ == '__main__':

    text = 'Hola que tal estas, yo muy bien, me alegro que me preguntes, hoy hace un buen dia, o no, porque llueve, vaya, queremos que salga el sol, por favor.'

    # convertimos el texto a tokens
    tokens_list = text2token(text)

    # convertimos el texto a chunks:
    chunk_list = text2chunks(text, 5)


    print('hola')



