from config import API_KEY
from bs4 import BeautifulSoup

import requests
import time


# lat:float = 56.19
# lon:float = 44.00

url = "https://yandex.ru/weather/nizhny-novgorod"

def check_connect(new_url):
  response = requests.get(new_url)
  print(response)
  soup = BeautifulSoup(response.text, "html.parser")
  if soup:
    # print(soup.prettify())
    return soup
  else: return -1
def formatted_data(soup):
  result = dict()

  data = soup.find("div", class_="content__top")
  # data2 = soup.find("div", class_="fact__title")
  if not data:
    return "No data"
  info = data.find_all("span")
  title = data.find("h1").text
  now_temper = data.find("a")['aria-label']
  wind = info[8].text
  humidity = info[9].text
  pressure = info[11].text[:14]
  # for i in range(15):
    # data_test = data.find_all("span")[i]
    # print(data_test.text, " ", i)
  # result.append(f"{title}\n{now_temper}n{wind}\n{humidity}\n{pressure} мм рт. ст.")
  result["text"] =(f"{title}\n{now_temper}\n{wind}\n{humidity}\n{pressure} мм рт. ст.")
  # result["url_photo"] = data.find_all("img")["src"]
  # print(data.find("img")["src"])
  # print(type(result))
  # print(f"{title}\n{now_temper}")
  # print(data.prettify())
  # print("RETURNED: ", f"{title}\n{now_temper}n{wind}\n{humidity}\n{pressure} мм рт. ст.")
  # return f"{title}\n{now_temper}n{wind}\n{humidity}\n{pressure} мм рт. ст."
  return result

sp:BeautifulSoup


def get_data(new_url):
  while True:
    sp = check_connect(new_url)
    if sp != -1:
      break
    time.sleep(2)
    print("check: next check in 2 seconds")

  return formatted_data(sp)

# get_data(url)
# print(response.status_code)


# print(data.find_all("div",class_="fact_props"))
