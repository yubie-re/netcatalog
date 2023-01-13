import requests
import zlib
import json

rsaccess_token = "" # This needs to be dumped from the game (not to be confused with GSINFO, this will be a base64 blob)
transaction_subdomain = "" # This needs to be dumped from the game, e.g prod.p01ewr.pod.rockstargames.com (this gets assigned to you)

result = requests.get("https://" + transaction_subdomain + "/gta5/11/GamePlayServices/GameTransactions.asmx/GetCatalog", headers={ "Authorization": "RSACCESS token=" + rsaccess_token })
catalog = json.loads(zlib.decompress(result.content, -15))
version = catalog["version"]
f = open('Catalog_' + str(version) + '.json', "w")
f.write(json.dumps(catalog, indent=4))
f.close()