import sys 
from ripgrepy import Ripgrepy
# The Ripgrepy class takes two arguments. The regex to search for and the folder path to search in
seearch_string ="'.+\.png'"
rg = Ripgrepy(seearch_string, './images/')

search_raw = rg.json().run().as_dict
if len(search_raw) == 0:
    print("nothing found that matches",seearch_string )
    sys.exit
searchs = [line["data"]["lines"]["text"] for line in search_raw]
# search_raw
for result in searchs:
    print(result) 
# the same can be executed using the rg shorthands
searchs
# rg.H().n().run().as_string