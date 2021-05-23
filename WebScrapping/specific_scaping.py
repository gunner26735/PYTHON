import requests
from bs4 import BeautifulSoup

# Now we will print the specific result from link
tosearch =input("Enter item to search on web:")
param = {"q":tosearch}
r =requests.get("https://www.google.com/search",params=param)

fettchsoup = BeautifulSoup(r.text, "html.parser")

results = fettchsoup.find("div", {"id":"main"})
links = results.findAll("div", {"class":"kCrYT"})

#print(type(links))
#print(results)

for item in links:
    item_href = item.find("a")

    if  item_href:
        print(item_href,"\n")
