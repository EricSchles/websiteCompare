from website_grab import Grabber
import requests
import sys
g = Grabber()


baseurl = sys.argv[1]
if sys.argv[2].lower() == "true":
    new = True
elif sys.argv[2].lower() == "false":
    new = False
else:
    new = ''

links = g.map_website(baseurl,depth=3)

if new == '':
    print "must tell me whether this is a new website or not"
    print "format as follows:"
    print "python main.py [website name] [True or False - pick one]"
    print "example: python main.py https://www.google.com True"
    print "example2: python main.py https://www.google.com False"
    sys.exit(0)

if new:
    for link in links:
        r = requests.get(link)
        g.save(baseurl,r)
else:
    for link in links:
        g.webpage_grab(baseurl,link)
