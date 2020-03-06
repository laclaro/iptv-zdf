
# iptv-zdf

Since the streams offered by ZDF are not handled correctly by ffmpeg, this script extracts
audio and video stream urls from the master.m8u and prints a complete iptv pipe list for
tvheadend.

Eventually run this script as cron job piping the output into a file

`~$ python3 iptv-zdf-pipe.py > /home/hts/ZDF-HD.m3u`

Tvheadend imports local files with the *IPTV Automatic Network* by giving an url, such as

`file:///home/hts/ZDF-HD.m3u`


Credits:
--------

Thanks to the insightful thread in the `ComputerBase Forums https://www.computerbase.de/forum/threads/mit-mpc-be-stream-aufnehmen.1922912/ and the `kodinerds iptv list https://github.com/jnk22/kodinerds-iptv
