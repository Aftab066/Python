import win32com.client as wincl

speaker_number = 0
spk = wincl.Dispatch("SAPI.SpVoice")
vcs = spk.GetVoices()
# SVSFlag = 11
# print(vcs.Item (speaker_number) .GetAttribute ("Name")) # speaker name
spk.Voice
spk.SetVoice(vcs.Item(speaker_number)) # set voice (see Windows Text-to-Speech settings)
lst = ["Shoutout To Aftab",
       "Shoutout To Omkar",
       "Shoutout To Nikhil"]

for i in lst:   
    print(i)
    spk.Speak(i)
# spk.Speak("All Out")
