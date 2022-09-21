# import speech_recognition as sr
# import pyaudio
# from pydub import AudioSegment
# from pydub.utils import make_chunks

# #This code will take in a wav file and output the audio to text

# #********Input wav file for speech to text translation*************
# #sound = AudioSegment.from_file("3574_NormalText_9-11-20.wav" , "wav") 

# r = sr.Recognizer()
# with sr.Microphone() as source:
#     print("Say something!")
#     sound = r.listen(source)


# chunk_length_ms = 9000 # pydub is used to calculate in millisec
# chunks = make_chunks(sound, chunk_length_ms) #Turns the milisecond lenght in the chunk

# #sound = AudioSegment.from_mp3("/path/to/file.mp3")
# #sound.export("/output/path/file.wav", format="wav")
# # Used to convert from mp3 to wav
# for i, chunk in enumerate(chunks):
#     chunk_name = "chunk{0}.wav".format(i)
#     print ("exporting", chunk_name)
#     chunk.export(chunk_name, format="wav")

# i=0
# for chunk in chunks:
#     #print ("in chunks")
#     chunk_silent = AudioSegment.silent(duration = 10)
#     audio_chunk = chunk_silent + chunk + chunk_silent
#     #audio_chunk.export("./chunk{0}.wav".format(i), bitrate ='192k', format ="wav")
#     filename = 'chunk'+str(i)+'.wav'
#     #print("Processing chunk "+str(i))
#     file = filename
#     r = sr.Recognizer()
#     with sr.AudioFile(file) as source:
#         #r.adjust_for_ambient_noise(source)
#         audio_listened = r.listen(source)
#     try:
#         rec = r.recognize_google(audio_listened)
#         print (rec)
#     except:
#         rec = r.recognize_google(audio_listened,show_all=True) # all possibilities 
#         print(rec,type(rec))

#     i = i+1


#!/usr/bin/env python3
# Requires PyAudio and PySpeech.

import speech_recognition as sr

# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# print("a")
# Speech recognition using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("You said: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


