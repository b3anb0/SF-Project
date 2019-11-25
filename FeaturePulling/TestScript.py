from scipy.io import wavfile

frate,data = wavfile.read('../84-121123-0005.wav')
for i in data:
    print(i)
