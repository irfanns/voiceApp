import speech_recognition as sr
import nimporter
import texttospeech
import lt_api_func
import os
from sh import mpv
import time
from scipy.io.wavfile import write
import sounddevice as sd
import soundfile as sf
import vosk
import wave
import json
import datetime

text = "default string"

# check devices:
devices = sd.query_devices(device = None, kind = None)
# Recording properties
SAMPLE_RATE = 44100
SECONDS = 10
# Channels
MONO = 1
STEREO = 2

sd.default.device = 4

def record():

    print("Recording for 10 seconds")
    time.sleep(3)

    recording = sd.rec( int(SECONDS * SAMPLE_RATE),
                   samplerate = SAMPLE_RATE, channels = MONO)
    sd.wait()

    write("inputrecording.wav", SAMPLE_RATE, recording)

# Convert recording.wav to 16-bit PCM

    data,samplerate = sf.read("inputrecording.wav")
    sf.write("inputprocessed.wav", data, samplerate, subtype = "PCM_16")
print("Do you want to record a voice or translate written word? 1 or 2, please")
voice_record_bool = str(input())
if voice_record_bool.lower() == "1":
    record()
else:
    print("We continue to the voice recognition")

def recog():
    # load vosk Model and start the recognition
    wf = wave.open("inputprocessed.wav", "rb")
    model = vosk.Model("vosk-model-small-en-us-0.15")
    rec = vosk.KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)
    results = []
    text = ''

    # do the recognition and convert i
    while True:
        data = wf.readframes(40000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            part_result = json.loads(rec.Result())
            results.append(part_result)

        part_result = json.loads(rec.FinalResult())
        results.append(part_result)

# forming a final string from the words
    for r in results:
        text += r['text'] + ' '

if voice_record_bool.lower() == "1":
        recog()
else:
    print("Please input your to-be translated text")
    text = str(input())

print("We continue to the voice output")



print(f"Original words to translate: {text}")


# translate through texttospeech (written in Nim, uses libretranslate server)
x = lt_api_func.translate_text(text)

print(f"Translated words in Japanese: {x}")
if isinstance(x, str):
    # output speech through nimopenjtalk
    y = texttospeech.speech_synthesis(x)
    mpv("output.wav")
else:
    print("you didn't give a string!")

current_time = datetime.datetime.now()
current_timestr = str(current_time)
with open('log.txt', 'a') as f:
    f.write(current_timestr + " " + text + "\n")
    f.write(current_timestr + " " + x + "\n")
