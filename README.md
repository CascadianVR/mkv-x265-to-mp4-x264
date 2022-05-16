# mkv-x265-to-mp4-x264
A simple Python script I made using ffmpeg to convert mkv x265 videos to web supported mp4 x264.  
Usually the provess would be simple converting form mkv to mp4.  
However, since the codec also needs to be switched since x265 is not supported on most browsers it's more work.  
Additionally, there are options for using subtitles and how many threads should be used.

## Install and Usage
You will first need to install **ffmpeg** and make sure to setup the enviroment variable under PATH if it's not already.

**ffmpeg Download:** https://ffmpeg.org/download.html  
**Environment Variable:** https://www.thewindowsclub.com/how-to-install-ffmpeg-on-windows-10  
  
Next, place the downloaded .py script in the directory with the videos inside it.  
You can run it directly form python or from the command line typing "python mkvtomp4.py"  

Once it is run, it will ask you if you want to burn in the subtitles and how many threads you want to use.  
After that you hsould be good and it will go through each .mkv file and output the .mp4 in the same folder.

