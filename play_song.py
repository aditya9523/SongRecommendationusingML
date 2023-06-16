import random
import os
n = random.randint(0,10)
print(n)

music_dir = 'D:/SONG RECOMENDATION SYSTEM/Punjabi'
songs = os.listdir(music_dir)
print(songs)    
os.startfile(os.path.join(music_dir, songs[n]))