# -*-coding:utf-8 -*-
import sys
import NeteaseCloudMusic

song_name = sys.argv[1]
print NeteaseCloudMusic.search_song_by_name(song_name)
