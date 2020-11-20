from os import system
import json
from youtubesearchpython import SearchVideos
import time

time.sleep(3)
se = input('Search: ')
search = SearchVideos(se, offset = 1, mode = "json", max_results = 1)

time.sleep(1)
response = json.loads(search.result())

link = response['search_result'][0]['link']


print(response['search_result'][0]['title'])
time.sleep(15)
system('youtube-dl --force-ipv4 --extract-audio --audio-format mp3 '+link)



