from pytube import YouTube
import os


#User enters the desired URL
video_url = input("Enter Youtube URL: ").strip()
yt = YouTube(video_url)


#Filter for the best quality video with audio and download it 
yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution().download(filename="video")
os.rename("video.mp4", f"{yt.title}.mp4")

print(f"Video {yt.title} was downloaded.")
#Download the audio with name 'audio'
#audio = youtube_obj.streams.filter(only_audio=True)
#audio[0].download(filename="audio")


#video_stream = ffmpeg.input('video.mp4')
#audio_stream = ffmpeg.input('audio.mp4')
#ffmpeg.output(audio_stream, video_stream, f'{youtube_obj.title}.mp4').run()
