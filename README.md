# Vindex

A search tool that plays the video from a place where a search term exists using subtitles. Uses *autosub* to generate subtitles and *vlc* to play files.

Runs on python3.

Install autosub using
```
pip install autosub
```

Install vlc.

Place the video files and subtiles(if exists) in the same folder

If the subtitles don't exist, it'll auto generate.

Download the repository

Run 
```
chmod +x seek.sh && chmod +x vid.sh
```
in your terminal, from the folder where it is downloaded.(Only for the first time)

Now run
```
python vindex.py
```

Enter file name then after subtitle generation enter your search term.

In case your query doesn't match any result, try entering a word that might appear close to it.
