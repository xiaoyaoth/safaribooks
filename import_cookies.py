import json

# view and export cookies by using Chrome
# https://developer.chrome.com/docs/devtools/storage/cookies/
# view sample exported cookies in in.json and sample output in out.json
# rename out.json to cookies.json to continue using safaribooks.py

file_in = open("in.json","r")
map_in = json.load(file_in)
# print(map_in)

map_out = {}
for item in map_in:
  map_out[item['name']] = item['value']

json.dump(map_out, open("out.json","w"))
