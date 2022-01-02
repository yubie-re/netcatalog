import requests
import zlib
import json

latest_known_ver = 829 # we can't get the latest catalog without ros access, so we need to make a method to find it
while True: # loop through the versions until we hit a 404
    result = requests.get('http://prod.cloud.rockstargames.com/titles/gta5/pcros/gamecatalog/Catalog_' + str(latest_known_ver) + '.zip')
    if result.status_code == 404:
        break
    latest_known_ver += 1
    last_real_result = result 

f = open('Catalog_' + str(latest_known_ver) + '.json', "w")
f.write(json.dumps(json.loads(zlib.decompress(last_real_result._content, -15)), indent=4))
f.close()