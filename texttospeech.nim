import ./nimopenjtalk/src/nimopenjtalk/nimojtutil
import nimpy

var
    context = createContext()
    voice = createVoice()
    txt: string = "default translation"

proc speech_prep =
    defer:
        voice.clear()
        context.clear()

        if not context.load("./data/open_jtalk_dic_utf_8-1.11"):
            echo "Failed to load dictionary"
        if not voice.load("./data/mei/mei_normal.htsvoice"):
            echo "Failed to load voice"

proc speech_synthesis*(txt: string) {.exportpy.} =
    speech_prep()
    if context.synthesis(voice, txt):
        writeWave(voice, "output.wav")
    else:
        echo "Error: waveform can not be synthetised"

