# This python file, follows the basics of the chapter 12 of the artificial intelligence with python book
# wth this file, the basic of the speech and audio procesing with python is explained

from scipy.io import wavfile


if __name__ == '__main__':

    #from scipy, wav file is imported
    sampling_frequency, audio_signal = wavfile.read('random_sound.wav')


    print('hola')

