import requests
import time
import os
from glob import glob
import lxml.html

class Grabber:
    def save(self,r):
        if not os.path.exists("pages"):
            os.mkdir("pages")
        os.chdir("pages")
        name = "".join(r.url.split("/")[-2:])
        with open(name+".html","w") as f:
            text = r.text.encode("ascii","ignore")
            f.write(text)
        os.chdir("../")
        return name+".html"

    def webpage_grab(self,url):
        r = requests.get(url)
        name = "_".join(r.url.split("/")[-2:]).replace(".html","")
        if not os.path.exists(name):
            os.mkdir(name)
        os.chdir(name)
        now = time.strftime("%m_%d_%y_%H")
        folder = os.path.join(os.getcwd(), name)
        html_files = [file for file in glob(os.path.join(folder,'*.html'))]
        html_files.sort(key=os.path.getmtime)
        most_recently_edited = html_files[-1]
        previous = open(most_recently_edited,"r").read()
        text = r.text.encode("ascii","ignore")
        if text != previous:
            with open(name+now+".html","w") as f:
                f.write(r.text)

    def map_website(self,base_url,depth=15):
        r = requests.get(base_url)
        links = []
        urlname = base_url.split("//")[1].split("/")[0]
        return mapper(base_url,urlname,links,depth)

    def mapper(self,url,urlname,links,depth):
        if depth <= 0:
            return links
        r = requests.get(url)
        html = lxml.html.fromstr(r.text)
        tmp = html.xpath("//a/@href")
        for link in tmp:
            if urlname in link:
                tmp_links = mapper(link,urlname,links,depth-1)
                links += [link for link in tmp_links if not link in links]
                if not link in links:
                    links.append(link)
        return links

