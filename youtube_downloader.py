from pytube import YouTube
from pytube import Playlist
import os
import moviepy.editor as mp
import re

# Name of the folder and url of the playlist
folder = "./custom_song"
url = "https://www.youtube.com/playlist?list=PLQD9v8pn7Xi7bqIfuq-Q6h_9aeuMpPpel"


playlist = Playlist(url)

#prints each video url, which is the same as iterating through playlist.video_urls
for url in playlist:
    print(url)


print('The Number of Songs are', len(url))
if not os.path.isdir(folder):
    os.makedirs(folder, mode=0o777, exist_ok=True)

index = 0
for url in playlist:
    index = index + 1
    try:
        YouTube(url).streams.filter(only_audio=True).first().download(folder)
        print('%s- The url %s is downloaded' % (index, url))
    except Exception as e:
        print("%s- This url %s cannot be downloaded" % (index, url))
        print(e)

# for url in playlist:
#     YouTube(url).streams.first().download(folder)

index = 0
for file in os.listdir(folder):
    index = index + 1
    print("Song %s will be convert to mp3" % index)
    if re.search('mp4', file):
        mp4_path = os.path.join(folder, file)
        mp3_path = os.path.join(folder, os.path.splitext(file)[0]+'.mp3')
        new_file = mp.AudioFileClip(mp4_path)
        new_file.write_audiofile(mp3_path)
        os.remove(mp4_path)