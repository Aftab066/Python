import win32com.client as wincl

speaker_number = 0
spk = wincl.Dispatch("SAPI.SpVoice")
vcs = spk.GetVoices()
# SVSFlag = 11
print(vcs.Item (speaker_number) .GetAttribute ("Name")) # speaker name
spk.Voice
spk.SetVoice(vcs.Item(speaker_number)) # set voice (see Windows Text-to-Speech settings)
spk.Speak("Hey I Am Jarvis")
spk.Speak("Welcome To Aftab's Lab")
spk.Speak("Here I Am Your Assistant")
spk.Speak("All Out")
