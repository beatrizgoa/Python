# This python file, follows the basics of the chapter 12 of the artificial intelligence with python book
# wth this file, the basic of the speech and audio procesing with python is explained

from scipy.io import wavfile
from numpy import power, fft, pi, linspace, sin, random


def normalize_signal(audio_signal):

    singal_nm = audio_signal/power(2,15) # el 2 y e 15 no se por qué

    return singal_nm


def to_frecuency_domain(audio_signal):

    return fft.fft(audio_signal)

def generate_audio(duration, tone_frec, sampling_frec = 44100, amplitud = 2*pi):

    #define t
    t = linspace(-2*amplitud, 2*amplitud, duration*sampling_frec)
    #define the signal
    signal =  sin(amplitud*tone_frec*t)

    #create noise
    noise = .5 * random.rand(duration*sampling_frec)

    return signal+noise

if __name__ == '__main__':

    #from scipy, wav file is imported
    sampling_frequency, audio_signal = wavfile.read('random_sound.wav')

    #normalize the signal
    singal_nm = normalize_signal(audio_signal)

    create_audio = generate_audio(duration = 10, sampling_frec = 44100, tone_frec = 700, amplitud = 2*pi)

    print('hola')

