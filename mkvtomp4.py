import os
import subprocess

mkv_list = os.listdir(os.getcwd())

subtitles = input('Use Subtitles? y/n ')
#threads = input('Number of threads: ')

for mkv in mkv_list:
    name, ext = os.path.splitext(mkv)

    if ext == ".mp4": 
        continue
    output_name = name + ".mp4"

    #input()

    if subtitles == 'y':
        try:
            subprocess.run(
            ["ffmpeg","-y" ,"-i", f"{mkv}", '-vf', f"subtitles={mkv}:stream_index=1","-threads", '6', '-vcodec', 'libx264', '-acodec', 'aac','-movflags', '+faststart', f"{output_name}"], check=True
        )
        except:
            raise Exception(
                "Please DOWNLOAD, INSTALL & ADD the path of FFMPEG to Environment Variables!"
            )
    
    else:
        try:
            subprocess.run(
            ["ffmpeg","-y" ,"-i", f"{mkv}","-threads", '6', '-vcodec', 'libx264', '-acodec', 'aac','-movflags', '+faststart', f"{output_name}"], check=True
        )
        except:
            raise Exception(
            "Please DOWNLOAD, INSTALL & ADD the path of FFMPEG to Environment Variables!"
        )


print(f"{len(mkv_list)} video(s) converted to MP4!")
os.startfile("result")
