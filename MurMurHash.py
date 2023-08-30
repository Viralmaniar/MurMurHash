import mmh3
import requests
import codecs
import sys

if len(sys.argv) != 2:
    print("USAGE: MurMurHash FAVICON_URL")
    exit(0)

requests.packages.urllib3.disable_warnings()

response = requests.get(sys.argv[1], verify=False)
print(f"Go to https://www.shodan.io/search?query=http.favicon.hash%3A{mmh3.hash(codecs.encode(response.content,'base64'))}")
