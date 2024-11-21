import asyncio
import aiogram
from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.bot import DefaultBotProperties 
# from aiogram.fsm.properties.memory import MemoryStorage
from aiogram.fsm.storage.memory import MemoryStorage

from config import BOT_KEY
from handlers import router

async def main():
  bot = Bot(token=BOT_KEY, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
  dp = Dispatcher(storage=MemoryStorage())
  dp.include_router(router)
  await bot.delete_webhook(drop_pending_updates=True)
  await dp.start_polling (bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == "__main__":
  asyncio.run(main())
