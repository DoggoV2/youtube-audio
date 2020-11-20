from os import system
import json
from youtubesearchpython import SearchVideos



se = input('Search: ')
search = SearchVideos(se, offset = 1, mode = "json", max_results = 1)


response = json.loads(search.result())

link = response['search_result'][0]['link']


print(response['search_result'][0]['title'])

system('youtube-dl --force-ipv4 --extract-audio --audio-format mp3 '+link)



