from scipy.io import wavfile
import subprocess

#https://aubio.org/manual/latest/cli.html


'''This function can return over half a million
   data points for a thirty second file, and we're
   not sure what data it's actually returning.
   Use cautiously
'''
def getFreqs(file):
	rate,data = wavfile.read(file)
	return data





def getPitches(file):
	results=subprocess.check_output("aubio pitch "+file)
	broken=[o for o in str(results).split('\\t')]
	broken=[p.split('\\r\\n') for p in broken][1:-1]
	pitches=[l[0] for l in broken]
	return pitches
def getBeatTimes(file):
	results=subprocess.check_output("aubio beat "+file)
	broken=[o.replace("b'",'') for o in str(results).split('\\t\\r\\n')[:-1]]
	beats=broken
	return beats
def getTempo(file):
	results=str(subprocess.check_output("aubio tempo "+file)).replace(' bpm\\r\\n','').replace("'",'').replace("b",'')
	return results

def getMfcc(file):#mel-frequency cepstrum coefficients
	results=str(subprocess.check_output("aubio mfcc "+file)).replace("'",'').replace("b",'')
	mfcc=[o.replace('\\r','').split("\\t") for o in results.split("\\n")][:-1]
	return mfcc
def getMelbands(file):#mel-frequency energies per band
	results=str(subprocess.check_output("aubio melbands "+file)).replace("'",'').replace("b",'')
	melbands=[o.replace('\\r','').split("\\t") for o in results.split("\\n")][:-1]
	return melbands

print(getMelbands("TestFile.wav"))
