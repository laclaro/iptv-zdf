#!/usr/bin/python3


""" Simple script to extract audio and video streams from ZDF, ZDFneo and ZDFinfo m8u files 
and build a pipe command with ffmpeg for tvheadend.
Icon files are included from https://github.com/jnk22/kodinerds-iptv
"""

__author__ = "Henning Hollermann"
__contributor__ = "https://www.computerbase.de/forum/members/axel-erfurt.818532/"

import requests

def return_extinf(channel):
    """ returns the extinf string """
    return '#EXTINF:-1 tvg-name="{0} HD" tvg-id="{0}.de" group-title="{0}" tvg-logo="{1}",{0} HD'.format(channel,logo[channel])


def build_pipe():
    """ This function build the pipe commands by extracting streams from the given urls """

    for channel in pipe:
        result = requests.get(url[channel])
        t = result.text
        audio = t.partition('NAME="TV Ton",LANGUAGE="deu",DEFAULT=YES,URI="')[2].partition('"')[0]
        video = t.partition('RESOLUTION=1280x720\n')[2].partition('\n')[0]
        pipe[channel] = 'pipe://ffmpeg -loglevel fatal -i {} -i {} -vcodec copy -acodec copy -metadata service_name={}\ HD -metadata service_provider=ZDF -mpegts_service_type advanced_codec_digital_hdtv -f mpegts pipe:1'.format(audio,video,channel)


def print_extm3u():
    """ prints the file to be included with tvheadend """

    print("#EXTM3U")
    for channel in pipe:
        print(extinf[channel])
        print(pipe[channel])


url = {"ZDF":"http://zdf-hls-01.akamaized.net/hls/live/2002460/de/veryhigh/master.m3u8",
       "ZDFneo":"http://zdf-hls-02.akamaized.net/hls/live/2002461/de/veryhigh/master.m3u8",
       "ZDFinfo":"http://zdfhls17-i.akamaihd.net/hls/live/744750/de/veryhigh/master.m3u8"}

logo = {"ZDF":'https://raw.githubusercontent.com/jnk22/kodinerds-iptv/master/logos/tv/zdfhd.png',
        "ZDFneo":'https://raw.githubusercontent.com/jnk22/kodinerds-iptv/master/logos/tv/zdfneohd.png',
        "ZDFinfo":'https://raw.githubusercontent.com/jnk22/kodinerds-iptv/master/logos/tv/zdfinfohd.png'}

extinf = {"ZDF":return_extinf("ZDF"),"ZDFneo":return_extinf("ZDFneo"),"ZDFinfo":return_extinf("ZDFinfo")}

pipe   = {"ZDF":"","ZDFneo":"","ZDFinfo":""}



build_pipe()
print_extm3u()
