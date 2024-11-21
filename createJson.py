import pprint
from weather_api import check_connect
from bs4 import BeautifulSoup
import json

dict_of_city = {}
regions = []
url_of_cities = "https://yandex.ru/weather/ru-RU/region/russia"

data:BeautifulSoup = check_connect(url_of_cities)
# print(data.prettify())
# print(data.find("a", class_="AppRegion_list__sub__MvdSO"))
for region_container in data.find_all("section", class_="AppRegion_region__Oymus"):
  for region in region_container.find_all("a"):
    print(region["href"])
    regions.append(region["href"])
#   # print(region)
#   if "/weather/ru-RU/region/" in region["href"]:
# # print(regions)

for region in regions:
  region_data = check_connect(f"https://yandex.ru{region}")
  for city in region_data.find_all("a"):
    # print(city["href"])
    pass
    if "/weather" in city["href"]:
      dict_of_city[city.text] = city["href"]
      # print(city["href"])
      pass
    
pprint.pp(dict_of_city)

with open("cities.json", "w", encoding="utf-8") as f:
  json.dump(dict_of_city, f, ensure_ascii=False, indent=4)