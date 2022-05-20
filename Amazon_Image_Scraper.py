from bs4 import BeautifulSoup
import urllib3
import random
import urllib.request

url = "https://www.amazon.com/s?k=wedding+fabric&i=arts-crafts&rh=n%3A2617941011%2Cp_n_material_browse%3A316507011%2Cp_n_srvg_2947266011%3A2637798011&dc&qid=1583481523&rnid=2947266011&ref=sr_nr_p_n_srvg_2947266011_1"

for i in range(1,53):
  if i >= 2:
    url ="https://www.amazon.com/s?k=wedding+fabric&i=arts-crafts&rh=n%3A2617941011%2Cp_n_material_browse%3A316507011%2Cp_n_srvg_2947266011%3A2637798011&dc&page=" + str(i) +"&qid=1583481625&rnid=2947266011&ref=sr_pg_2" 
  http = urllib3.PoolManager()

  source_code = http.request("GET", url)

  plain_text = source_code.data


  soup = BeautifulSoup(plain_text, "lxml")

  for link in soup.find_all("img", ("class","s-image")):
    src = link.get("src")
    if src == None:
      src = link.get("data-src")

    img_name = random.randrange(1,100000000000000000000000000)

    full_name = str(img_name) + ".jpg"

    urllib.request.urlretrieve(src, full_name)
