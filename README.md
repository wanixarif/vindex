# Vindex
>Video Indexing tool

Your Ctrl+F kind of utility for videos!

Enter your search term in text format and see where the phrase exists in the video and be able to directly play from that position, also tries to find the closest possible matches if your query doesn't exist.

Runs on python3.

Install autosub and ffmpeg using
```
pip install autosub
```
```
sudo YOUR-PACKAGE-MANAGER-INSTALL-COMMAND ffmpeg
```
YOUR-PACKAGE-MANGER-INSTALL-COMMAND = "apt install" or "pacman -Sy" or yum or dnf, depends on your distro

>Install vlc media player.

Download this repository

Run 
```
chmod +x seek.sh && chmod +x vid.sh
```
in your terminal, from within the folder where it is downloaded.(Only for the first time)

Place the video files and subtiles(if exists) in the same folder

If the subtitles don't exist, it'll auto generate.

Now run
```
python vindex.py
```
if it gives errors try
```
python3 vindex.py
```

Enter file name (with extension) then after subtitle generation enter your search term or phrase.
