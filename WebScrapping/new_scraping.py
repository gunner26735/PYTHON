from bs4 import BeautifulSoup
from bs4.element import ResultSet
import requests

#tosearch =input("Enter item to search on web:")
#param = {"q":tosearch}
r =requests.get("https://en.wikipedia.org/wiki/Machine_learning")

print(r.status_code)

fetchsoup = BeautifulSoup(r.content,"lxml")
results = fetchsoup.findAll("span",attrs={"class":"mw-headline"})

content = str(results).split(",")
for val in content:
    print(val)