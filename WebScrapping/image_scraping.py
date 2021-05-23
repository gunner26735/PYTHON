from bs4 import BeautifulSoup
import requests
import urllib.request
from PIL import Image
from io import BytesIO
 
r =requests.get("http://www.reddit.com/r/Guns")

fetchimage = BeautifulSoup(r.content,"html.parser")
resimage = fetchimage.find_all("img",attrs={"alt":"Post image"})

num = 0
for getimg in resimage:
    imgsrc = getimg["src"]
    print(imgsrc)
    urllib.request.urlretrieve(imgsrc,"WebScrapping/scraped_images/"+str(num))
    #img_obj = requests.get(imgsrc)                                 #This three commented lines can also be used for image scrapping
    #img = Image.open(BytesIO(img_obj.content))
    #img.save("WebScrapping/scraped_images/"+str(num),img.format)
    num +=1

