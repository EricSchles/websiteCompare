from website_grab import Grabber
import requests
g = Grabber()

baseurl = "https://www.google.com"
links = g.map_website(baseurl,depth=2)

for link in links:
    r = requests.get(link)
    g.save(baseurl,r)

for link in links:
    g.webpage_grab(baseurl,link)

