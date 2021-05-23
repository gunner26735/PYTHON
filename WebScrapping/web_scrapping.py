import requests
from bs4 import BeautifulSoup

tosearch =input("Enter item to search on web:")
param = {"q":tosearch}
r =requests.get("https://www.google.com/search",params=param)

print(r.status_code)

fettchsoup = BeautifulSoup(r.text, "html.parser")
#print(fettchsoup.prettify())  #: This code will print the whole souce code of page.   UNCOMMENT to print in console

newfile = open("WebScrapping/data.html","w+")
newfile.write(r.text)
