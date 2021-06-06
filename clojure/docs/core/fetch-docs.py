import requests
from scrapy.selector import Selector as sel
import sys

uri = sys.argv[1]

if not uri.startswith("https://clojuredocs.org"):
    print("only clojure docs supported")
else:
    text = requests.get(uri).text
    cmds = sel(text=text).css(".dl-horizontal > .dl-row > .name > a::text").extract()
    docs = sel(text=text).css(".dl-horizontal > .dl-row > .doc::text").extract()
    res = dict(zip(cmds, docs))
    breakpoint()
