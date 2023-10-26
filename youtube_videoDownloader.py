from pytube import YouTube
import sys 

link = sys.argv[1]

yt = YouTube(link)

print("Title : ", yt.title)
print("Views: ", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download('D:\Downloads\Video')