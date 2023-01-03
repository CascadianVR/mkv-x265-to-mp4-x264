import os
import subprocess

mkv_list = os.listdir(os.getcwd())

subtitles = input('Use Subtitles? y/n ')

if subtitles == 'y':
    subindex = input('Subtitle Index: ')

threads = input('Number of threads: ')

for mkv in mkv_list:
    name, ext = os.path.splitext(mkv)

    if ext == ".mp4": 
        continue
    if ext == ".py": 
        continue
    output_name = name + ".mp4"

    #input()

    if subtitles == 'y':
        try: #'-metadata:s:a:0 language=eng',
            subprocess.run(
            ["ffmpeg","-y" ,"-i", f"{mkv}", '-map', '0:0', '-map', f'0:1','-vf', f"subtitles={mkv}:stream_index={subindex}","-threads", f'{threads}', '-vcodec', 'libx264', '-acodec', 'aac', '-preset', 'medium', '-pix_fmt', 'yuv420p','-movflags', '+faststart', '-metadata:s:a:1','title=jpn', f"{output_name}"], check=True
        )
        except:
            raise Exception(
                "Please DOWNLOAD, INSTALL & ADD the path of FFMPEG to Environment Variables!"
            )
    
    else:
        try:
            subprocess.run(
            ["ffmpeg","-y" ,"-i", f"{mkv}","-threads", f'{threads}', '-vcodec', 'libx264', '-acodec', 'aac', '-preset', 'medium', '-pix_fmt', 'yuv420p','-movflags', '+faststart', '-metadata:s:a:1','title=jpn', f"{output_name}"], check=True
        )
        except:
            raise Exception(
            "Please DOWNLOAD, INSTALL & ADD the path of FFMPEG to Environment Variables!"
        )


print(f"{len(mkv_list)} video(s) converted to MP4!")

