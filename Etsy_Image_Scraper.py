from bs4 import BeautifulSoup
import urllib3
import random
import urllib.request

url = "https://www.etsy.com/search?q=lace+fabric&explicit=1&attr_1=10"

for i in range(1,249):
  if i >= 2:
    url ="https://www.etsy.com/search?q=lace+fabric&explicit=1&attr_1=10&ref=pagination&page=" + str(i)
  http = urllib3.PoolManager()

  source_code = http.request("GET", url)

  plain_text = source_code.data


  soup = BeautifulSoup(plain_text, "lxml")

  for link in soup.find_all("img", ("class","width-full wt-height-full display-block position-absolute")):
    src = link.get("src")
    if src == None:
      src = link.get("data-src")

    img_name = random.randrange(1,100000000000000000000000000)

    full_name = str(img_name) + ".jpg"

    urllib.request.urlretrieve(src, full_name)
