from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from weather_api import get_data
import json

router = Router()


dict_of_cities = {}

with open('cities.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    dict_of_cities = data

# print(data)
print("Bot is ready")


@router.message(Command("start"))
async def start_handler(msg:Message):
  await msg.answer("Hello")

@router.message()
async def send_info(msg:Message):
  url = "https://yandex.ru"
  # compl_url = f"{url}{dict_of_cities[msg.text]}"
  # print("try to get info from: {compl_url}")  
  try:
    compl_url = f"{url}{dict_of_cities[msg.text]}"
    print("try to get info from: {compl_url}")
    data:dict = get_data(compl_url)
    await msg.answer(data["text"])
  except:
    await msg.answer("Такого города пока что нет, плаки плаки лысый \n<code>Ну либо ошибка на сервере, но это маловероятно</code>")
