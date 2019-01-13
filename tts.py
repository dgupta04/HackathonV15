from gtts import gTTS
from pydub import AudioSegment
import random
import librosa

def stretch(f):
    y,sr = librosa.load(f)
    y_modified = librosa.effects.time_stretch(y,random.uniform(0.75,1.4))
    librosa.output.write_wav(f, y_modified, sr)

def overlap_audio(f1,f2):
    #overlaps 2 audio files
    sound1 = AudioSegment.from_file(f1)
    sound2 = AudioSegment.from_file(f2)
    combined = sound1.overlay(sound2)
    combined.export("final_aud.wav", format='wav')

def joinwav(f, f3):
    combined_wav = AudioSegment.empty()
    for i in range(len(f)):
    	combined_wav += AudioSegment.from_wav(f[i])
    combined_wav.export(f3,"wav")

def cat_audio(s):
	a = []
	b = []
	f=s.split()
	for i in range(len(f)):
		if i in b:
			continue
		if len(f[i]) <= 3 and i!=len(f)-1:
			a.append(f[i] + ' ' + f[i+1])
			b.append(i+1)
		else:
			a.append(f[i])
	return a

text = input("Enter text to be spoken(without carriage return):\n")
inpFile = input("Enter file name of song to be used as background(with appropriate extension):")
tts = gTTS(text,'en')
tts.save("l.mp3")

list_audio = ['useless.wav']*70

y = inpFile

for i in cat_audio(text):
	tts = gTTS(i,'en')
	tts.save(str(i)+".mp3")
	x = AudioSegment.from_mp3(str(i)+'.mp3')
	x.export(str(i)+'.wav','wav')
	stretch(str(i)+'.wav')
	list_audio.append(str(i)+'.wav')

joinwav(list_audio, 'final_aud.wav')
overlap_audio('final_aud.wav',inpFile)




