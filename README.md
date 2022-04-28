# voiceApp
A python script backed with Nim modules through the Nimpy library to do offline translation between english audio or text input to japanese with voice output!


License: MIT License

Codes based on:
Python 3.10 -- Python Software Foundation License Version 2 and Zero-Clause BSD License
Nim language and standard library MIT License
https://github.com/Pebaz/nimporter MIT License
https://github.com/yglukhov/nimpy MIT License
https://github.com/demotomohiro/nimopenjtalk MIT License
https://github.com/alphacep/vosk-api Apache-2.0 License
https://github.com/LibreTranslate/LibreTranslate AGPL-3.0 License (only API access)
https://github.com/Uberi/speech_recognition All Rights Reserved (ok as library)
https://github.com/scipy/scipy BSD-3-Clause License

The code uses models from http://open-jtalk.sourceforge.net/ (Modified BSD license, attribution) and http://www.mmdagent.jp/ (Modified BSD license, attribution)

Requirements:
Nim: Nim 1.6.4 and nimpy.
Python: vosk, speechrecognition, nimporter, scipy, sounddevice and soundfile
Libretranslate server. I recommend using venv, conda, or docker.
Due to directory links, it will probably only run on OSX and Linux for now.

Please put open_jtalk_dic_utf_8-1.11 and MMDAgent model mei/mei_normal.htsvoice into /data/
Please put vosk-model-small-en-us-0.15 into the same folder as the program.
They can be downloaded in the linked websites.


Usage:
Please install Nim version 1.6.4, then run `nimble install nimpy`

Then compile the nim source codes as:

`nim cpp --app:lib -d:release --out:texttospeech.so --threads:on texttospeech.nim`
And
`nim c --app:lib -d:release --out:lt_api_func.so --threads:on lt_api_func.nim` 

I provide the compiled texttospeech.so and lt_api_func.so in the main folder as well.

Then, start libretranslate on http://localhost:5000 (hardcoded for now, sorry!) with flag " --load-only en,ja", and invoke python voiceapp.py

Please follow the instructions in the CLI.
Every temporary files (inputrecording.wav, inputprocessed.wav, and output.wav) is put into the /temp folder. All translations are logged by default on log.txt 
(N.B. you may need to change the default device for microphone in the voiceapp.py script. It's in the sd.default.device variable)

Thank you to demotomohiro and Yardanico for the kind guidance and patience in helping me develop this app. I was totally new to the Nim language. Thank you once again. 
